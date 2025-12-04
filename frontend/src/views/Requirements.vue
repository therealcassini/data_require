<template>
  <div class="requirements-container">
    <h2>需求管理</h2>
    
    <!-- 查询条件区域 -->
    <div class="search-container" style="margin-bottom: 16px; padding: 16px; background-color: #f5f5f5; border-radius: 4px;">
      <a-row :gutter="16">
        <a-col :span="5">
          <a-form-item label="大类">
            <a-select v-model:value="searchParams.category" placeholder="请选择大类">
              <a-select-option v-for="item in options.categories" :key="item" :value="item">
                {{ item }}
              </a-select-option>
            </a-select>
          </a-form-item>
        </a-col>
        <a-col :span="5">
          <a-form-item label="版块">
            <a-select v-model:value="searchParams.section" placeholder="请选择版块">
              <a-select-option v-for="item in options.sections" :key="item" :value="item">
                {{ item }}
              </a-select-option>
            </a-select>
          </a-form-item>
        </a-col>
        <a-col :span="5">
          <a-form-item label="是否已对接">
            <a-select v-model:value="searchParams.is_connected" placeholder="请选择是否已对接">
              <a-select-option v-for="item in options.is_connected_list" :key="item.value" :value="item.value">
                {{ item.label }}
              </a-select-option>
            </a-select>
          </a-form-item>
        </a-col>
        <a-col :span="5">
          <a-form-item label="对接部门">
            <a-select v-model:value="searchParams.department" placeholder="请选择对接部门">
              <a-select-option v-for="item in options.departments" :key="item" :value="item">
                {{ item }}
              </a-select-option>
            </a-select>
          </a-form-item>
        </a-col>
        <a-col :span="4">
          <a-form-item label="需求名目">
            <a-input v-model:value="searchParams.requirement_name" placeholder="请输入需求名目" />
          </a-form-item>
        </a-col>
      </a-row>
      <a-row :gutter="16" style="margin-top: 16px;">
        <a-col :span="5">
          <a-form-item label="计划对接时间">
            <a-select v-model:value="searchParams.planned_time" placeholder="请选择计划对接时间">
              <a-select-option v-for="item in options.planned_time_list" :key="item" :value="item">
                {{ item }}
              </a-select-option>
            </a-select>
          </a-form-item>
        </a-col>
      </a-row>
      <a-row style="margin-top: 8px;">
        <a-col :span="24" style="text-align: right;">
          <a-button type="primary" @click="handleSearch">查询</a-button>
          <a-button @click="resetSearch">重置</a-button>
        </a-col>
      </a-row>
    </div>
    
    <a-button type="primary" @click="showAddModal" style="margin-bottom: 16px;">
      <a-icon type="plus" /> 添加需求
    </a-button>
    
    <!-- 需求列表 -->
    <a-table
      :columns="columns"
      :data-source="requirements"
      :pagination="{ pageSize: 10 }"
      row-key="id"
      bordered
    >
      <template #action="{ record }">
        <a-button type="link" @click="showEditModal(record)">
          编辑
        </a-button>
        <a-button type="link" danger @click="handleDelete(record.id)">
          删除
        </a-button>
      </template>
      
      <template #is_connected="{ record }">
        <a-tag :color="record.is_connected === '是' ? 'green' : 'red'">
          {{ record.is_connected === '是' ? '已对接' : '未对接' }}
        </a-tag>
      </template>
      
      <template #need_coordination="{ record }">
        <a-tag :color="record.need_coordination === '是' ? 'red' : 'green'">
          {{ record.need_coordination === '是' ? '需要' : '不需要' }}
        </a-tag>
      </template>
    </a-table>
    
    <!-- 添加需求模态框 -->
    <a-modal
      title="添加需求"
      v-model:visible="addModalVisible"
      @ok="handleAddOk"
      @cancel="handleAddCancel"
    >
      <a-form :model="newRequirement" :rules="rules" ref="addFormRef">
        <a-form-item label="大类" name="category">
          <a-input v-model:value="newRequirement.category" placeholder="请输入大类" />
        </a-form-item>
        <a-form-item label="版块" name="section">
          <a-input v-model:value="newRequirement.section" placeholder="请输入版块" />
        </a-form-item>
        <a-form-item label="需求名目" name="requirement_name">
          <a-input v-model:value="newRequirement.requirement_name" placeholder="请输入需求名目" />
        </a-form-item>
        <a-form-item label="是否已对接">
          <a-radio-group v-model:value="newRequirement.is_connected">
            <a-radio value="否">未对接</a-radio>
            <a-radio value="是">已对接</a-radio>
          </a-radio-group>
        </a-form-item>
        <a-form-item label="对接部门">
          <a-input v-model:value="newRequirement.department" placeholder="请输入对接部门" />
        </a-form-item>
        <a-form-item label="对接数据系统">
          <a-input v-model:value="newRequirement.data_system" placeholder="请输入对接数据系统" />
        </a-form-item>
        <a-form-item label="对接数据名称">
          <a-input v-model:value="newRequirement.data_name" placeholder="请输入对接数据名称" />
        </a-form-item>
        <a-form-item label="已对接数据质量">
          <a-select v-model:value="newRequirement.data_quality" placeholder="请选择数据质量">
            <a-select-option value="优">优</a-select-option>
            <a-select-option value="良">良</a-select-option>
            <a-select-option value="中">中</a-select-option>
            <a-select-option value="差">差</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="已对接数据情况">
          <a-textarea v-model:value="newRequirement.data_status" placeholder="请输入已对接数据情况" :rows="3" />
        </a-form-item>
        <a-form-item label="是否需要业主协调">
          <a-radio-group v-model:value="newRequirement.need_coordination">
            <a-radio value="否">不需要</a-radio>
            <a-radio value="是">需要</a-radio>
          </a-radio-group>
        </a-form-item>
        <a-form-item label="下一步计划">
          <a-textarea v-model:value="newRequirement.next_plan" placeholder="请输入下一步计划" :rows="3" />
        </a-form-item>
        <a-form-item label="计划对接时间">
          <a-input v-model:value="newRequirement.planned_time" placeholder="请输入计划对接时间" style="width: 100%;" />
        </a-form-item>
        <a-form-item label="备注">
          <a-textarea v-model:value="newRequirement.remarks" placeholder="请输入备注" :rows="3" />
        </a-form-item>
      </a-form>
    </a-modal>
    
    <!-- 编辑需求模态框 -->
    <a-modal
      title="编辑需求"
      v-model:visible="editModalVisible"
      @ok="handleEditOk"
      @cancel="handleEditCancel"
    >
      <a-form :model="editingRequirement" :rules="rules" ref="editFormRef">
        <a-form-item label="大类" name="category">
          <a-input v-model:value="editingRequirement.category" placeholder="请输入大类" />
        </a-form-item>
        <a-form-item label="版块" name="section">
          <a-input v-model:value="editingRequirement.section" placeholder="请输入版块" />
        </a-form-item>
        <a-form-item label="需求名目" name="requirement_name">
          <a-input v-model:value="editingRequirement.requirement_name" placeholder="请输入需求名目" />
        </a-form-item>
        <a-form-item label="是否已对接">
          <a-radio-group v-model:value="editingRequirement.is_connected">
            <a-radio value="否">未对接</a-radio>
            <a-radio value="是">已对接</a-radio>
          </a-radio-group>
        </a-form-item>
        <a-form-item label="对接部门">
          <a-input v-model:value="editingRequirement.department" placeholder="请输入对接部门" />
        </a-form-item>
        <a-form-item label="对接数据系统">
          <a-input v-model:value="editingRequirement.data_system" placeholder="请输入对接数据系统" />
        </a-form-item>
        <a-form-item label="对接数据名称">
          <a-input v-model:value="editingRequirement.data_name" placeholder="请输入对接数据名称" />
        </a-form-item>
        <a-form-item label="已对接数据质量">
          <a-select v-model:value="editingRequirement.data_quality" placeholder="请选择数据质量">
            <a-select-option value="优">优</a-select-option>
            <a-select-option value="良">良</a-select-option>
            <a-select-option value="中">中</a-select-option>
            <a-select-option value="差">差</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="已对接数据情况">
          <a-textarea v-model:value="editingRequirement.data_status" placeholder="请输入已对接数据情况" :rows="3" />
        </a-form-item>
        <a-form-item label="是否需要业主协调">
          <a-radio-group v-model:value="editingRequirement.need_coordination">
            <a-radio value="否">不需要</a-radio>
            <a-radio value="是">需要</a-radio>
          </a-radio-group>
        </a-form-item>
        <a-form-item label="下一步计划">
          <a-textarea v-model:value="editingRequirement.next_plan" placeholder="请输入下一步计划" :rows="3" />
        </a-form-item>
        <a-form-item label="计划对接时间">
          <a-input v-model:value="editingRequirement.planned_time" placeholder="请输入计划对接时间" style="width: 100%;" />
        </a-form-item>
        <a-form-item label="备注">
          <a-textarea v-model:value="editingRequirement.remarks" placeholder="请输入备注" :rows="3" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue';
