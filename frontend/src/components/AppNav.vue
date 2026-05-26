<template>
  <nav>
    <a class="nav-logo" href="#">
      <div class="nav-logo-icon">L</div>
      <div class="nav-logo-text">Lingua<span>Flow</span></div>
    </a>
    <ul class="nav-links">
      <li v-for="link in navLinks" :key="link">
        <a href="#">{{ link }}</a>
      </li>
    </ul>
    <div class="nav-actions">
      <button class="btn-ghost">登录</button>
      <button class="btn-primary">免费开始</button>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';

const navLinks = ref(['课程', '语种', '学习路径', '社区']);
</script>