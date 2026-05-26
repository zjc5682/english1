<template>
  <section class="learning-path" id="path">
    <div class="section-header">
      <div class="section-label">学习路径</div>
      <h2>从零到流利，我们为你规划好每一步</h2>
      <p>科学分阶，循序渐进，每一步都有明确的目标</p>
    </div>
    <div class="path-container">
      <div class="path-step" v-for="step in steps" :key="step.num">
        <div class="path-number">{{ step.num }}</div>
        <div class="path-content">
          <h3>{{ step.title }}</h3>
          <p>{{ step.desc }}</p>
          <span class="path-tag">{{ step.tag }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const steps = ref([
  { num: 1, title: '基础入门 — 认识语音与基础词汇', desc: '从字母、发音规则开始，学习最常用的 500 个核心词汇和基础句型，建立语言感知力。', tag: '约 4 周 · 每日 15 分钟' },
  { num: 2, title: '日常对话 — 场景化学习', desc: '涵盖购物、点餐、问路、旅行等 20 个真实场景，通过 AI 对话练习提升口语表达能力。', tag: '约 8 周 · 每日 20 分钟' },
  { num: 3, title: '进阶提升 — 语法与表达深化', desc: '掌握复杂语法结构，学习地道表达方式，通过阅读和听力材料扩展语言输入量。', tag: '约 12 周 · 每日 25 分钟' },
  { num: 4, title: '流利表达 — 自如运用', desc: '深度话题讨论、文化理解、写作练习，让你能在各种场景下自信、流利地使用新语言。', tag: '持续学习 · 每日 30 分钟' }
]);
</script>