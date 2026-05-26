<template>
  <section class="testimonials" id="testimonials">
    <div class="section-header">
      <div class="section-label">用户评价</div>
      <h2>听听学习者怎么说</h2>
      <p>来自全球学习者的真实反馈</p>
    </div>
    <div class="testimonials-grid">
      <div class="testimonial-card" v-for="(item, index) in testimonials" :key="index">
        <div class="testimonial-stars">★★★★★</div>
        <blockquote>"{{ item.quote }}"</blockquote>
        <div class="testimonial-author">
          <div class="testimonial-avatar" :class="item.avatarClass">{{ item.avatar }}</div>
          <div>
            <div class="testimonial-name">{{ item.name }}</div>
            <div class="testimonial-role">{{ item.role }}</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const testimonials = ref([
  { quote: '用了三个月就能和日本朋友简单对话了！AI 对话练习功能让我克服了开口说的心理障碍，每天学习都像在玩游戏一样开心。', avatar: '林', avatarClass: 't1', name: '林小雨', role: '日语学习者 · 学习 3 个月' },
  { quote: '间隔重复的记忆方法真的很有效！以前背单词总是记不住，现在学的法语单词记得特别牢，推荐给所有想学语言的朋友。', avatar: '张', avatarClass: 't2', name: '张明远', role: '法语学习者 · 学习 6 个月' },
  { quote: '界面设计非常舒服，学习体验很流畅。课程内容贴近生活，不是枯燥的语法堆砌，而是真正能用上的表达。', avatar: '王', avatarClass: 't3', name: '王思琪', role: '韩语学习者 · 学习 1 年' }
]);
</script>