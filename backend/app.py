from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 创建 Flask 应用
app = Flask(__name__)

# 配置 CORS
CORS(app, resources={"/*": {"origins": "*"}})

# 配置数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 导入数据库实例
from extensions import db
# 初始化数据库
db.init_app(app)

# 导入模型
from models import *
# 导入路由蓝图
from routes import api

# 注册蓝图
app.register_blueprint(api, url_prefix='/api')

# 创建数据库表 - 注释掉以避免与现有表冲突
# with app.app_context():
#     db.create_all()

# 测试路由
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Flask backend!'})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('FLASK_RUN_PORT'))