import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue' //导入根组件
import router from './router'
import './assets/main.css'

const app = createApp(App)
/*
    创建vue应用实例并挂载到DOM
    createApp(App)接收根组件作为参数返回一个实例应用
*/

app.use(createPinia())
app.use(router)

app.mount('#app')//.mount将应用实例挂载到index.html中id=“app”的元素


