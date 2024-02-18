<template>
    <li id="jobPosting">
        <h2 class="info" id="title">{{ title }}</h2>
        <div class="info" id="company">{{ company }}</div>
        <div class="info" id="location">{{ location }}</div>
    </li>
</template>

<script>
    export default {
        props: {
            title: {required: true, type: String},
            location: {required: true, type: String},
            company: {required: true, type: String}
        }
    }
</script>

<style scoped>

    #jobPosting {
        width: 100%;
        height: 120px;
        display: grid;
        grid-template-rows: 40px 40px 40px;
        align-items: center;
        background-color: #001D3D;
        margin-bottom: 2px;
        transition: background-color 0.3s;

        border-radius: 8px;
        overflow: hidden;
    }

    #jobPosting:hover {
        background-color: #19295e;
    }

    #title {
        background-color: transparent;
        font-size: 20pt;
        color: #e2d6be;
        height: 100%;
        text-align: left;
        padding-top: 1%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    #company {
        background-color: transparent;
        font-size: 18pt;
    }

    #location {
        background-color: transparent;
        font-size: 14pt;
    }

    .info {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #e2d6be;
        padding-left: 5px;
    }

</style>