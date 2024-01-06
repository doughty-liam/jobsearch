<template>
  <div id="mainContainer">
    <div id="listContainer">
      <sortOptions></sortOptions>
      <ul v-for="job in jobs" :key="job.id" id="joblist">
        <jobPosting :title="job.title" :location="job.location" :description="job.description" v-on:click="updateJobDetails(job.id, job.title, job.location, job.description)"></jobPosting>
      </ul>
    </div>
    <jobDetails :key="selectedJob.id" :title="selectedJob.title" :location="selectedJob.location" :description="selectedJob.description"></jobDetails>
  </div>
</template>

<script>

import jobPosting from './components/jobPosting.vue'
import sortOptions from './components/sortOptions.vue'
import jobDetails from './components/jobDetails.vue'
import { computed } from 'vue'
import gql from 'graphql-tag'
import {provideApolloClient, useQuery} from '@vue/apollo-composable'
import client from './apollo-config'

export default {
  name: 'App',
  components: {
    jobPosting,
    sortOptions,
    jobDetails
  },
  data() {

    return {
      selectedJob: {}
    }
  },

  methods: {
    updateJobDetails(id, title, location, description) {
      
      this.selectedJob = {
        id: id,
        title: title,
        location: location,
        description: description
      }

    }
  },

  setup() {

    provideApolloClient(client);

    const {result} = useQuery(gql`
    query {
	    jobsByDateAdded(keyword: "python") {
        id
        title
        location
        description
      }
    }
      `,
    );
    
    const jobs = computed(() => result.value?.jobsByDateAdded ?? []);
    return {
      jobs,
    }
  },
}

</script>

<style>
#mainContainer {
  display: flex;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #2c3a50;
  width: 100%;
  margin-top: 60px;
}

#listContainer {
  width: 50%;
}

#joblist {
  margin: 2px;
  padding: 0px;
}


</style>
