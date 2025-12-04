<template>
  <div class="login-container">
    <div class="login-form-wrapper">
      <h2 class="login-title">需求管理系统</h2>
      <a-form :model="loginForm" :rules="loginRules" ref="loginFormRef" class="login-form">
        <a-form-item name="username" label="用户名">
          <a-input v-model:value="loginForm.username" placeholder="请输入用户名" />
        </a-form-item>
        <a-form-item name="password" label="密码">
          <a-input-password v-model:value="loginForm.password" placeholder="请输入密码" />
        </a-form-item>
        <a-form-item>
          <a-button type="primary" @click="handleLogin" :loading="loading" block>
            登录
          </a-button>
        </a-form-item>
      </a-form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';
import { message } from 'ant-design-vue';
import axios from 'axios';

const router = useRouter();
const loginFormRef = ref();
const loading = ref(false);

const loginForm = reactive({
  username: '',
  password: ''
});

const loginRules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' }
  ]
};

const handleLogin = async () => {
  if (!loginFormRef.value) return;
  
  try {
    await loginFormRef.value.validate();
    loading.value = true;
    
    const response = await axios.post('http://localhost:5000/api/login', {
      username: loginForm.username,
      password: loginForm.password
    });
    
    // 保存用户信息到localStorage
    localStorage.setItem('user', JSON.stringify(response.data.user));
    localStorage.setItem('token', 'logged_in'); // 简单的登录状态标识
    
    message.success('登录成功');
    router.push('/');
  } catch (error) {
    if (error.response) {
      message.error(error.response.data.message || '登录失败');
    } else {
      message.error('网络错误，请稍后重试');
    }
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f2f5;
}

.login-form-wrapper {
  width: 400px;
  padding: 24px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.login-title {
  text-align: center;
  margin-bottom: 24px;
  color: #1890ff;
}

.login-form {
  margin-top: 24px;
}
</style>