<template>
  <!-- NAV -->
  <div class="topnav">
    <a class="nav-logo" href="#">
      <div class="nav-logo-icon">L</div>
      <div class="nav-logo-text">Lingua<span>Flow</span></div>
    </a>
    <!-- 点击返回首页 -->
    <a class="nav-back" href="#" @click.prevent="router.push('/')">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="15 18 9 12 15 6"/>
      </svg>
      返回首页
    </a>
  </div>

  <!-- REGISTER CARD -->
  <div class="register-wrapper">

    <!-- LEFT: Branding -->
    <div class="left-panel">
      <div class="left-top">
        <h2>开启你的语言之旅</h2>
        <p>加入 500 万+ 学习者的社区，每天 15 分钟，轻松掌握一门新语言。</p>
      </div>

      <div class="left-illustration">
        <div class="illust-container">
          <div class="illust-circle">
            <span class="illust-emoji">🎓</span>
          </div>
          <!-- 使用 v-for 循环渲染浮动卡片 -->
          <div 
            v-for="card in floatCards" 
            :key="card.text" 
            class="illust-float-card" 
            :class="card.cardClass"
          >
            <span class="fc-icon" :class="card.iconClass">{{ card.icon }}</span>
            {{ card.text }}
          </div>
        </div>
      </div>

      <!-- 使用 v-for 循环渲染统计数据 -->
      <div class="left-bottom">
        <div v-for="stat in stats" :key="stat.label" class="left-stat">
          <h3>{{ stat.value }}</h3>
          <p>{{ stat.label }}</p>
        </div>
      </div>
    </div>

    <!-- RIGHT: Form -->
    <div class="right-panel">
      <div class="form-header">
        <h1>创建账号</h1>
        <p>已有账号？<a href="#" @click.prevent="router.push('/login')">立即登录</a></p>
      </div>

      <!-- Social -->
      <div class="social-login">
        <button v-for="btn in socialButtons" :key="btn.label" class="social-btn">
          <span class="social-icon">{{ btn.icon }}</span>
          {{ btn.label }}
        </button>
      </div>

      <div class="divider">
        <div class="divider-line"></div>
        <span class="divider-text">或使用邮箱注册</span>
        <div class="divider-line"></div>
      </div>

      <!-- Form -->
      <!-- 绑定提交事件 -->
      <form @submit.prevent="handleSubmit">
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">姓名</label>
            <div class="input-wrapper">
              <!-- v-model 绑定姓名 -->
              <input 
                v-model="form.name" 
                type="text" 
                class="form-input" 
                placeholder="你的名字"
              >
              <span class="input-icon">👤</span>
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">想学的语言</label>
            <div class="lang-select-wrapper">
              <!-- v-model 绑定语言 -->
              <select v-model="form.language" class="form-select">
                <option v-for="opt in languageOptions" :key="opt.value" :value="opt.value">
                  {{ opt.label }}
                </option>
              </select>
              <span class="input-icon">🌍</span>
              <span class="select-arrow">▼</span>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">邮箱地址</label>
          <div class="input-wrapper">
            <!-- v-model 绑定邮箱 -->
            <input 
              v-model="form.email" 
              type="email" 
              class="form-input" 
              placeholder="name@example.com"
            >
            <span class="input-icon">✉️</span>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">设置密码</label>
          <div class="input-wrapper">
            <!-- v-model 绑定密码，动态 type -->
            <input 
              v-model="form.password" 
              :type="passwordVisible ? 'text' : 'password'" 
              class="form-input" 
              placeholder="至少 8 位，含字母和数字"
            >
            <span class="input-icon">🔒</span>
            <button type="button" class="input-toggle" @click="passwordVisible = !passwordVisible">
              {{ passwordVisible ? '🙈' : '👁' }}
            </button>
          </div>
          <!-- 密码强度条 -->
          <div class="password-strength">
            <div 
              v-for="i in 4" 
              :key="i" 
              class="strength-bar"
              :class="{ active: strengthLevel.score >= i, [strengthLevel.cls]: strengthLevel.score >= i }"
            ></div>
          </div>
          <div v-if="form.password" class="strength-text" :class="strengthLevel.cls">
            密码强度：{{ strengthLevel.label }}
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">确认密码</label>
          <div class="input-wrapper">
            <input 
              v-model="form.confirmPassword" 
              :type="passwordVisible ? 'text' : 'password'" 
              class="form-input" 
              placeholder="再次输入密码"
            >
            <span class="input-icon">🔒</span>
          </div>
        </div>

        <div class="form-checkbox-group">
          <div 
            class="custom-checkbox" 
            :class="{ checked: agreed }" 
            @click="agreed = !agreed"
          >
            <span class="checkmark">✓</span>
          </div>
          <label @click="agreed = !agreed">
            我已阅读并同意 <a href="#">服务条款</a> 和 <a href="#">隐私政策</a>
          </label>
        </div>

        <!-- 错误提示 -->
        <div v-if="errorMsg" class="error-message">
          ⚠️ {{ errorMsg }}
        </div>

        <button type="submit" class="btn-submit" :disabled="loading">
          {{ loading ? '注册中...' : '创建我的账号' }}
          <span v-if="!loading" class="arrow">→</span>
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

