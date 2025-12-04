<template>
  <div class="users">
    <a-page-header
      class="site-page-header"
      title="用户管理"
      sub-title="管理系统用户信息"
    >
      <template #extra>
        <a-button type="primary" @click="showModal">
          <template #icon>
            <PlusOutlined />
          </template>
          添加用户
        </a-button>
      </template>
    </a-page-header>

    <a-table
      :columns="columns"
      :data-source="users"
      :pagination="{ pageSize: 10 }"
      :row-key="row => row.id"
    >
      <template #action="{ record }">
        <a-space>
          <a-button type="link" @click="editUser(record)">
            <template #icon>
              <EditOutlined />
            </template>
            编辑
          </a-button>
          <a-button type="link" danger @click="deleteUser(record.id)">
            <template #icon>
              <DeleteOutlined />
            </template>
            删除
          </a-button>
        </a-space>
      </template>
    </a-table>

    <!-- 添加/编辑用户模态框 -->
    <a-modal
      v-model:open="modalVisible"
      :title="isEdit ? '编辑用户' : '添加用户'"
      @ok="handleOk"
      @cancel="handleCancel"
    >
      <a-form :model="form" layout="vertical">
        <a-form-item label="用户名" :rules="[{ required: true, message: '请输入用户名' }]">
          <a-input v-model:value="form.username" placeholder="请输入用户名" />
        </a-form-item>
        <a-form-item label="邮箱" :rules="[{ required: true, message: '请输入邮箱', type: 'email' }]">
          <a-input v-model:value="form.email" placeholder="请输入邮箱" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { PlusOutlined, EditOutlined, DeleteOutlined } from '@ant-design/icons-vue'
import { getUserList, createUser, updateUser, deleteUser as deleteUserApi } from '../api/user'

export default {
  name: 'Users',
  components: {
    PlusOutlined,
    EditOutlined,
    DeleteOutlined
  },
  setup() {
    const users = ref([])
    const modalVisible = ref(false)
    const isEdit = ref(false)
    const form = ref({
      username: '',
      email: ''
    })

    const columns = [
      { title: 'ID', dataIndex: 'id', key: 'id' },
      { title: '用户名', dataIndex: 'username', key: 'username' },
      { title: '邮箱', dataIndex: 'email', key: 'email' },
      { title: '创建时间', dataIndex: 'created_at', key: 'created_at' },
      { title: '操作', key: 'action', slots: { customRender: 'action' }, width: 150 }
    ]

    // 获取用户列表
    const fetchUsers = async () => {
      try {
        const response = await getUserList()
        users.value = response.data
      } catch (error) {
        message.error('获取用户列表失败')
      }
    }

    // 显示添加用户模态框
    const showModal = () => {
      isEdit.value = false
      form.value = { username: '', email: '' }
      modalVisible.value = true
    }

    // 编辑用户
    const editUser = (record) => {
      isEdit.value = true
      form.value = { ...record }
      modalVisible.value = true
    }

    // 处理模态框确认
    const handleOk = async () => {
      try {
        if (isEdit.value) {
          await updateUser(form.value.id, form.value)
          message.success('用户更新成功')
        } else {
          await createUser(form.value)
          message.success('用户添加成功')
        }
        modalVisible.value = false
        fetchUsers()
      } catch (error) {
        message.error(isEdit.value ? '用户更新失败' : '用户添加失败')
      }
    }

    // 处理模态框取消
    const handleCancel = () => {
      modalVisible.value = false
    }

    // 删除用户
    const deleteUser = async (id) => {
      try {
        await deleteUserApi(id)
        message.success('用户删除成功')
        fetchUsers()
      } catch (error) {
        message.error('用户删除失败')
      }
    }

    // 组件挂载时获取用户列表
    onMounted(() => {
      fetchUsers()
    })

    return {
      users,
      columns,
      modalVisible,
      isEdit,
      form,
      showModal,
      editUser,
      handleOk,
      handleCancel,
      deleteUser
    }
  }
}
</script>

<style scoped>
.users {
  padding: 24px 0;
}
</style>