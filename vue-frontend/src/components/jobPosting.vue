<template>
    <li id="jobPosting">
        <h2 id="title">{{ title }}</h2>
        <h5 id="location">{{ location }}</h5>
        <p id="description">{{ description }}</p>
    </li>
</template>

<script>
    export default {
        props: {
            title: {required: true, type: String},
            location: {required: true, type: String},
            description: {required: true, type: String}
        }
    }
</script>

<style scoped>

    #jobPosting {
        width: 100%;
        height: 120px;
        display: grid;
        grid-template-rows: 30% 20% 50%;
        align-items: center;
        background-color: #ffffff;

        border-radius: 8px;
        overflow: hidden;
    }

    #jobPosting:hover {
        background-color: #eaeaea;
    }

    #title {
        background-color: transparent;
        color: #2a2a2f;
        height: 100%;
        text-align: left;
        padding-left: 5px;
        padding-top: 1%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    #location {
        background-color: transparent;
        color: #2a2a2f;
        height: 100%;
        text-align: left;
        padding-left: 5px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        margin-top: 16px;
    }

    #description {
        background-color: transparent;
        color: #3d3d43;
        font-size: 10pt;
        height: 100%;
        text-align: left;
        padding-left: 5px;
        overflow: hidden;
        margin-bottom: 30px;
        padding-bottom: 2px;
    }

</style>