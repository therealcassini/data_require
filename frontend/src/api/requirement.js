import axios from 'axios';

const apiClient = axios.create({
  baseURL: '/api', // 与vite.config.js中的代理配置一致
  headers: {
    'Content-Type': 'application/json'
  }
});

// 需求管理API服务
export default {
  // 获取所有需求
  getRequirements() {
    return apiClient.get('/requirements');
  },

  // 获取单个需求
  getRequirement(id) {
    return apiClient.get(`/requirements/${id}`);
  },

  // 创建需求
  createRequirement(requirement) {
    return apiClient.post('/requirements', requirement);
  },

  // 更新需求
  updateRequirement(id, requirement) {
    return apiClient.put(`/requirements/${id}`, requirement);
  },

  // 删除需求
  deleteRequirement(id) {
    return apiClient.delete(`/requirements/${id}`);
  }
};