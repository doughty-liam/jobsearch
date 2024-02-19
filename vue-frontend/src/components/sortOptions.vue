<template>
  <div id="menu">
    <div class="options" id="filter">Filter</div>
  </div>
</template>

<script>
export default {

}
</script>

<!-- Trigger event from here which is handled
by the parent component, App.vue -->

<style>

  #menu {
    margin-bottom: 10px;
    display: flex;
  }

  #filter {
    text-align: center;
    width: 150px;
    margin-left: 50px;
    padding-top: 10px;
    justify-content: left;
  }

  .options {
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 20pt;
    font-weight: 700;
    background-color: transparent;
    color: #e2d6be  ;
    justify-self: center;
    height: 100%;
    padding-top: 10px;
    transition-duration: 0.6s;
  }

  .options:hover {
    color: #d230c2;
    font-size: 20.5pt;
  }

</style>