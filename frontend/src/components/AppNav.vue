<template>
  <nav :class="{'nav-scrolled':scrolled}"> <!--<nav>是HTML5语音化标签，表示导航栏连接区域-->
    <a class="nav-logo" href="#">
      <div class="nav-logo-icon">L</div>
      <div class="nav-logo-text">Lingua<span>Flow</span></div>
    </a>
    <ul class="nav-links">
      <li v-for="link in navLinks" :key="link.text">
        <a href="javascript:void(0)" @click="scrollTo(link.href)">{{ link.text }}</a>
      </li>
    </ul>
    <div class="nav-actions">
      <button class="btn-ghost" @click="goToLogin">登录</button>
      <button class="btn-primary" @click="goTORegister">免费开始</button>
    </div>
  </nav>
</template>

<script setup>
import { onMounted, ref,nextTick } from 'vue';
import router from '@/router';




const navLinks = ref([
    {text:'课程',href:'#features'},
    {text:'语种',href:'#languages'},
    {text:'学习路径',href:'#path'},
    {text:'社区',href:'#testimonials'},
]);
const scrolled = ref(false)

onMounted(()=>{
    window.addEventListener('scroll',()=>{
        scrolled.value=window.scroll >10
    })
})
const scrollTo = (href) =>{
    router.push({path:'/',hash: href});

    nextTick(() =>{
        const element = document.querySelector(href);
        if(element){
            element.scrollIntoView({behavior:'smooth'});
        }
    })
}

//跳转登录页面
const goToLogin =() =>{
    router.push('/login')
}
//跳转到注册界面
const goTORegister = () =>{
    router.push('/register')
}
</script>