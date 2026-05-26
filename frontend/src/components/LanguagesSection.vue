<template>
  <section class="languages" id="languages">
    <div class="section-header">
      <div class="section-label">热门语种</div>
      <h2>选择你想学习的语言</h2>
      <p>涵盖 32 种语言，从热门语种到小众语言，总有适合你的</p>
    </div>
    <div class="language-grid">
      <div class="language-card" v-for="(lang, index) in languages" :key="index">
        <span class="language-flag">{{ lang.flag }}</span>
        <h4>{{ lang.name }}</h4>
        <p>{{ lang.native }}</p>
        <span class="language-learners">{{ lang.learners }}</span>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const languages = ref([
  { flag: '🇺🇸', name: '英语', native: 'English', learners: '180万学习者' },
  { flag: '🇯🇵', name: '日语', native: '日本語', learners: '120万学习者' },
  { flag: '🇰🇷', name: '韩语', native: '한국어', learners: '95万学习者' },
  { flag: '🇫🇷', name: '法语', native: 'Français', learners: '68万学习者' },
  { flag: '🇩🇪', name: '德语', native: 'Deutsch', learners: '52万学习者' },
  { flag: '🇪🇸', name: '西班牙语', native: 'Español', learners: '76万学习者' },
  { flag: '🇮🇹', name: '意大利语', native: 'Italiano', learners: '35万学习者' },
  { flag: '🇵🇹', name: '葡萄牙语', native: 'Português', learners: '28万学习者' }
]);
</script>