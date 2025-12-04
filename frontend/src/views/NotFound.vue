<template>
  <div class="not-found">
    <div class="not-found-content">
      <a-result
        status="404"
        title="404"
        sub-title="抱歉，您访问的页面不存在"
      >
        <template #extra>
          <a-button type="primary" @click="goHome">
            <template #icon>
              <HomeOutlined />
            </template>
            返回首页
          </a-button>
        </template>
      </a-result>
    </div>
  </div>
</template>

<script>
import { HomeOutlined } from '@ant-design/icons-vue'
import { useRouter } from 'vue-router'

export default {
  name: 'NotFound',
  components: {
    HomeOutlined
  },
  setup() {
    const router = useRouter()
    
    const goHome = () => {
      router.push('/')
    }
    
    return {
      goHome
    }
  }
}
</script>

<style scoped>
.not-found {
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.not-found-content {
  width: 100%;
  max-width: 600px;
}
</style>