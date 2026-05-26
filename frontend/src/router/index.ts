import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect:'/home'
    },
    {
      path:'/home',
      name:'home',
      component:() => import('../views/HomeView.vue')
    },
    {
      path:'/login',
      name:'login',
      component:()=> import('../views/LoginView.vue')
    },
    {
      path:'/register',
      name:'register',
      component:()=> import('../views/RegisterView.vue')
    },
    //关于页面保存
    {
      path:'/about',
      name:'about',
      component:()=> import('../views/AboutView.vue')
    },
  ],
})


export default router
