<template>
  <div id="mainContainer">
    <div id="optionsBar">
      <sortOptions></sortOptions>
    </div>
    <div id="main">
      <div id="listContainer">
        <ul v-for="job in jobs" :key="job.id" id="joblist">
          <jobPosting :title="job.title" :location="job.location" :description="job.description" v-on:click="updateJobDetails(job.id, job.title, job.companyName, job.location, job.description)"></jobPosting>
        </ul>
      </div>
      <div id="details">
        <jobDetails :key="selectedJob.id" :title="selectedJob.title" :companyName="selectedJob.company" :location="selectedJob.location" :description="selectedJob.description"></jobDetails>
      </div>
    </div>
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
    updateJobDetails(id, title, companyName, location, description) {
      
      companyName = companyName + " | ";

      this.selectedJob = {
        id: id,
        title: title,
        company: companyName,
        location: location,
        description: description
      }

    }
  },

  setup() {

    provideApolloClient(client);

    const {result} = useQuery(gql`
    query {
	    jobsBySimilarity {
        id
        title
        companyName
        location
        description
      }
    }
      `,
    );
    
    const jobs = computed(() => result.value?.jobsBySimilarity ?? []);
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
}

#optionsBar {
  display: flex;
  position: absolute;
  width: 100%;
  height: 55px;
  margin: 0px;
  top: 0px;
  background-color: #50616b;
}

#main {
  margin-top: 60px;
  display: grid;
  grid-template-columns: 50% 50%;
}

#listContainer {
  height: calc(100vh - 65px);
  overflow-y: scroll;
}

::-webkit-scrollbar {
  width: 0px;
  background: transparent;
}

#joblist {
  margin: 0px;
  margin-left: 5px;
  padding: 0px;
}

</style>