// 表单数据
const form = ref({
  name: '',
  language: '',
  email: '',
  password: '',
  confirmPassword: ''
})

// 状态
const loading = ref(false)
const errorMsg = ref('')
const passwordVisible = ref(false)
const agreed = ref(true)

// 静态数据
const socialButtons = [
  { icon: '🔵', label: 'Google' },
  { icon: '⚫', label: 'Apple' },
  { icon: '🟢', label: '微信' }
]

const languageOptions = [
  { value: '', label: '选择语言' },
  { value: 'en', label: '🇺🇸 英语' },
  { value: 'ja', label: '🇯🇵 日语' },
  { value: 'kr', label: '🇰🇷 韩语' },
  { value: 'fr', label: '🇫🇷 法语' },
  { value: 'de', label: '🇩🇪 德语' },
  { value: 'es', label: '🇪🇸 西班牙语' }
]

const stats = [
  { value: '500万+', label: '全球学习者' },
  { value: '32种', label: '可学语言' },
  { value: '4.9', label: '用户评分' }
]

const floatCards = [
  { icon: '✓', iconClass: 'green', text: '连续 7 天打卡', cardClass: 'card-1' },
  { icon: '⚡', iconClass: 'yellow', text: '+120 XP 获得', cardClass: 'card-2' },
  { icon: '🔥', iconClass: 'blue', text: '新单词已掌握', cardClass: 'card-3' }
]

// 密码强度计算 (移植自您的原始代码逻辑)
const strengthLevel = computed(() => {
  const val = form.value.password
  if (val.length === 0) return { score: 0, label: '', cls: '' }

  let score = 0
  if (val.length >= 6) score++
  if (val.length >= 10) score++
  if (/[A-Z]/.test(val) && /[a-z]/.test(val)) score++
  if (/[0-9]/.test(val) && /[^A-Za-z0-9]/.test(val)) score++

  const levels = [
    { cls: 'weak', label: '弱' },
    { cls: 'medium', label: '一般' },
    { cls: 'strong', label: '良好' },
    { cls: 'very-strong', label: '非常强' }
  ]

  const level = levels[Math.min(score, 3)]
  return { score: Math.min(score, 3), ...level }
})

