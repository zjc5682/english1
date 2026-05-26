<template>
    <div class = "register-container">
        <h2>注册</h2>
        <from @submit.prevent = "handleRegister">
            <div>
                <label>用户名</label>
                <input v-model = "form.username" type="text" required/>
            </div>
            <div>
                <label>邮箱</label>
                <input v-model = "form.email" type="email" required/>
            </div>
            <div>
                <label>密码</label>
                <input v-model = "form.password" type = "password" required/>
            </div>
            <p v-if="errorMsg" class = "error">{{ errorMsg }}</p>
            <button type = "submit":disabled="loading">
                {{ loading?'注册中...':'注册' }}
            </button>
        </from>>
        <p>
            已有账号？
            <router-link to="/login">去登录</router-link>
        </p>    

    </div>
</template>

<script setup lang="ts">
import {reactive,ref } from 'vue'
import {useRouter} from 'vue-router'
import {useAuthStore} from '@/stores/auth'

const authStore = useAuthStore()
const router = useRouter()

const form = reactive({
    username:'',
    email:'',
    password:'',
})
const loading = ref(false)
const errorMsg = ref('')

async function handleRegister(){
    loading.value = true
    errorMsg.value = ''
    try{
        await authStore.register(form.username,form.email,form.password)
        //注册成功后自动登录并跳转到首页
        await authStore.login (form.username,form.password)
        router.push('/')

    }
    catch(err:any){
        errorMsg.value = err.response?.data?.detail ||'注册失败，请稍后重试'
    }finally{
        loading.value = false
    }
}
</script>

<style scoped>
.register-container{
    max-width:400px;
    margin:40px auto;
}
.error{
    color:red;
}
</style>