<template>
  <div id="details-container">
    <p>{{ title }}</p>
    <p>{{ location }}</p>
    <p>{{ description }}</p>
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
}

</style>