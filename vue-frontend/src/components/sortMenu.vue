<template>
    <div>
        <div id="options-container">
            <p class="option">similarity rating</p>
            <p class="option">date posted</p>
        </div>
    </div>    
</template>

<script>

</script>

<style>

    #options-container {
        height: 100px;
        width: 150px;
        display:flex;
        flex-direction: column;
        flex: 100px;
        background-color: #103047;
        border-radius: 5px;
        border: 1px solid #605d6a;
    }   

    .option {
        font-size: 14pt;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 500;
        color: rgb(247, 246, 237);
        flex: 1;
        text-align: center;
        line-height: 50px;
        margin: 0;
        transition: color 0.5s;
    }

    .option:hover {
        color: rgb(201, 216, 255);
    }
</style>