<template>
    <div class="postingContainer" :class="{expanded: isSelected}" @click="testFunc()">
        <li class="jobPosting" :class="{addDescToGrid: isSelected}">
            <h2 class="title info">{{ title }}</h2>
            <div class="company info">{{ company }}</div>
            <div class="location info">{{ location }}</div>
            <transition>
                <div id="descriptionText" v-if="isSelected">{{ description }}</div>
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
        src: url("../../../fonts/Barlow-Regular.ttf ");
    }

    .postingContainer {
        width: 100%;
        display: flex;
        background-color: #1d2227;
        /* color: rgb(247, 246, 237); */
        border-radius: 8px; 
        margin-bottom: 10px;
        height: 120px;
        transition: all 0.4s ease-in-out;
    }

    .postingContainer:hover {
        background-color: #222c33;
    }

    .expanded {
        height: 550px;
        background-color: #222c33;
    }

    .jobPosting {
        width: 90%;
        height: 120px;
        display: grid;
        grid-template-rows: 40px 40px 40px;
        align-items: center;
        overflow: hidden;
        transition: all 0.4s ease-in-out;
        padding: 5px;
    }

    .addDescToGrid {
        grid-template-rows: 40px 40px 40px 415px;
        height: 550px;
    }

    .title {
        font-family: Barlow Regular;
        background-color: transparent;
        font-size: 20pt;
        color: rgb(247, 246, 237);
        height: 100%;
        text-align: left;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .company {
        font-family: Barlow Regular;
        background-color: transparent;
        font-size: 18pt;
        height: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .location {
        font-family: Barlow Regular;
        background-color: transparent;
        font-size: 14pt;
        height: 100%;
        text-overflow: ellipsis;

    }

    #descriptionText {
        font-family: Barlow Regular;
        font-size: 14pt;
        height: 100%;
        overflow-y: scroll;
        color: rgb(247, 246, 237);
        padding-left: 10px;
    }

    .v-enter-active,
    .v-leave-active {
        transition: all 0.4s ease;
    }

    .v-enter-from,
    .v-leave-to {
        opacity: 0;
    }

    /* .description {
        overflow: hidden;   
        background-color: transparent;
        font-family: Barlow Regular;
        padding-left: 10px;
        padding-top: 20px;
        overflow-y: auto;
    }

    .displayDescription {
        height: 100%;
        animation: changeDescColor 0.2s linear 1;
        color: rgb(247, 246, 237);
    }

    @keyframes changeDescColor {
        0% {
            color: transparent;
        }

        50% {
            color: linear-gradient(to bottom, transparent 50%, rgb(247, 246, 237) 50%)
        }

        100% {
            color: rgb(247, 246, 237);

        }
    } */

    .info {
        font-family: Barlow Regular;
        color: rgb(247, 246, 237);
        padding-left: 10px;
    }

</style>