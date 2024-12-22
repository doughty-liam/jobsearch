<template>
    <div>
        <div id="menubar">
            <div class="menu-item" id="left"></div>
            <div class="menu-item" id="center">
                <div class="menu-item" id="search_wrap">
                    <input type="search" placeholder="Enter comma-separated keywords ..." v-model="keywordStr" class="menu-item" id="searchbar" v-on:input="emitNewKeywords($event)">
                </div>
            </div>
            <div id="right">
                <button class="menu-btn" id="get-more-btn" v-on:click="collectNewJobs()">get more</button>
                <button class="menu-btn" id="start-fresh-btn">start fresh</button>
            </div>    
        </div>
    </div>
</template>

<script>

    /* import { provideApolloClient, useQuery } from '@vue/apollo-composable';
    import client from "../apollo-config"
    import gql from 'graphql-tag'; */

    export default {
        data() {
            return {
            keywordStr: ""
            }
        },
        methods: {
            emitNewKeywords() {
                this.$emit("update-keywords", this.keywordStr)
            },

            collectNewJobs() {
                /* const q = gql`query collectNewJobs {
                    getNewJobs
                }`;
                provideApolloClient(client);

                const {result} = useQuery(q);
                console.log(result); */
                console.log("Get new jobs clicked.")

            }
        }
    }
</script>

<style>

    #menubar {
        width: 100%;
        display: grid;
        grid-template-columns: 33% 33% 33%;
        height: 100%;
        padding-bottom: 10px;
        padding-top: 10px;
        background-color: green;
        
    }

    .menu-item {
        font-size: 14pt;
        margin: auto;
        color: white;
        font-family: Barlow Regular;
        width: 100%;
        height: 100%;
    }

    .menu-btn {
        height: 40px;
        width: 130px;
        font-size: 14pt;
        color: white;
        font-family: Barlow Regular;
        margin-left: 10px;
        text-align: center;
        align-content: center;
        border-radius: 20px;
        border-color: transparent;
        background-color: #2e2e60;
        
    }

    .menu-btn:hover {
        background-color: #000f935e;
    }

    #right {
        display: flex;
        justify-content: flex-end;
    }

    #search_wrap {
        display: flex;
        width: 100%;
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
        padding: auto;
        background-color: transparent;
        color: black;
        border: 0;
        font-size: 18pt;
    }

    #searchbar:focus {
        outline: none;
    }

    #get-more-btn {
        color: white;
    }

    #start-fresh-btn {
        color: white;
    }
</style>