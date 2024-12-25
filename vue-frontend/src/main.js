import { createApp } from 'vue'
import App from './App.vue'
import apolloClient from './apollo-config'
import {createApolloProvider} from '@vue/apollo-option'
import { library } from "@fortawesome/fontawesome-svg-core";
import  { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"
import './assets/styles/jobsearch.css'
// import vueConfig from 'vue.config'

const apolloProvider = createApolloProvider({
    defaultClient: apolloClient,
});

library.add(faMagnifyingGlass);
createApp(App).use(apolloProvider).component("font-awesome-icon", FontAwesomeIcon).mount('#app')

// Try running 'npm run build' and then opening the index.html file.
