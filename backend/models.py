from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    password = db.Column(db.String(100), nullable=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class RequirementManagement(db.Model):
    __tablename__ = 'requirement_management'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键ID')
    category = db.Column(db.String(50), nullable=False, comment='大类')
    section = db.Column(db.String(50), nullable=False, comment='版块')
    requirement_name = db.Column(db.String(100), nullable=False, comment='需求名目')
    is_connected = db.Column(db.String(200), default='否', comment='是否已对接')
    department = db.Column(db.String(50), nullable=True, comment='对接部门')
    data_system = db.Column(db.String(50), nullable=True, comment='对接数据系统')
    data_name = db.Column(db.String(100), nullable=True, comment='对接数据名称')
    data_quality = db.Column(db.String(20), nullable=True, comment='已对接数据质量（优/良/中/差）')
    data_status = db.Column(db.Text, nullable=True, comment='已对接数据情况')
    need_coordination = db.Column(db.String(100), default='否', comment='是否需要业主协调')
    next_plan = db.Column(db.Text, nullable=True, comment='下一步计划')
    planned_time = db.Column(db.String(20), nullable=True, comment='计划对接时间')
    remarks = db.Column(db.Text, nullable=True, comment='备注')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    
    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'section': self.section,
            'requirement_name': self.requirement_name,
            'is_connected': self.is_connected,
            'department': self.department,
            'data_system': self.data_system,
            'data_name': self.data_name,
            'data_quality': self.data_quality,
            'data_status': self.data_status,
            'need_coordination': self.need_coordination,
            'next_plan': self.next_plan,
            'planned_time': self.planned_time if self.planned_time is not None else None,
            'remarks': self.remarks,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time is not None else None,
            'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S') if self.update_time is not None else None
        }