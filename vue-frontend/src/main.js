import { createApp } from 'vue'
import App from './App.vue'
import apolloClient from './apollo-config'
import {createApolloProvider} from '@vue/apollo-option'
// import vueConfig from 'vue.config'

const apolloProvider = createApolloProvider({
    defaultClient: apolloClient,
});

createApp(App).use(apolloProvider).mount('#app')

// Try running 'npm run build' and then opening the index.html file.
