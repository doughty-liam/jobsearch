<template>
    <div id="jobPosting">
        <h2 id="title">Software Engineer Intern</h2>
        <h5 id="location">Toronto</h5>
        <p id="description">Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus, vel rerum officia cumque nemo quia molestias pariatur vitae similique nisi, sit totam debitis corporis. Necessitatibus vel ab error sit ullam.</p>
    </div>
</template>

<script>
    export default {}
</script>

<style scoped>

    #jobPosting {
        width: 40%;
        height: 120px;
        display: grid;
        grid-template-rows: 30% 20% 50%;
        align-items: center;

        border-radius: 5px;
        overflow: hidden;
    }

    #title {
        background-color: #ffffff;
        color: #2a2a2f;
        height: 100%;
        text-align: left;
        padding-left: 5px;
    }

    #location {
        background-color: rgb(255, 255, 255);
        color: #3d3d43;
        height: 100%;
        text-align: left;
        padding-left: 5px;

    }

    #description {
        background-color: rgb(255, 255, 255);
        color: #2a2a2f;
        font-size: 10pt;
        height: 100%;
        text-align: left;
        padding-left: 5px;
    }

</style>