<template>
  <div>
    <ul v-for="job in results.result.value" :key="job.id" id="joblist">
      <jobPosting :title="job.title" :location="job.location" :description="job.description"></jobPosting>
      <!-- <router-link to="/home" :title="job.title" :location="job.location" :description="job.description"></router-link>   -->
    </ul>
  </div>
</template>

<script>

import jobPosting from './components/jobPosting.vue'
import gql from 'graphql-tag'
import {provideApolloClient, useQuery} from '@vue/apollo-composable'
import client from './apollo-config'

// const lodash = require('lodash')
// const uniqueId = lodash.uniqueId;

export default {
  name: 'App',
  components: {
    jobPosting
  },
  setup() {

    provideApolloClient(client);

    const results = useQuery(gql`
        query getPostings {
          job {
          title
          location
          description
          }
        }
      `,
    );
    return {
      results
    }
    // console.log(results.result.value.job);
  },

}
/*   data() {
    return {
      postings: null, [ 
        {id: uniqueId("job"), title: "Software Engineer Intern", location: "Toronto", description: "Description 1"},
        {id: uniqueId("job"), title: "Data Engineering Intern", location: "Oakville", description: "Description 2"},
        {id: uniqueId("job"), title: "Data Analytics - Summer Student", location: "Edmonton", description: "Description 3"}
      ]
    };
  },

  async testWilsonAPI() {
    const results = client.query({
      query: gql`
        job {
          title
          location
          description
        }
      `,
    });

    this.postings = results.data; */
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
