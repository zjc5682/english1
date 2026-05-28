import { defineStore} from 'pinia'
import { ref, computed} from 'vue'
import apiClient from '@/api/client'

export interface User {
    id :number
    username :string
    email :string
    is_active :boolean
}
export interface LoginCredentials{
    username?:string
    email?:string
    password:string
}//新增一个登录凭证接口

export interface RegisterCredentials{
    username?:string
    email?:string
    password:string
}



export const useAuthStore = defineStore('auth',() =>{
    const token = ref<string>(localStorage.getItem('access_token')||'')
    const user = ref<User |null>(null)

    const isLoggedIn = computed(()=> !!token.value)

    //设置请求头
    function setAuthHeader(){
        if(token.value){
            apiClient.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
        }
        else{
            delete apiClient.defaults.headers.common['Authorization']
        }
        
    }


    //初始化时设置
    setAuthHeader()

    //注册
    async function register(credrntials:RegisterCredentials){
        const {data}= await apiClient.post('/auth/register',
            credrntials
        )
        return data
    }

    //登录
    async function login(credentials: LoginCredentials){
        const {data} = await apiClient.post('/auth/login',
            credentials
        )
        token.value = data.access_token
        localStorage.setItem('access_token',token.value)
        setAuthHeader()
        await fetchUser()
        return data
    }

    //获取用户信息
    async function fetchUser(){
        if (!token.value)return
        try{
            const {data} = await apiClient.get('/auth/me')
                user.value = data
           }
        catch(error){
                logout()
            }
    }

    //登出
    async function logout(){
        token.value = ''
        user.value = null
        localStorage.removeItem('access_token')
        setAuthHeader()
    }

    return{
        token,
        user,
        isLoggedIn,
        register,
        login,
        fetchUser,
        logout,
    }
})