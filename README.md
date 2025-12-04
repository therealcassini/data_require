# Vue3 + Ant Design + Flask + MySQL 开发框架

一个基于 Vue3 + Ant Design + Flask + MySQL 的全栈开发框架，提供了简洁明了的路由跳转和完整的前后端集成方案。

## 技术栈

### 前端
- **Vue 3**：渐进式 JavaScript 框架
- **Ant Design Vue**：企业级 UI 组件库
- **Vue Router**：路由管理
- **Vite**：构建工具
- **Axios**：HTTP 客户端

### 后端
- **Flask**：轻量级 Python Web 框架
- **Flask-SQLAlchemy**：ORM 数据库工具
- **Flask-CORS**：跨域资源共享
- **PyMySQL**：MySQL 数据库驱动
- **python-dotenv**：环境变量管理

### 数据库
- **MySQL**：关系型数据库

## 项目结构

```
data_require/
├── backend/                 # Python 后端项目
│   ├── .env                 # 环境变量配置
│   ├── app.py              # Flask 应用入口
│   ├── models.py           # 数据模型定义
│   ├── routes.py           # API 路由配置
│   └── requirements.txt    # 依赖列表
├── frontend/               # Vue3 前端项目
│   ├── index.html          # HTML 入口文件
│   ├── package.json        # 项目配置和依赖
│   ├── vite.config.js      # Vite 配置
│   └── src/
│       ├── api/            # API 服务
│       ├── components/     # 通用组件
│       ├── router/         # 路由配置
│       ├── views/          # 页面组件
│       ├── App.vue         # 根组件
│       └── main.js         # 应用入口
└── README.md               # 项目说明文档
```

## 快速开始

### 1. 环境准备

- **Python 3.7+**：安装 Python
- **Node.js 14+**：安装 Node.js
- **MySQL 5.7+**：安装 MySQL 数据库

### 2. 后端配置

#### 2.1 安装依赖

```bash
cd backend
pip install -r requirements.txt
```

#### 2.2 配置数据库

1. 创建数据库：
   ```sql
   CREATE DATABASE test_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

2. 修改 `.env` 文件中的数据库配置：
   ```env
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=root
   DB_PASSWORD=your_password
   DB_NAME=test_db
   ```

#### 2.3 启动后端服务

```bash
cd backend
flask run
```

后端服务将在 http://localhost:5000 启动

### 3. 前端配置

#### 3.1 安装依赖

```bash
cd frontend
npm install
```

#### 3.2 启动前端服务

```bash
cd frontend
npm run dev
```

前端服务将在 http://localhost:3000 启动

## 主要功能

### 路由系统

框架提供了简洁明了的路由配置，支持页面快速跳转：

- **首页**：`/` - 框架介绍页面
- **用户管理**：`/users` - 用户增删改查功能
- **关于**：`/about` - 项目说明页面
- **404**：`/*` - 页面不存在时的提示页面

### API 接口

#### 用户接口
- `GET /api/users` - 获取用户列表
- `GET /api/users/{id}` - 获取单个用户
- `POST /api/users` - 创建用户
- `PUT /api/users/{id}` - 更新用户
- `DELETE /api/users/{id}` - 删除用户

#### 测试接口
- `GET /api/hello` - 测试接口

## 使用指南


## 相关建表语句
· `users` 表：用户信息表
  ```sql
  CREATE TABLE `users` (
    `id` int NOT NULL AUTO_INCREMENT,
    `username` varchar(80) COLLATE utf8mb4_bin NOT NULL,
    `email` varchar(120) COLLATE utf8mb4_bin NOT NULL,
    `created_at` datetime DEFAULT NULL,
    `password` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `username` (`username`),
    UNIQUE KEY `email` (`email`)
  ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
  ```

· `requirement_management` 表：需求对接管理表
  ```sql
  CREATE TABLE `requirement_management` ( 
   `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID', 
   `category` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL COMMENT '大类', 
   `section` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL COMMENT '版块', 
   `requirement_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL COMMENT '需求名目', 
   `is_connected` varchar(200) COLLATE utf8mb4_bin DEFAULT '0' COMMENT '是否已对接（0:否 1:是）', 
   `department` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '对接部门', 
   `data_system` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '对接数据系统', 
   `data_name` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '对接数据名称', 
   `data_quality` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '已对接数据质量（优/良/中/差）', 
   `data_status` text COLLATE utf8mb4_bin COMMENT '已对接数据情况', 
   `need_coordination` varchar(100) COLLATE utf8mb4_bin DEFAULT '0' COMMENT '是否需要业主协调（0:否 1:是）', 
   `next_plan` text COLLATE utf8mb4_bin COMMENT '下一步计划', 
   `planned_time` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '计划对接时间', 
   `remarks` text COLLATE utf8mb4_bin COMMENT '备注', 
   `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间', 
   `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间', 
   PRIMARY KEY (`id`) 
 ) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='需求对接管理表'
  ```

### 添加新页面

1. 在 `src/views/` 目录下创建新的 Vue 组件
2. 在 `src/router/index.js` 中添加路由配置
3. 在 `src/App.vue` 的菜单中添加导航链接

### 开发新 API

1. 在 `backend/models.py` 中定义数据模型
2. 在 `backend/routes.py` 中添加 API 路由
3. 在 `frontend/src/api/` 目录下创建对应的 API 服务
4. 在前端组件中调用 API 服务

## 构建和部署

### 前端构建

```bash
cd frontend
npm run build
```

构建后的文件将输出到 `dist` 目录

### 后端部署

可以使用以下方式部署后端服务：

- 使用 Gunicorn：
  ```bash
  cd backend
  gunicorn -w 4 -b 0.0.0.0:5000 app:app
  ```

- 使用 Docker：
  创建 Dockerfile 文件并构建镜像

## 注意事项

1. 确保 MySQL 数据库已正确安装和配置
2. 开发环境中使用的依赖版本可能需要根据实际情况调整
3. 生产环境中建议关闭调试模式并配置安全相关设置
4. 前后端服务需要同时运行才能正常工作

## License

MIT