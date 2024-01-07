<template>
  <div id="details-container">
    <h3 id="jobTitle">{{ title }}</h3>
    <h4>{{companyName}} {{ location }}</h4>
    <pre id="description_container">{{ description }}</pre>
  </div>
</template>

<script>
export default {
  name: 'jobDetails',
  props: {
    id: {required: false, type: Number, default: -5},
    companyName: {required: true, type: String, default: ""},
    title: {required: true, type: String, default: "Select a job to view details"},
    location: {required: true, type: String, default: ""},
    description: {required: true, type: String, default: ""}
  }

}
</script>

<style>

#details-container {
  background-color: rgb(255, 255, 255);
  height: calc(100vh - 65px);
  margin-left: 5px;
  border-radius: 8px;
  margin-right: 5px;
  overflow-y: auto;
  text-align: center;

}

#description_container {
  background-color: rgb(255, 255, 255);
  font-family: Arial, Helvetica, sans-serif;
  color: black;
  text-align: left;
  padding: 10px;
  white-space: pre-wrap;
  overflow-y: auto;
  overflow-x: auto;
}

</style>