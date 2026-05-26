<template>
  <section class="hero">
    <div class="hero-content">
      <div class="hero-badge">
        <span class="hero-badge-dot"></span>
        全新 AI 驱动学习体验
      </div>
      <h1>用更温柔的方式，<br>学会一门<span class="highlight">新语言</span></h1>
      <p>沉浸式的学习体验，像学母语一样自然。AI 智能匹配你的节奏，每天 15 分钟，轻松掌握新语言。</p>
      
      <div class="hero-buttons">
        <button class="btn-primary btn-large" @click="goTORegister">免费开始学习</button>
        <button class="btn-outline">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          观看介绍
        </button>
      </div>

      <div class="hero-stats">
        <div class="hero-stat" v-for="stat in stats" :key="stat.label">
          <h3>{{ stat.value }}</h3>
          <p>{{ stat.label }}</p>
        </div>
      </div>
    </div>

    <div class="hero-visual">
      <div class="hero-card-stack">
        <div class="hero-main-card">
          <div class="hero-main-card-header">
            <span class="lesson-tag">{{ lesson.tag }}</span>
            <span class="lesson-progress-mini">
              <span class="dot-track"><span class="dot-fill" :style="{ width: lesson.progress + '%' }"></span></span>
              {{ lesson.current }}/{{ lesson.total }}
            </span>
          </div>
          <div class="word-display">
            <span class="emoji">{{ lesson.emoji }}</span>
            <div class="word">{{ lesson.word }}</div>
            <div class="pronunciation">{{ lesson.pronunciation }}</div>
            <div class="meaning">{{ lesson.meaning }}</div>
          </div>
          <div class="answer-options">
            <div 
              v-for="(opt, i) in options" 
              :key="i" 
              class="answer-option" 
              :class="{ 'correct': opt.correct && opt.selected, 'wrong': !opt.correct && opt.selected }"
              @click="selectOption(opt)"
            >
              {{ opt.text }}
            </div>
          </div>
        </div>

        <div class="hero-floating-card floating-streak">
          <span class="fire">🔥</span>
          <div>
            <div class="streak-text">连续学习</div>
            <div class="streak-num">12 天</div>
          </div>
        </div>

        <div class="hero-floating-card floating-xp">
          <div class="xp-icon">⚡</div>
          <div>
            <div class="xp-text">今日获得</div>
            <div class="xp-num">+120 XP</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import router from '@/router';//导入路由实例

const stats = ref([
  { value: '500万+', label: '全球学习者' },
  { value: '32种', label: '可学语言' },
  { value: '4.9', label: '用户评分' }
]);

const lesson = ref({
  tag: '日语 · 初级',
  progress: 60,
  current: 3,
  total: 5,
  emoji: '🌸',
  word: '桜 (さくら)',
  pronunciation: 'sakura',
  meaning: '樱花'
});

const options = ref([
  { text: '🌊 海', correct: false, selected: false },
  { text: '🌸 花', correct: true, selected: false },
  { text: '🍃 叶', correct: false, selected: false },
  { text: '🌙 月', correct: false, selected: false }
]);

const selectOption = (option) => {
  options.value.forEach(o => o.selected = false);
  option.selected = true;

};
const goTORegister = () =>{
    router.push('/register')
}
</script>