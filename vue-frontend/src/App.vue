<template>
  <ul v-for="job in jobs" :key="job.id" id="joblist">  
    <jobPosting :title="job.title" :location="job.location" :description="job.description"></jobPosting>
  </ul>
</template>

<script>

import jobPosting from './components/jobPosting.vue'

const lodash = require('lodash')
const uniqueId = lodash.uniqueId;

export default {
  name: 'App',
  components: {
    jobPosting
  },
  data() {
    return {
      jobs: [ 
        {id: uniqueId("job"), title: "Software Engineer Intern", location: "Toronto", description: "Description 1"},
        {id: uniqueId("job"), title: "Data Engineering Intern", location: "Oakville", description: "Description 2"},
        {id: uniqueId("job"), title: "Data Analytics - Summer Student", location: "Edmonton", description: "Description 3"}
      ]
    }
  }
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
