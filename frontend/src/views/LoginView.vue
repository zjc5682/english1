<template>
    <div class = "login-container">
        <h2>登录</h2>
        <form @submit.prevent="handleLogin">
            <div>
                <label>用户名</label>
                <input v-model="form.username" type="text" required/>
            </div>
            <div>
                <label>密码</label>
                <input v-model = "form.password" type="password" required/>
            </div>
            <p v-if="errorMsg" class="error"{{ errorMsg }}></p>
            <button type = "submit":disabled="loading">{{ loading?'登录中...':'登录' }}</button>
        </form>
        <p>还没有账号？
            <router-link to="/register">去注册</router-link>
        </p>
    </div>
</template>

<script setup lang="ts">
import { reactive,ref} from 'vue'
import { useRouter} from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const router = useRouter()

const form = reactive({
    username:'',
    password:'',
})
const loading = ref(false)
const errorMsg = ref('')

async function handleLogin(){
    loading.value = true
    errorMsg.value = ''
    try {
        await authStore.login(form.username,form.password)
        
        router.push('/') //登陆成功后跳转到首页
    }catch(err: any){
        errorMsg.value = err.response?.data?.detail ||'登陆失败，请检查用户名和密码'
    }finally{
        loading.value = false
    }
}
</script>

<style scoped>
.login-container{
    max-width:400px;
    margin:40px auto;
}
.error{
    color:red;
}
</style>