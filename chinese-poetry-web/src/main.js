import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.config.globalProperties.BASE_URL = 'http://localhost:5000/'
app.use(router)

app.mount('#app')
