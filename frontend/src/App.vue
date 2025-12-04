<template>
  <div class="app-container">
    <a-layout>
      <a-layout-header class="header">
        <div class="logo">Vue3 + Ant Design</div>
        <a-menu
          mode="horizontal"
          :default-selected-keys="[activeMenu]"
          :style="{ lineHeight: '64px', flex: 1 }"
          theme="dark"
        >
          <a-menu-item key="home">
            <router-link to="/">首页</router-link>
          </a-menu-item>
          <a-menu-item key="users">
            <router-link to="/users">用户管理</router-link>
          </a-menu-item>
          <a-menu-item key="requirements">
            <router-link to="/requirements">需求管理</router-link>
          </a-menu-item>
          <a-menu-item key="about">
            <router-link to="/about">关于</router-link>
          </a-menu-item>
        </a-menu>
        
        <!-- 用户信息和登出按钮 -->
        <div class="user-info" v-if="currentUser">
          <a-dropdown>
            <a class="ant-dropdown-link" href="#">
              <span>{{ currentUser.username }}</span>
              <a-icon type="down" />
            </a>
            <template #overlay>
              <a-menu>
                <a-menu-item @click="handleLogout">
                  <a-icon type="logout" /> 登出
                </a-menu-item>
              </a-menu>
            </template>
          </a-dropdown>
        </div>
      </a-layout-header>
      <a-layout-content style="padding: 0 50px; margin-top: 24px; min-height: calc(100vh - 160px);">
        <a-card>
          <router-view></router-view>
        </a-card>
      </a-layout-content>
      <a-layout-footer style="text-align: center;">
        Vue3 + Ant Design + Flask + MySQL 开发框架 ©2024
      </a-layout-footer>
    </a-layout>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { message } from 'ant-design-vue';

const router = useRouter();
const route = useRoute();
const currentUser = ref(null);

// 获取当前激活的菜单
const activeMenu = computed(() => {
  const path = route.path;
  if (path === '/') return 'home';
  if (path === '/users') return 'users';
  if (path === '/requirements') return 'requirements';
  if (path === '/about') return 'about';
  return 'home';
});

// 初始化用户信息
onMounted(() => {
  const userStr = localStorage.getItem('user');
  if (userStr) {
    currentUser.value = JSON.parse(userStr);
  }
});

// 登出处理
const handleLogout = () => {
  // 清除localStorage中的登录状态
  localStorage.removeItem('user');
  localStorage.removeItem('token');
  currentUser.value = null;
  
  message.success('登出成功');
  router.push('/login');
};
</script>

<style>
.app-container {
  min-height: 100vh;
}

.header {
  background: #001529;
  padding: 0 24px;
  display: flex;
  align-items: center;
}

.logo {
  float: left;
  width: 120px;
  height: 31px;
  margin: 16px 24px 16px 0;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
}

.user-info {
  display: flex;
  align-items: center;
  color: white;
  margin-left: auto;
  padding: 0 16px;
}

.user-info a {
  color: white;
  text-decoration: none;
}
</style>