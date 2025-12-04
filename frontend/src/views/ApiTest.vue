<template>
  <div class="test-container">
    <h1>API测试页面</h1>
    <a-button type="primary" @click="testApi">测试API调用</a-button>
    <div v-if="testData" style="margin-top: 20px;">
      <h2>API调用结果:</h2>
      <pre>{{ JSON.stringify(testData, null, 2) }}</pre>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import requirementApi from '../api/requirement';

export default {
  name: 'ApiTest',
  setup() {
    const testData = ref(null);
    
    const testApi = () => {
      console.log('开始测试API调用...');
      requirementApi.getRequirements()
        .then(response => {
          console.log('API调用成功:', response);
          testData.value = response.data;
        })
        .catch(error => {
          console.error('API调用失败:', error);
          alert('API调用失败，请检查控制台');
        });
    };
    
    return {
      testData,
      testApi
    };
  }
};
</script>

<style scoped>
.test-container {
  padding: 20px;
}
pre {
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
}
</style>