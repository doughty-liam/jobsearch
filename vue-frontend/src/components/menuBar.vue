<template>
    <div>
        <div id="menubar">
            <div id="left">
                <div id="title">
                    <font-awesome-icon icon="briefcase" style="padding-right: 15px; color: rgb(81, 130, 155)"/>
                    job finder
                </div>
            </div>
            <div id="center">
                <div class="menu-item" id="search_wrap">
                    <input type="search" placeholder="Enter comma-separated keywords ..." v-model="keywordStr"
                        class="menu-item" id="searchbar" v-on:input="emitNewKeywords($event)">
                </div>
            </div>
            <div id="right">
                <div class="menu-item" id="menu-options-container">
                    <button class="menu-btn" id="get-more-btn" v-on:click="collectNewJobs()">get more</button>
                    <button class="menu-btn" id="start-fresh-btn">start fresh</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import { provideApolloClient, useQuery } from '@vue/apollo-composable';
import client from "../apollo-config"
import gql from 'graphql-tag';

export default {
    data() {
        return {
            keywordStr: "",
            querySelectOpen: false
        }
    },
    methods: {
        emitNewKeywords() {
            this.$emit("update-keywords", this.keywordStr)
        },

        collectNewJobs() {
            const q = gql`query collectNewJobs {
                getNewJobs
            }`;
            provideApolloClient(client);

            const {result} = useQuery(q);
            console.log(result);

        }
    }
}
</script>

<style>
#menubar {
    width: 100%;
    display: grid;
    grid-template-columns: 33.33% 33.33% 33.33%;
    height: 100%;
    background-color: rgb(17 25 37);

}

.menu-item {
    width: 100%;
    height: 100%;
    font-size: 14pt;
    color: white;
    font-family: Barlow Regular;
}

.menu-btn {
    height: 75%;
    width: 130px;
    font-size: 14pt;
    color: white;
    font-family: Barlow Regular;
    margin-top: auto;
    margin-bottom: auto;
    margin-right: 15px;
    text-align: center;
    align-content: center;
    border-radius: 20px;
    border-color: transparent;
    background-color: #203643;
    transition: 0.15s ease-in-out;

}

.menu-btn:hover {
    background-color: #1d2734;
}

#left {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: flex-start;
    justify-items: center;
    align-items: center;
}

#right {
    display: flex;
    margin: auto;
    height: 100%;
    width: 100%;
}

#center {
    display: flex;
    width: 100%;
    height: 100%;
    margin: auto;
    align-items: center;
}

#title {
    padding-left: 15px;
    color: white;
    font-size: 28pt;
    font-family: 'Barlow Regular';
}

#search_wrap {
    width: 80%;
    height: 70%;
    margin: auto;
    background-color: white;
    align-items: center;
    align-content: center;
    border-radius: 30px;
    transition: background-color 0.17s linear;
}

#search_wrap:focus-within {
    background-color: rgb(255, 255, 255);
}

#searchbar {
    width: 95%;
    height: 90%;
    margin: auto;
    padding-left: 6px;
    padding-right: 6px;
    background-color: transparent;
    color: black;
    border: 0;
}

#searchbar:focus {
    outline: none;
}

#menu-options-container {
    display: flex;
    justify-content: flex-end;
    width: 100%;
}

#get-more-btn {
    color: white;
}

#start-fresh-btn {
    color: white;
}

</style>