import requirementApi from '../api/requirement';
import { message } from 'ant-design-vue';
import axios from 'axios';

export default {
  name: 'Requirements',
  setup() {
    // 需求列表数据
    const requirements = ref([]);
    
    // 筛选选项
    const options = reactive({
      categories: [],
      sections: [],
      is_connected_list: [],
      departments: [],
      planned_time_list: []
    });
    
    // 查询参数
    const searchParams = reactive({
      category: null,
      section: null,
      is_connected: null,
      department: null,
      requirement_name: '',
      planned_time: null
    });
    
    // 添加需求模态框相关
    const addModalVisible = ref(false);
    const newRequirement = reactive({
      category: '',
      section: '',
      requirement_name: '',
      is_connected: '否',
      department: '',
      data_system: '',
      data_name: '',
      data_quality: '',
      data_status: '',
      need_coordination: '否',
      next_plan: '',
      planned_time: '',
      remarks: ''
    });
    const addFormRef = ref(null);
    
    // 编辑需求模态框相关
    const editModalVisible = ref(false);
    const editingRequirement = reactive({
      id: null,
      category: '',
      section: '',
      requirement_name: '',
      is_connected: '否',
      department: '',
      data_system: '',
      data_name: '',
      data_quality: '',
      data_status: '',
      need_coordination: '否',
      next_plan: '',
      planned_time: '',
      remarks: ''
    });
    const editFormRef = ref(null);
    
    // 表单验证规则
    const rules = {
      category: [{ required: true, message: '请输入大类', trigger: 'blur' }],
      section: [{ required: true, message: '请输入版块', trigger: 'blur' }],
      requirement_name: [{ required: true, message: '请输入需求名目', trigger: 'blur' }]
    };
    
    // 表格列配置
    const columns = [
      { title: '大类', dataIndex: 'category', key: 'category' },
      { title: '版块', dataIndex: 'section', key: 'section' },
      { title: '需求名目', dataIndex: 'requirement_name', key: 'requirement_name' },
      { title: '是否已对接', dataIndex: 'is_connected', key: 'is_connected', slots: { customRender: 'is_connected' } },
      { title: '对接部门', dataIndex: 'department', key: 'department' },
      { title: '对接数据系统', dataIndex: 'data_system', key: 'data_system' },
      { title: '对接数据名称', dataIndex: 'data_name', key: 'data_name' },
      { title: '已对接数据质量', dataIndex: 'data_quality', key: 'data_quality' },
      { title: '是否需要业主协调', dataIndex: 'need_coordination', key: 'need_coordination', slots: { customRender: 'need_coordination' } },
      { title: '计划对接时间', dataIndex: 'planned_time', key: 'planned_time' },
      { title: '操作', key: 'action', slots: { customRender: 'action' } }
    ];
    
    // 获取下拉选项值
    const fetchOptions = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/requirements/options');
        Object.assign(options, response.data);
      } catch (error) {
        console.error('获取下拉选项值失败:', error);
        message.error('获取下拉选项值失败');
      }
    };
    
    // 获取所有需求（支持过滤和搜索）
    const fetchRequirements = async () => {
      try {
        // 构建查询参数
        const params = {};
        if (searchParams.category) params.category = searchParams.category;
        if (searchParams.section) params.section = searchParams.section;
        if (searchParams.is_connected !== null) params.is_connected = searchParams.is_connected;
        if (searchParams.department) params.department = searchParams.department;
        if (searchParams.requirement_name) params.requirement_name = searchParams.requirement_name;
        if (searchParams.planned_time) params.planned_time = searchParams.planned_time;
        
        const response = await axios.get('http://localhost:5000/api/requirements', { params });
        requirements.value = response.data;
      } catch (error) {
        console.error('获取需求列表失败:', error);
        message.error('获取需求列表失败');
      }
    };
    
    // 处理查询
    const handleSearch = () => {
      fetchRequirements();
    };
    
    // 重置查询条件
    const resetSearch = () => {
      searchParams.category = null;
      searchParams.section = null;
      searchParams.is_connected = null;
      searchParams.department = null;
      searchParams.requirement_name = '';
      searchParams.planned_time = null;
      fetchRequirements();
    };
    
    // 页面挂载时获取下拉选项和需求列表
    fetchOptions();
    fetchRequirements();
    
    // 显示添加模态框
    const showAddModal = () => {
      addModalVisible.value = true;
    };
    
    // 处理添加确认
    const handleAddOk = () => {
      addFormRef.value.validate().then(() => {
        // 直接使用 newRequirement 对象，因为 a-date-picker 已经返回了 YYYY-MM-DD 格式的字符串
        const requirementData = { ...newRequirement };
        
        requirementApi.createRequirement(requirementData)
          .then(() => {
            message.success('添加需求成功');
            addModalVisible.value = false;
            fetchRequirements();
            resetAddForm();
          })
          .catch(error => {
            message.error('添加需求失败');
            console.error('Error creating requirement:', error);
          });
      }).catch(() => {});
    };
    
    // 处理添加取消
    const handleAddCancel = () => {
      addModalVisible.value = false;
      resetAddForm();
    };
    
    // 重置添加表单
    const resetAddForm = () => {
      newRequirement.category = '';
      newRequirement.section = '';
      newRequirement.requirement_name = '';
      newRequirement.is_connected = '否';
      newRequirement.department = '';
      newRequirement.data_system = '';
      newRequirement.data_name = '';
      newRequirement.data_quality = '';
      newRequirement.data_status = '';
      newRequirement.need_coordination = '否';
      newRequirement.next_plan = '';
      newRequirement.planned_time = '';
      newRequirement.remarks = '';
    };
    
    // 显示编辑模态框
    const showEditModal = (record) => {
      Object.assign(editingRequirement, record);
      // 直接使用后端返回的日期字符串，不转换为 Date 对象
      // 因为 Ant Design Vue 的日期组件可以直接处理 ISO 格式的日期字符串
      editModalVisible.value = true;
    };
    
    // 处理编辑确认
    const handleEditOk = () => {
      editFormRef.value.validate().then(() => {
        // 直接使用 editingRequirement 对象，因为 a-date-picker 已经返回了 YYYY-MM-DD 格式的字符串
        const requirementData = { ...editingRequirement };
        
        requirementApi.updateRequirement(requirementData.id, requirementData)
          .then(() => {
            message.success('更新需求成功');
            editModalVisible.value = false;
            fetchRequirements();
          })
          .catch(error => {
            message.error('更新需求失败');
            console.error('Error updating requirement:', error);
          });
      }).catch(() => {});
    };
    
    // 处理编辑取消
    const handleEditCancel = () => {
      editModalVisible.value = false;
    };
    
    // 处理删除需求
    const handleDelete = (id) => {
      requirementApi.deleteRequirement(id)
        .then(() => {
          message.success('删除需求成功');
          fetchRequirements();
        })
        .catch(error => {
          message.error('删除需求失败');
          console.error('Error deleting requirement:', error);
        });
    };
    
    // 页面挂载时获取下拉选项和需求列表
    onMounted(() => {
      fetchOptions();
      fetchRequirements();
    });
    
    return {
      requirements,
      options,
      searchParams,
      columns,
      addModalVisible,
      newRequirement,
      addFormRef,
      editModalVisible,
      editingRequirement,
      editFormRef,
      rules,
      showAddModal,
      handleAddOk,
      handleAddCancel,
      showEditModal,
      handleEditOk,
      handleEditCancel,
      handleDelete,
      fetchRequirements,
      handleSearch,
      resetSearch
    };
  }
};
</script>

<style scoped>
.requirements-container {
  padding: 20px;
}
</style>