<template>
    <div class="postingContainer" :class="{expanded: isSelected}" @click="testFunc()">
        <li class="jobPosting" :class="{addDescToGrid: isSelected}">
            <h2 id="title" class="title info">{{ title }}</h2>
            <div class="company info">{{ company }}</div>
            <div class="location info">{{ location }}</div>
            <div class="job-actions">
                <button class="action-btn" >shortlist</button>
                <button class="action-btn" >applied</button>
                <button id="apply_link" class="action-btn" :href="link">apply</button>
            </div>
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
        line-height: 100%;
        align-content: center;
        padding-left: 10px;
        margin: 0;
    }

    .job-actions {
        width: 100%;
        display: flex;
        justify-content: flex-start;
        margin: auto;
    }

    .action-btn {
        margin-left: 10px;
        width: 100px;
        font-size: 14pt;
        font-family: Barlow Regular;
        color: #383f4d;
        background-color: #6b92b9;
        border-radius: 10px;
        border-color: transparent;
        transition: box-shadow 120ms ease-in-out, color 300ms ease-in-out;
    }

    .action-btn:hover {
        border-width: 0;
        box-shadow: inset 100px 0 0 0 rgb(8, 14, 49);
        box-sizing: border-box;
        color: white;
    }

</style>