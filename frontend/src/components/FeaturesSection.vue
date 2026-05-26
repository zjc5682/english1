<template>
  <section class="features" id="features">
    <div class="section-header">
      <div class="section-label">为什么选择我们</div>
      <h2>让学习变得自然而有效</h2>
      <p>融合认知科学与 AI 技术，为你打造最高效的语言学习体验</p>
    </div>
    <div class="features-grid">
      <div class="feature-card" v-for="(feature, index) in features" :key="index">
        <div class="feature-icon" :class="feature.color">{{ feature.icon }}</div>
        <h3>{{ feature.title }}</h3>
        <p>{{ feature.desc }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const features = ref([
  { icon: '🧠', color: 'blue', title: 'AI 个性化教学', desc: '智能分析你的学习习惯和薄弱环节，自动调整课程难度与内容，实现因材施教。' },
  { icon: '🎧', color: 'teal', title: '沉浸式听力训练', desc: '真实场景对话录音，配合智能语音识别，帮你练就地道的发音和听力。' },
  { icon: '🎮', color: 'sky', title: '游戏化学习', desc: '完成任务解锁成就、积累经验值，让每一次学习都充满成就感和乐趣。' },
  { icon: '📝', color: 'mint', title: '间隔重复记忆', desc: '基于遗忘曲线的智能复习系统，在最佳时机安排复习，让记忆更加牢固。' },
  { icon: '💬', color: 'lavender', title: 'AI 对话练习', desc: '与 AI 进行真实场景模拟对话，在安全的环境中大胆开口，无惧犯错。' },
  { icon: '🌍', color: 'peach', title: '全球学习社区', desc: '与来自世界各地的学习者互动交流，结伴学习，互相激励，共同进步。' }
]);
</script>