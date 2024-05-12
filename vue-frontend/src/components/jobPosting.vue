<template>
    <div class="postingContainer">
        <li class="jobPosting">
            <h2 class="info" id="title">{{ title }}</h2>
            <div class="info" id="company">{{ company }}</div>
            <div class="info" id="location">{{ location }}</div>
        </li>
        <checkMark :applied=applied></checkMark>
        <!-- insert checkMark component -->
    </div>
</template>

<script>

import checkMark from './checkMark.vue'

export default {
    components: {
        checkMark
    },
    props: {
        title: {required: true, type: String},
        location: {required: true, type: String},
        company: {required: true, type: String},
        applied: {required: true, type: Boolean}
    }
}

</script>

<style scoped>

    .postingContainer {
        display: flex;
        background-color: #001D3D;
        color: #FFFFFF;
        border-radius: 8px;
        margin-bottom: 2px;
        transition: background-color 0.3s;
    }

    .postingContainer:hover {
        background-color: #19295e;
    }

    .jobPosting {
        width: 80%;
        height: 120px;
        display: grid;
        grid-template-rows: 40px 40px 40px;
        align-items: center;
        overflow: hidden;
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