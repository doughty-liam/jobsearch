<template>
  <div>
    <sortOptions></sortOptions>
    <ul v-for="job in jobs" :key="job.id" id="joblist">
      <jobPosting :title="job.title" :location="job.location" :description="job.description"></jobPosting>
    </ul>
  </div>
</template>

<script>

import jobPosting from './components/jobPosting.vue'
import sortOptions from './components/sortOptions.vue'
import { computed } from 'vue'
import gql from 'graphql-tag'
import {provideApolloClient, useQuery} from '@vue/apollo-composable'
import client from './apollo-config'

export default {
  name: 'App',
  components: {
    jobPosting,
    sortOptions
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
  background-color: #41502c;
  width: 40%;
  margin-top: 60px;
  margin-left: 10px;
}

#joblist {
  display: flex;
  margin: 2px;
  padding: 0px;
}

</style>