// 提交处理 (对接您的接口逻辑)
const handleSubmit = async () => {
  if (!agreed.value) {
    errorMsg.value = '请先同意服务条款和隐私政策'
    return
  }
  
  if (form.value.password !== form.value.confirmPassword) {
    errorMsg.value = '两次输入的密码不一致'
    return
  }

  loading.value = true
  errorMsg.value = ''
  
  try {
    // 调用 authStore 的注册方法
    // 注意：您的 store 接口参数需要对应，这里假设 register 接受一个对象
    await authStore.register(
        form.value.name, // 将 name 映射为 username
        form.value.email,
        form.value.password
      // language 可以根据后端需求决定是否发送
    )
    
    // 注册成功后跳转
    router.push('/')
    console.log('注册成功！') 
  } catch (err) {
    errorMsg.value = err.response?.data?.detail || '注册失败，请稍后重试'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
:root {
    --cyan-50: #e0f7fa;
    --cyan-100: #b2ebf2;
    --cyan-200: #80deea;
    --cyan-300: #4dd0e1;
    --cyan-400: #26c6da;
    --cyan-500: #00bcd4;
    --cyan-600: #00acc1;
    --cyan-700: #0097a7;
    --cyan-800: #00838f;
    --cyan-900: #006064;
    --white: #ffffff;
    --snow: #f8fcfd;
    --text-dark: #1a3a4a;
    --text-body: #3e6070;
    --text-muted: #7a9aab;
    --shadow-soft: 0 4px 24px rgba(0, 150, 167, 0.08);
    --shadow-hover: 0 8px 40px rgba(0, 150, 167, 0.15);
    --radius: 16px;
    --radius-lg: 24px;
    --radius-xl: 32px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

/* 注意：body 样式在 scoped 中可能不生效，建议移至全局 main.css */
body {
    font-family: 'Nunito', sans-serif;
    background: var(--snow);
    color: var(--text-body);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
}

body::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse at 10% 30%, rgba(77, 208, 225, 0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 90% 70%, rgba(0, 188, 212, 0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 100%, rgba(0, 150, 167, 0.04) 0%, transparent 40%);
    pointer-events: none;
    z-index: 0;
}

/* ===== NAV ===== */
.topnav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 100;
    padding: 0 48px;
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(248, 252, 253, 0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(0, 188, 212, 0.08);
}

.nav-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
}

.nav-logo-icon {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, var(--cyan-300), var(--cyan-500));
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 800;
    font-size: 18px;
    box-shadow: 0 2px 12px rgba(0, 188, 212, 0.3);
}

.nav-logo-text {
    font-size: 22px;
    font-weight: 700;
    color: var(--text-dark);
}

.nav-logo-text span {
    color: var(--cyan-500);
}

.nav-back {
    display: flex;
    align-items: center;
    gap: 6px;
    text-decoration: none;
    color: var(--text-muted);
    font-size: 14px;
    font-weight: 600;
    transition: color 0.2s;
}

.nav-back:hover {
    color: var(--cyan-600);
}

.nav-back svg {
    transition: transform 0.2s;
}

.nav-back:hover svg {
    transform: translateX(-3px);
}

/* ===== MAIN CARD ===== */
.register-wrapper {
    position: relative;
    z-index: 1;
    display: flex;
    width: 1020px;
    min-height: 620px;
    background: var(--white);
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-hover);
    overflow: hidden;
    animation: fadeUp 0.7s ease forwards;
    margin: 100px auto 40px; /* 调整上边距以适应固定导航栏 */
}

/* ===== LEFT PANEL ===== */
.left-panel {
    flex: 1;
    background: linear-gradient(145deg, var(--cyan-500), var(--cyan-700));
    padding: 52px 44px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
}

.left-panel::before {
    content: '';
    position: absolute;
    top: -60%;
    right: -30%;
    width: 450px;
    height: 450px;
    background: radial-gradient(circle, rgba(255, 255, 255, 0.08) 0%, transparent 70%);
    border-radius: 50%;
}

.left-panel::after {
    content: '';
    position: absolute;
    bottom: -30%;
    left: -20%;
    width: 320px;
    height: 320px;
    background: radial-gradient(circle, rgba(255, 255, 255, 0.06) 0%, transparent 70%);
    border-radius: 50%;
}

.left-top {
    position: relative;
    z-index: 1;
}

.left-top h2 {
    font-size: 30px;
    font-weight: 800;
    color: white;
    line-height: 1.3;
    margin-bottom: 14px;
}

.left-top p {
    font-size: 15px;
    color: rgba(255, 255, 255, 0.8);
    line-height: 1.7;
    max-width: 320px;
}

/* Illustration area */
.left-illustration {
    position: relative;
    z-index: 1;
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 30px 0;
}

.illust-container {
    position: relative;
    width: 260px;
    height: 260px;
}

