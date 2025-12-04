from flask import Blueprint, jsonify, request
from extensions import db
from models import User, RequirementManagement
from datetime import datetime

# 创建蓝图
api = Blueprint('api', __name__)

# 用户相关接口

# 获取所有用户
@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# 获取单个用户
@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

# 创建用户
@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data.get('password'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# 更新用户
@api.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    if data.get('password') is not None:
        user.password = data.get('password')
    db.session.commit()
    return jsonify(user.to_dict())

# 删除用户
@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 204

# 用户登录
@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': '用户名和密码不能为空'}), 400
    
    # 查询用户
    user = User.query.filter_by(username=username).first()
    
    if not user or user.password != password:
        return jsonify({'message': '用户名或密码错误'}), 401
    
    # 登录成功，返回用户信息
    return jsonify({
        'message': '登录成功',
        'user': user.to_dict()
    }), 200

# 需求管理相关接口

# 获取下拉选项值
@api.route('/requirements/options', methods=['GET'])
def get_requirement_options():
    # 获取大类的唯一值
    categories = db.session.query(RequirementManagement.category).distinct().all()
    # 获取版块的唯一值
    sections = db.session.query(RequirementManagement.section).distinct().all()
    # 获取对接部门的唯一值
    departments = db.session.query(RequirementManagement.department).filter(RequirementManagement.department.isnot(None)).distinct().all()
    # 获取是否已对接的唯一值
    is_connected_values = db.session.query(RequirementManagement.is_connected).distinct().all()
    # 获取是否需要协调的唯一值
    need_coordination_values = db.session.query(RequirementManagement.need_coordination).distinct().all()
    # 获取计划对接时间的唯一值
    planned_time_values = db.session.query(RequirementManagement.planned_time).filter(RequirementManagement.planned_time.isnot(None), RequirementManagement.planned_time != '').distinct().all()
    
    return jsonify({
        'categories': [category[0] for category in categories],
        'sections': [section[0] for section in sections],
        'is_connected_list': [{'value': value[0], 'label': value[0]} for value in is_connected_values],
        'need_coordination_list': [{'value': value[0], 'label': value[0]} for value in need_coordination_values],
        'departments': [department[0] for department in departments],
        'planned_time_list': [planned_time[0] for planned_time in planned_time_values]
    })

# 获取所有需求（支持过滤和搜索）
@api.route('/requirements', methods=['GET'])
def get_requirements():
    # 获取查询参数
    category = request.args.get('category')
    section = request.args.get('section')
    is_connected = request.args.get('is_connected')
    department = request.args.get('department')
    requirement_name = request.args.get('requirement_name')
    planned_time = request.args.get('planned_time')
    
    # 构建查询
    query = RequirementManagement.query
    
    # 应用过滤条件
    if category:
        query = query.filter_by(category=category)
    if section:
        query = query.filter_by(section=section)
    if is_connected is not None:
        query = query.filter_by(is_connected=is_connected)
    if department:
        query = query.filter_by(department=department)
    if requirement_name:
        query = query.filter(RequirementManagement.requirement_name.like(f'%{requirement_name}%'))
    if planned_time:
        query = query.filter_by(planned_time=planned_time)
    
    # 执行查询
    requirements = query.all()
    return jsonify([req.to_dict() for req in requirements])

# 获取单个需求
@api.route('/requirements/<int:req_id>', methods=['GET'])
def get_requirement(req_id):
    requirement = RequirementManagement.query.get_or_404(req_id)
    return jsonify(requirement.to_dict())

# 创建需求
@api.route('/requirements', methods=['POST'])
def create_requirement():
    data = request.get_json()
    
    new_requirement = RequirementManagement(
        category=data['category'],
        section=data['section'],
        requirement_name=data['requirement_name'],
        is_connected=data.get('is_connected', '否'),
        department=data.get('department'),
        data_system=data.get('data_system'),
        data_name=data.get('data_name'),
        data_quality=data.get('data_quality'),
        data_status=data.get('data_status'),
        need_coordination=data.get('need_coordination', '否'),
        next_plan=data.get('next_plan'),
        planned_time=data.get('planned_time'),
        remarks=data.get('remarks')
    )
    
    db.session.add(new_requirement)
    db.session.commit()
    return jsonify(new_requirement.to_dict()), 201

# 更新需求
@api.route('/requirements/<int:req_id>', methods=['PUT'])
def update_requirement(req_id):
    requirement = RequirementManagement.query.get_or_404(req_id)
    data = request.get_json()
    
    # 更新字段
    requirement.category = data.get('category', requirement.category)
    requirement.section = data.get('section', requirement.section)
    requirement.requirement_name = data.get('requirement_name', requirement.requirement_name)
    requirement.is_connected = data.get('is_connected', requirement.is_connected)
    requirement.department = data.get('department', requirement.department)
    requirement.data_system = data.get('data_system', requirement.data_system)
    requirement.data_name = data.get('data_name', requirement.data_name)
    requirement.data_quality = data.get('data_quality', requirement.data_quality)
    requirement.data_status = data.get('data_status', requirement.data_status)
    requirement.need_coordination = data.get('need_coordination', requirement.need_coordination)
    requirement.next_plan = data.get('next_plan', requirement.next_plan)
    requirement.remarks = data.get('remarks', requirement.remarks)
    
    # 直接使用字符串值，不进行日期转换
    requirement.planned_time = data.get('planned_time', requirement.planned_time)
    
    db.session.commit()
    return jsonify(requirement.to_dict())

# 删除需求
@api.route('/requirements/<int:req_id>', methods=['DELETE'])
def delete_requirement(req_id):
    requirement = RequirementManagement.query.get_or_404(req_id)
    db.session.delete(requirement)
    db.session.commit()
    return jsonify({'message': 'Requirement deleted successfully'}), 204