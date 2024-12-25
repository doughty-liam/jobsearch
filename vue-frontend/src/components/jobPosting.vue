<template>
    <div class="postingContainer" :class="{expanded: isSelected}" @click="testFunc()">
        <li class="jobPosting" :class="{addDescToGrid: isSelected}">
            <h2 id="title" class="title info">{{ title }}</h2>
            <div class="company info">{{ company }}</div>
            <div class="location info">{{ location }}</div>
            <a id="apply_link" class="info" :href="link">Apply</a>

            <transition>
                <pre id="descriptionText" v-if="isSelected">{{ description }}</pre>
            </transition>
        </li>
        <checkMark :applied=applied></checkMark>
        <!-- insert checkMark component -->
    </div>
</template>

<script>

import checkMark from './checkMark.vue'
import {ref} from 'vue'

export default {
    
    components: {
        checkMark
    },
    props: {
        title: {required: true, type: String},
        location: {required: true, type: String},
        company: {required: true, type: String},
        applied: {required: true, type: Boolean},
        description: {required: false, type: String},
        link: {required: false, type: String}
    },

    setup() {
        
        var isSelected = ref(false)

        const testFunc = () => {

            if(isSelected.value == false) {
                isSelected.value = true
            } else {
                isSelected.value = false
            }
        }

        return {
            testFunc,
            isSelected
        }
    }
}

</script>

<style scoped>

    @font-face {
        font-family: "Barlow Regular";
        src: url("../../fonts/Barlow-Regular.ttf ");
    }

    .postingContainer {
        width: 100%;
        display: flex;
        background-color: #203643;
        border-radius: 8px;
        padding: 0;
        margin-bottom: 10px;
        height: 120px;
        transition: all 0.15s ease-in-out;
    }

    .postingContainer:hover {
        background-color: #1d2734;
    }

    .expanded {
        height: 550px;
        background-color: #1d2734;
    }

    .jobPosting {
        width: 100%;
        height: 120px;
        display: grid;
        grid-template-rows: 35% 32.5% 32.5%;
        align-items: center;
        overflow: hidden;
        transition: all 0.3s ease-in-out;
    }

    .addDescToGrid {
        grid-template-rows: 6% 6% 6% 6% 78%;
        height: 550px;
    }

    #title {
        color: transparent;
        background: rgba(243, 242, 229, 0.897);
        background-clip: text;
    }

    #apply_link {
        font-family: Barlow Regular;
        color: rgba(243, 242, 229, 0.897);
        height: 100%;
        margin-left: 0;
        width: fit-content;
        text-align: left;
        text-decoration: none;
        font-size: 15pt;
        padding: none;
        transition: ease-in-out 0.3s;
    }

    #apply_link:hover {
        font-size: 16pt;
        color: rgba(107, 107, 255, 0.774);
    }

    .title {
        font-family: Barlow Regular;
        font-size: 20pt;
        height: 100%;
        text-align: left;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .company {
        color: rgba(243, 242, 229, 0.897);
        font-family: Barlow Regular;
        background-color: transparent;
        font-size: 15pt;
        height: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .location {
        color: rgba(243, 242, 229, 0.897);
        font-family: Barlow Regular;
        background-color: transparent;
        font-size: 15pt;
        height: 100%;
        margin: auto;
        text-overflow: ellipsis;

    }

    #descriptionText {
        font-family: Barlow Regular;
        font-size: 14pt;
        height: 100%;
        line-height: 22px;
        overflow: auto;
        text-wrap: wrap;
        color: rgba(243, 242, 229, 0.897);
        padding-left: 10px;
        margin: 0px;
        transform: translate(0px, 15px);
    }

    .v-enter-active,
    .v-leave-active {
        transition: all 0.3s ease-in-out;
    }

    .v-enter-from,
    .v-leave-to {
        opacity: 0;
    }

    .info {
        font-family: Barlow Regular;
        padding-left: 10px;
        margin: 0;
    }

</style>