.illust-circle {
    width: 260px;
    height: 260px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    border: 2px dashed rgba(255, 255, 255, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    animation: float 5s ease-in-out infinite;
}

.illust-emoji {
    font-size: 100px;
    filter: drop-shadow(0 8px 24px rgba(0, 0, 0, 0.15));
}

.illust-float-card {
    position: absolute;
    background: rgba(255, 255, 255, 0.95);
    border-radius: 14px;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    font-weight: 700;
    color: var(--cyan-700);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.illust-float-card.card-1 {
    top: 10px;
    left: -30px;
    animation: float 4s ease-in-out infinite;
}

.illust-float-card.card-2 {
    bottom: 20px;
    right: -40px;
    animation: float 4s ease-in-out 1s infinite;
}

.illust-float-card.card-3 {
    top: 50%;
    right: -50px;
    transform: translateY(-50%);
    animation: float 4.5s ease-in-out 0.5s infinite;
}

.illust-float-card .fc-icon {
    width: 30px;
    height: 30px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
}

.illust-float-card .fc-icon.green { background: #e8f5e9; }
.illust-float-card .fc-icon.yellow { background: #fff8e1; }
.illust-float-card .fc-icon.blue { background: #e3f2fd; }

/* Bottom stats */
.left-bottom {
    position: relative;
    z-index: 1;
    display: flex;
    gap: 24px;
}

.left-stat {
    color: white;
}

.left-stat h3 {
    font-size: 22px;
    font-weight: 800;
}

.left-stat p {
    font-size: 12px;
    color: rgba(255, 255, 255, 0.7);
}

/* ===== RIGHT PANEL (FORM) ===== */
.right-panel {
    flex: 1;
    padding: 48px 48px 40px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.form-header {
    margin-bottom: 32px;
}

.form-header h1 {
    font-size: 28px;
    font-weight: 800;
    color: var(--text-dark);
    margin-bottom: 6px;
}

.form-header p {
    font-size: 14px;
    color: var(--text-muted);
}

.form-header p a {
    color: var(--cyan-500);
    text-decoration: none;
    font-weight: 700;
    transition: color 0.2s;
}

.form-header p a:hover {
    color: var(--cyan-700);
}

/* Social login */
.social-login {
    display: flex;
    gap: 12px;
    margin-bottom: 28px;
}

.social-btn {
    flex: 1;
    padding: 12px 0;
    border: 2px solid rgba(0, 188, 212, 0.1);
    border-radius: 12px;
    background: var(--white);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    font-family: 'Nunito', sans-serif;
    font-size: 14px;
    font-weight: 700;
    color: var(--text-body);
    transition: all 0.2s;
}

.social-btn:hover {
    border-color: var(--cyan-300);
    background: var(--cyan-50);
    transform: translateY(-1px);
}

.social-btn .social-icon {
    font-size: 18px;
}

/* Divider */
.divider {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 24px;
}

.divider-line {
    flex: 1;
    height: 1px;
    background: rgba(0, 188, 212, 0.1);
}

.divider-text {
    font-size: 12px;
    color: var(--text-muted);
    font-weight: 600;
}

/* Form fields */
.form-group {
    margin-bottom: 18px;
}

.form-row {
    display: flex;
    gap: 14px;
}

.form-row .form-group {
    flex: 1;
}

.form-label {
    display: block;
    font-size: 13px;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 7px;
}

.input-wrapper {
    position: relative;
}

.input-icon {
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 16px;
    color: var(--text-muted);
    pointer-events: none;
    transition: color 0.2s;
}

.form-input {
    width: 100%;
    padding: 12px 14px 12px 42px;
    border: 2px solid rgba(0, 188, 212, 0.12);
    border-radius: 12px;
    background: var(--snow);
    font-family: 'Nunito', sans-serif;
    font-size: 14px;
    color: var(--text-dark);
    outline: none;
    transition: all 0.3s;
}

.form-input::placeholder {
    color: var(--text-muted);
    font-weight: 400;
}

.form-input:focus {
    border-color: var(--cyan-400);
    background: var(--white);
    box-shadow: 0 0 0 4px rgba(0, 188, 212, 0.08);
}

.form-input:focus ~ .input-icon {
    color: var(--cyan-500);
}

.input-toggle {
    position: absolute;
    right: 14px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    cursor: pointer;
    font-size: 15px;
    color: var(--text-muted);
    padding: 4px;
    transition: color 0.2s;
}

.input-toggle:hover {
    color: var(--cyan-600);
}

/* Language select */
.lang-select-wrapper {
    position: relative;
}

.form-select {
    width: 100%;
    padding: 12px 14px 12px 42px;
    border: 2px solid rgba(0, 188, 212, 0.12);
    border-radius: 12px;
    background: var(--snow);
    font-family: 'Nunito', sans-serif;
    font-size: 14px;
    color: var(--text-dark);
    outline: none;
    appearance: none;
    -webkit-appearance: none;
    cursor: pointer;
    transition: all 0.3s;
}

.form-select:focus {
    border-color: var(--cyan-400);
    background: var(--white);
    box-shadow: 0 0 0 4px rgba(0, 188, 212, 0.08);
}

.select-arrow {
    position: absolute;
    right: 14px;
    top: 50%;
    transform: translateY(-50%);
    pointer-events: none;
    color: var(--text-muted);
    font-size: 12px;
}

/* Checkbox */
.form-checkbox-group {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 24px;
}

.custom-checkbox {
    flex-shrink: 0;
    width: 18px;
    height: 18px;
    border: 2px solid var(--cyan-200);
    border-radius: 5px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    margin-top: 1px;
}

.custom-checkbox.checked {
    background: linear-gradient(135deg, var(--cyan-400), var(--cyan-600));
    border-color: var(--cyan-500);
}

.custom-checkbox .checkmark {
    color: white;
    font-size: 11px;
    font-weight: 800;
    opacity: 0;
    transform: scale(0.5);
    transition: all 0.2s;
}

.custom-checkbox.checked .checkmark {
    opacity: 1;
    transform: scale(1);
}

.form-checkbox-group label {
    font-size: 13px;
    color: var(--text-muted);
    line-height: 1.5;
    cursor: pointer;
}

.form-checkbox-group label a {
    color: var(--cyan-500);
    text-decoration: none;
    font-weight: 600;
}

.form-checkbox-group label a:hover {
    color: var(--cyan-700);
}

/* Submit button */
.btn-submit {
    width: 100%;
    padding: 14px 0;
    border: none;
    border-radius: 14px;
    background: linear-gradient(135deg, var(--cyan-400), var(--cyan-600));
    color: white;
    font-family: 'Nunito', sans-serif;
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 4px 20px rgba(0, 188, 212, 0.25);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.btn-submit:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 28px rgba(0, 188, 212, 0.35);
}

.btn-submit:active {
    transform: translateY(0);
}

.btn-submit .arrow {
    transition: transform 0.3s;
}

.btn-submit:hover .arrow {
    transform: translateX(4px);
}

/* Password strength */
.password-strength {
    display: flex;
    gap: 5px;
    margin-top: 8px;
}

.strength-bar {
    flex: 1;
    height: 4px;
    border-radius: 2px;
    background: rgba(0, 188, 212, 0.1);
    transition: all 0.3s;
}

.strength-bar.active.weak { background: #ff8a65; }
.strength-bar.active.medium { background: #ffd54f; }
.strength-bar.active.strong { background: #4dd0e1; }
.strength-bar.active.very-strong { background: #0097a7; }

.strength-text {
    font-size: 11px;
    margin-top: 4px;
    font-weight: 600;
    transition: color 0.3s;
}

.strength-text.weak { color: #ff8a65; }
.strength-text.medium { color: #f9a825; }
.strength-text.strong { color: var(--cyan-500); }
.strength-text.very-strong { color: var(--cyan-700); }

/* 错误信息样式 (Vue版本新增) */
.error-message {
    background-color: #fff5f5;
    color: #c62828;
    border: 1px solid #ffcdd2;
    padding: 10px 14px;
    border-radius: 10px;
    font-size: 13px;
    margin-bottom: 18px;
    text-align: center;
}

/* ===== ANIMATIONS ===== */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.3); }
}

/* ===== RESPONSIVE ===== */
@media (max-width: 900px) {
    .register-wrapper {
        flex-direction: column;
        width: 92%;
        min-height: auto;
        margin-top: 80px;
    }
    .left-panel {
        padding: 36px 32px;
    }
    .left-illustration {
        display: none;
    }
    .right-panel {
        padding: 36px 32px;
    }
    .form-row {
        flex-direction: column;
        gap: 0;
    }
}
</style>