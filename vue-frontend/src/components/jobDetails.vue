<template>
  <div id="details-container">
    <h3 id="jobTitle">{{ title }}</h3>
    <h4 id="company-location">{{companyName}} {{ location }}</h4>
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
  background-color: #103047;
  color: rgb(247, 246, 237);
  height: calc(100vh - 65px);
  margin-left: 5px;
  border-radius: 8px;
  margin-right: 5px;
  overflow-y: auto;
  text-align: center;

}

#description_container {
  background-color: #103047;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: rgb(247, 246, 237);
  text-align: left;
  padding: 10px;
  font-size: 14pt;
  white-space: pre-wrap;
  overflow-y: auto;
  overflow-x: auto;
}

#jobTitle {
  font-size: 30pt;
  color: rgb(247, 246, 237);
  font-weight:700;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

#company-location {
  color: rgb(247, 246, 237);
  font-size: 20pt;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>