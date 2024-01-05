<template>
  <div id="details-container">
    <h3>{{ title }}</h3>
    <h4>{{ location }}</h4>
    <pre id="description_container">{{ description }}</pre>
  </div>
</template>

<script>
export default {
  name: 'jobDetails',
  props: {
    id: {required: false, type: Number, default: -5},
    title: {required: true, type: String, default: "Select a job to view details"},
    location: {required: true, type: String, default: ""},
    description: {required: true, type: String, default: ""}
  }

}
</script>

<style>

#details-container {
  background-color: rgb(255, 255, 255);
  width: 49%;
  height: 90%;
  margin-left: 5px;
  border-radius: 8px;
  margin-top: 4px;
  margin-right: 10px;
  position: fixed;
  right: 0px;
  overflow-y: auto;
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