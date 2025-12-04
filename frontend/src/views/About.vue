<template>
  <div class="about">
    <a-page-header
      class="site-page-header"
      title="关于我们"
      sub-title="Vue3 + Ant Design + Flask + MySQL 开发框架"
    />
    <a-card>
      <div class="about-content">
        <h2>框架介绍</h2>
        <p>这是一个基于 Vue3 + Ant Design + Flask + MySQL 的全栈开发框架，提供了简洁明了的路由跳转和完整的前后端集成方案。</p>
        
        <h3>技术栈</h3>
        <a-descriptions bordered :column="2">
          <a-descriptions-item label="前端框架">Vue 3</a-descriptions-item>
          <a-descriptions-item label="UI组件库">Ant Design Vue</a-descriptions-item>
          <a-descriptions-item label="构建工具">Vite</a-descriptions-item>
          <a-descriptions-item label="路由管理">Vue Router</a-descriptions-item>
          <a-descriptions-item label="后端框架">Flask</a-descriptions-item>
          <a-descriptions-item label="数据库">MySQL</a-descriptions-item>
          <a-descriptions-item label="ORM">SQLAlchemy</a-descriptions-item>
          <a-descriptions-item label="API设计">RESTful API</a-descriptions-item>
        </a-descriptions>
        
        <h3>主要特性</h3>
        <a-list :bordered="true">
          <a-list-item>简洁明了的路由配置，支持页面快速跳转</a-list-item>
          <a-list-item>完整的用户管理功能，包括增删改查</a-list-item>
          <a-list-item>响应式设计，适配各种屏幕尺寸</a-list-item>
          <a-list-item>前后端分离架构，便于团队协作开发</a-list-item>
          <a-list-item>内置API代理，解决跨域问题</a-list-item>
        </a-list>
      </div>
    </a-card>
  </div>
</template>

<script>
export default {
  name: 'About'
}
</script>

<style scoped>
.about {
  padding: 24px 0;
}

.about-content {
  padding: 24px;
}

h2 {
  margin-bottom: 16px;
  color: rgba(0, 0, 0, 0.85);
  font-size: 20px;
  font-weight: 600;
}

h3 {
  margin-top: 24px;
  margin-bottom: 16px;
  color: rgba(0, 0, 0, 0.85);
  font-size: 16px;
  font-weight: 600;
}

p {
  margin-bottom: 16px;
  line-height: 1.6;
}
</style>