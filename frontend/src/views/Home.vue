<template>
  <div class="home">
    <a-page-header
      class="site-page-header"
      title="欢迎使用"
      sub-title="Vue3 + Ant Design + Flask + MySQL 开发框架"
    />
    <div class="home-content">
      <a-row :gutter="[16, 16]">
        <a-col :xs="24" :sm="12" :md="8">
          <a-card hoverable :bordered="false">
            <template #cover>
              <img alt="Vue3" src="https://vuejs.org/images/logo.png" style="height: 120px; object-fit: contain;" />
            </template>
            <a-card-meta title="Vue3" description="渐进式 JavaScript 框架" />
          </a-card>
        </a-col>
        <a-col :xs="24" :sm="12" :md="8">
          <a-card hoverable :bordered="false">
            <template #cover>
              <img alt="Ant Design" src="https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg" style="height: 120px; object-fit: contain;" />
            </template>
            <a-card-meta title="Ant Design" description="企业级 UI 设计语言" />
          </a-card>
        </a-col>
        <a-col :xs="24" :sm="12" :md="8">
          <a-card hoverable :bordered="false">
            <template #cover>
              <img alt="Flask" src="https://flask.palletsprojects.com/en/3.0.x/_static/flask.png" style="height: 120px; object-fit: contain;" />
            </template>
            <a-card-meta title="Flask" description="轻量级 Python Web 框架" />
          </a-card>
        </a-col>
      </a-row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.home {
  padding: 24px 0;
}

.home-content {
  margin-top: 24px;
}
</style>