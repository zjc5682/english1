<template>
  <div class="words">
    <h1>单词本</h1>
    <ul>
      <li v-for="word in words" :key="word.id">
        <strong>{{ word.english }}</strong> - {{ word.chinese }}
        <span v-if="word.part_of_speech">({{ word.part_of_speech }})</span>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import apiClient from '@/api/client'

interface Word {
  id: number
  english: string
  chinese: string
  part_of_speech?: string
  example_sentence?: string
}

const words = ref<Word[]>([])

onMounted(async () => {
  try {
    const response = await apiClient.get('/words/')
    words.value = response.data
  } catch (error) {
    console.error('获取单词失败', error)
  }
})
</script>
