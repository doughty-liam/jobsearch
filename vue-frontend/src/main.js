import { createApp } from 'vue'
import App from './App.vue'
import apolloClient from '@/apollo-config.js'
// import vueConfig from 'vue.config'

createApp(App).use(apolloClient).mount('#app')

// Try running 'npm run build' and then opening the index.html file.
