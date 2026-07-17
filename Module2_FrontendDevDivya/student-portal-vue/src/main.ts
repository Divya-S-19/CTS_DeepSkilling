import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.config.errorHandler = (err, vm, info) => {
  console.error('Global Error:', err)
  console.error('Info:', info)

  alert('Something went wrong!')
}

app.mount('#app')