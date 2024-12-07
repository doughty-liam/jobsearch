<template>
    <div class="postingContainer" :class="{expanded: isSelected}" @click="testFunc()">
        <li class="jobPosting" :class="{addDescToGrid: isSelected}">
            <h2 id="title" class="title info">{{ title }}</h2>
            <div class="company info">{{ company }}</div>
            <div class="location info">{{ location }}</div>
            <transition>
                <pre id="descriptionText" v-if="isSelected">{{ description }}</pre>
                <!-- <div class="description" :class="{displayDescription: isSelected}"> {{ description }}</div> -->
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
        description: {required: false, type: String}
    },

    setup() {
        
        var isSelected = ref(false)

        const testFunc = () => {

            if(isSelected.value == false) {
                isSelected.value = true
                console.log("Component was not active.")
            } else {
                isSelected.value = false
                console.log("Component was active.")
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
        background-color: #141819;
        /* color: rgb(247, 246, 237); */
        border-radius: 8px; 
        margin-bottom: 10px;
        height: 120px;
        transition: all 0.3s ease-in-out;
    }

    .postingContainer:hover {
        background-color: #1c1e29;
    }

    .expanded {
        height: 550px;
        background-color: #1c1e29;
    }

    .jobPosting {
        width: 90%;
        height: 120px;
        display: grid;
        grid-template-rows: 35% 32.5% 32.5%;
        align-items: center;
        overflow: hidden;
        transition: all 0.3s ease-in-out;
    }

    .addDescToGrid {
        grid-template-rows: 6% 6% 6% 78%;
        height: 550px;
    }

    #title {
        color: transparent;
        background: rgba(107, 107, 255, 0.774);
        background-clip: text;
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
        font-size: 18pt;
        height: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .location {
        color: rgba(243, 242, 229, 0.897);
        font-family: Barlow Regular;
        background-color: transparent;
        font-size: 14pt;
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