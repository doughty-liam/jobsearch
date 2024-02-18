<template>
  <div id="menu">
    <div class="options" id="filter">Filter</div>
    <div class="options" id="find-matches">Find Matches</div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

  #menu {
    margin-bottom: 10px;
    display: flex;
  }

  #filter {
    text-align: left;
    padding-top: 10px;
    justify-content: left;
  }

  #find-matches {
    text-align: left;
    padding-left: 50px;
    padding-top: 10px;
  }

  .options {
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 20pt;
    font-weight: 700;
    background-color: transparent;
    color: #003566;
    justify-self: center;
    height: 100%;
    padding-top: 10px;
  }

</style>