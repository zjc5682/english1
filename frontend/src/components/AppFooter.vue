<template>
  <footer>
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="nav-logo" href="#">
          <div class="nav-logo-icon">L</div>
          <div class="nav-logo-text">Lingua<span>Flow</span></div>
        </a>
        <p>让每一个人都能用更温柔的方式，学会一门新语言。用科技与爱，连接世界的每一个角落。</p>
      </div>
      
      <div class="footer-col" v-for="col in footerCols" :key="col.title">
        <h4>{{ col.title }}</h4>
        <ul>
          <li v-for="link in col.links" :key="link">
            <a href="#">{{ link }}</a>
          </li>
        </ul>
      </div>
    </div>
    
    <div class="footer-bottom">
      <p>&copy; 2026 LinguaFlow. 用爱连接语言。</p>
      <div class="footer-socials">
        <a class="footer-social-icon" href="#">𝕏</a>
        <a class="footer-social-icon" href="#">in</a>
        <a class="footer-social-icon" href="#">▶</a>
        <a class="footer-social-icon" href="#">📷</a>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue';

const footerCols = ref([
  { title: '产品', links: ['所有课程', '学习路径', 'AI 对话', '移动应用'] },
  { title: '支持', links: ['帮助中心', '联系我们', '社区论坛', '反馈建议'] },
  { title: '公司', links: ['关于我们', '加入团队', '隐私政策', '使用条款'] }
]);
</script>