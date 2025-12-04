import axios from 'axios'

// 创建 axios 实例
const api = axios.create({
  baseURL: '/api',
  timeout: 5000
})

// 获取用户列表
export const getUserList = () => {
  return api.get('/users')
}

// 获取单个用户
export const getUser = (id) => {
  return api.get(`/users/${id}`)
}

// 创建用户
export const createUser = (data) => {
  return api.post('/users', data)
}

// 更新用户
export const updateUser = (id, data) => {
  return api.put(`/users/${id}`, data)
}

// 删除用户
export const deleteUser = (id) => {
  return api.delete(`/users/${id}`)
}