# ARoute API 文档

## 目录
- [简介](#简介)
- [用户相关API](#用户相关api)
- [文章相关API](#文章相关api)
- [自定义页面相关API](#自定义页面相关api)
- [标签相关API](#标签相关api)
- [分类相关API](#分类相关api)
- [系统信息相关API](#系统信息相关api)
- [JWT Token 相关](#jwt-token-相关)

## 简介
ARoute 是一个基于Django和Django REST framework构建的API项目，提供了对用户、文章、自定义页面、标签、分类和系统信息的管理功能。

## 用户相关API

### 注册用户
- **URL:** `/api/register/`
- **方法:** `POST`
- **参数:**
  - `username` (string): 用户名
  - `password` (string): 密码
  - `password2` (string): 确认密码
  - `email` (string): 邮箱
  - `is_staff` (boolean, 可选): 是否为管理员，默认为False
  - `profile_picture` (file, 可选): 用户头像

### 更新用户信息
- **URL:** `/api/update-profile/`
- **方法:** `PUT`
- **参数:**
  - `username` (string): 用户名
  - `email` (string): 邮箱
  - `profile_picture` (file, 可选): 用户头像

### 登录
- **URL:** `/api/login/`
- **方法:** `POST`
- **参数:**
  - `username` (string): 用户名
  - `password` (string): 密码

### 获取当前登录用户信息
- **URL:** `/api/user-info/`
- **方法:** `GET`

### 获取特定用户信息
- **URL:** `/api/users/<int:pk>/`
- **方法:** `GET`

### 删除用户
- **URL:** `/api/delete-user/<int:pk>/`
- **方法:** `DELETE`

### 获取所有用户列表
- **URL:** `/api/users/`
- **方法:** `GET`

## 文章相关API

### 创建文章
- **URL:** `/api/create-article/`
- **方法:** `POST`
- **参数:**
  - `title` (string): 标题
  - `content` (string): 内容
  - `cover` (file, 可选): 封面图片

### 获取所有文章
- **URL:** `/api/articles/`
- **方法:** `GET`

### 获取单篇文章
- **URL:** `/api/article/<int:pk>/`
- **方法:** `GET`

### 更新文章
- **URL:** `/api/update-article/<int:pk>/`
- **方法:** `PUT`
- **参数:**
  - `title` (string): 标题
  - `content` (string): 内容
  - `cover` (file, 可选): 封面图片

### 删除文章
- **URL:** `/api/delete-article/<int:pk>/`
- **方法:** `DELETE`

## 自定义页面相关API

### 创建自定义页面
- **URL:** `/api/create-custom-page/`
- **方法:** `POST`
- **参数:**
  - `title` (string): 标题
  - `content` (string): 内容
  - `slug` (string): 页面标识符

### 获取所有自定义页面
- **URL:** `/api/custom-pages/`
- **方法:** `GET`

### 获取单个自定义页面
- **URL:** `/api/custom-page/<int:pk>/`
- **方法:** `GET`

### 更新自定义页面
- **URL:** `/api/update-custom-page/<int:pk>/`
- **方法:** `PUT`
- **参数:**
  - `title` (string): 标题
  - `content` (string): 内容
  - `slug` (string): 页面标识符

### 删除自定义页面
- **URL:** `/api/delete-custom-page/<int:pk>/`
- **方法:** `DELETE`

## 标签相关API

### 创建标签
- **URL:** `/api/create-tag/`
- **方法:** `POST`
- **参数:**
  - `name` (string): 标签名

### 获取所有标签
- **URL:** `/api/tags/`
- **方法:** `GET`

### 获取单个标签
- **URL:** `/api/tag/<int:pk>/`
- **方法:** `GET`

### 更新标签
- **URL:** `/api/update-tag/<int:pk>/`
- **方法:** `PUT`
- **参数:**
  - `name` (string): 标签名

### 删除标签
- **URL:** `/api/delete-tag/<int:pk>/`
- **方法:** `DELETE`

## 分类相关API

### 创建分类
- **URL:** `/api/create-category/`
- **方法:** `POST`
- **参数:**
  - `name` (string): 分类名
  - `description` (string, 可选): 描述

### 获取所有分类
- **URL:** `/api/categories/`
- **方法:** `GET`

### 获取单个分类
- **URL:** `/api/category/<int:pk>/`
- **方法:** `GET`

### 更新分类
- **URL:** `/api/update-category/<int:pk>/`
- **方法:** `PUT`
- **参数:**
  - `name` (string): 分类名
  - `description` (string, 可选): 描述

### 删除分类
- **URL:** `/api/delete-category/<int:pk>/`
- **方法:** `DELETE`

## 系统信息相关API

### 创建系统信息
- **URL:** `/api/system-info/create/`
- **方法:** `POST`
- **参数:**
  - `name` (string): 名称
  - `description` (string, 可选): 描述
  - `seo_title` (string, 可选): SEO标题
  - `seo_description` (string, 可选): SEO描述
  - `seo_keywords` (string, 可选): SEO关键词

### 更新系统信息
- **URL:** `/api/system-info/<int:pk>/update/`
- **方法:** `PUT`
- **参数:**
  - `name` (string): 名称
  - `description` (string, 可选): 描述
  - `seo_title` (string, 可选): SEO标题
  - `seo_description` (string, 可选): SEO描述
  - `seo_keywords` (string, 可选): SEO关键词

## JWT Token 相关

### 刷新Token
- **URL:** `/api/token/refresh/`
- **方法:** `POST`
- **参数:**
  - `refresh` (string): 刷新Token

### 登出
- **URL:** `/api/logout/`
- **方法:** `POST`

### 重置密码
- **URL:** `/api/password_reset/`
- **方法:** `POST`
- **参数:**
  - `email` (string): 用户邮箱

### 重置密码确认
- **URL:** `/api/reset/<uidb64>/<token>/`
- **方法:** `POST`
- **参数:**
  - `new_password1` (string): 新密码
  - `new_password2` (string): 确认新密码

### 重置密码完成
- **URL:** `/api/reset/done/`
- **方法:** `GET`
- **描述:** `用户成功重置密码后，显示一个确认页面，告知用户密码已成功更新。`

## 安装与配置

### 环境依赖
确保你已经安装了以下依赖：
- Python 3.8+
- Django 5.1.4
- djangorestframework
- django-rest-framework-simplejwt
- drf-yasg
- Pillow (用于处理图片)

可以通过以下命令安装依赖：

```bash
pip install -r requirements.txt
```

### 数据库配置
默认使用 SQLite 数据库。如果你需要使用其他数据库，请修改 `ARoute/settings.py` 中的 `DATABASES` 配置。

### 启动项目
1. 进入项目根目录：
```bash
cd ARoute
```
2. 应用迁移：
```bash
python manage.py migrate
```
3. 启动开发服务器：
```bash
python manage.py runserver
```
访问 [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) 查看 API 文档。

## API 使用示例

### 注册用户
#### 请求
```bash
POST /api/register/ 
Content-Type: application/json

{ "username": "testuser", 
  "password": "password123", 
  "password2": "password123", 
  "email": "test@example.com" 
}
```
#### 响应
```json
{ 
"user": { 
"username": "testuser", 
"email": "test@example.com", 
"is_staff": false 
}, 
"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..." 
}
```
### 获取所有文章
#### 请求
```bash
GET /api/articles/
Authorization: Bearer <token>
```
#### 响应
```json
[
{ 
"id": 1, 
"title": "Sample Article", 
"content": "This is a sample article.", 
"cover": "http://127.0.0.1:8000/media/covers/sample.jpg", 
"author": 1, 
"created_at": "2023-10-01T12:00:00Z", 
"updated_at": "2023-10-01T12:00:00Z" }
]
```
## 错误处理

### 常见错误码

| 错误码 | 含义 | 解决方案 |
|-------|------|----------|
| 400   | 请求无效 | 检查请求参数是否正确 |
| 401   | 未授权 | 检查 Token 是否有效 |
| 403   | 禁止访问 | 用户权限不足 |
| 404   | 资源未找到 | 检查 URL 是否正确 |
| 500   | 内部服务器错误 | 检查服务器日志 |

### 调试建议
- 使用 Postman 或 cURL 测试 API 请求。
- 查看 Django 的日志文件以获取更多信息。

## 贡献指南

欢迎贡献代码！请遵循以下步骤：
1. Fork 仓库。
2. 创建一个新的分支 (`git checkout -b feature-branch`)。
3. 提交你的更改 (`git commit -m 'Add some feature'`)。
4. 推送到远程分支 (`git push origin feature-branch`)。
5. 创建 Pull Request。

请确保在提交之前运行测试并保持代码风格一致。

## 许可证

本项目采用 [GPL-3.0](LICENSE) 许可证。
