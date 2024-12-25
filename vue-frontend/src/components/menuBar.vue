<template>
    <div>
        <div id="menubar">
            <div id="left">
                <div id="query-select-container">
                    <label class="global-text" id="query-select-label">query select</label>
                    <font-awesome-icon icon="magnifying-glass" color="white" size="xl"/>
                </div>
                <!-- <input type="checkbox" id="check">
                <label for="check" class="checkbtn">
                </label>
                <div class="nav-mobile">
                    <a href="#">Home</a>
                    <a href="#">About</a>
                    <a href="#">Services</a>
                    <a href="#">Contact</a>
                </div> -->
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

#query-select-container {
    height: 75%;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    margin-left: 2%;
    color: white;
    background-color: #203643;
    border-radius: 20px;
    padding-left: 10px;
    padding-right: 10px;
}

#query-select-label {
    margin-right: 10px;
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

nav {
 padding: 1.5rem 2rem;
 background-color: #222831;
 color: #fff;
}

.checkbtn {
 font-size: 1.5rem;
 color: white;
 cursor: pointer;
}

.nav-mobile {
 display: none;
}

#check:checked ~ .nav-mobile {
 display: block;
}

.nav-mobile {
 position: absolute;
 top: 4.5rem;
 left: 0;
 background: #222831;
 z-index: 1;
 width: 200px;
}
.nav-mobile a {
 color: #fff;
 padding: 1rem 1.5rem;
 display: block;
}
</style>