<template>
    <div>
        <div id="menubar">
            <div class="menu" id="left">Left</div>
            <input type="search" placeholder="Enter comma-separated keywords..." class="menu" id="searchbar">
            <div class="menu" id="right">Right</div>
        </div>
    </div>
</template>

<script></script>

<style>

    #menubar {
        width: 100%;
        display: inline-flex;
        height: 100%;
        padding: 10px;
        
    }
    .menu {
        font-size: 14pt;
        margin: auto;
        color: white;
        font-family: Barlow Regular;
    }

    #searchbar {
        width: 20%;
        height: 100%;
        background-color: white;
        border-color: transparent;
        color: black;
        border-radius: 28px;
        font-size: 18pt;
    }

</style>