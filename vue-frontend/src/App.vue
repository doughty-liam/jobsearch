<template>
  <div>
    <ul v-for="job in jobs" :key="job.id" id="joblist">
      <jobPosting :title="job.title" :location="job.location" :description="job.description"></jobPosting>
      <!-- <router-link to="/home" :title="job.title" :location="job.location" :description="job.description"></router-link>   -->
    </ul>
  </div>
</template>

<script>

import jobPosting from './components/jobPosting.vue'
import { computed } from 'vue'
import gql from 'graphql-tag'
import {provideApolloClient, useQuery} from '@vue/apollo-composable'
import client from './apollo-config'

export default {
  name: 'App',
  components: {
    jobPosting
  },

  setup() {

    provideApolloClient(client);

    const {result} = useQuery(gql`
      {
          allJobs {
          id
          title
          location
          description
          }
        }
      `,
    );
    
    const jobs = computed(() => result.value?.allJobs ?? []);
    return {
      jobs,
    }
  },
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 40%;
  margin-top: 60px;
}

#joblist {
  display: flex;
  margin: 2px;
}

</style>
