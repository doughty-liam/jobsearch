<template>
  <div id="menu">
    <div id="sortButton">Sort</div>
    <div id="filterButton">Filter</div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

  #menu {
    display: flex;
    margin-left: 2px;
    margin-bottom: 10px;
  }

  #sortButton {
    background-color: rgb(135, 82, 36);
    font-size: 14pt;
    padding: 5px;
  }

  #filterButton {
    background-color: orange;
    margin-left: 10px;
    font-size: 14pt;
    padding: 5px;
  }

</style>