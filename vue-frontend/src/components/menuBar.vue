<template>
    <div>
        <div id="menubar">
            <div class="menu" id="left">Left</div>
            <div id="search_wrap">
                <input type="search" placeholder="Enter comma-separated keywords ..." v-model="keywordStr" class="menu" id="searchbar" v-on:input="emitNewKeywords($event)">
            </div>
            <div class="menu" id="right">Right</div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
            keywordStr: ""
            }
        },
        methods: {
            emitNewKeywords() {
                this.$emit("update-keywords", this.keywordStr)
            }
        }
    }
</script>

<style>

    #menubar {
        width: 100%;
        display: inline-flex;
        height: 100%;
        padding: 10px;
        
    }
    .menu {
        font-size: 14pt;
        margin: auto;
        color: white;
        font-family: Barlow Regular;
    }

    #search_wrap {
        display: flex;
        width: 20%;
        background-color: white;
        align-items: center;
        align-content: center;
        border-radius: 30px;
        transition: background-color 0.17s linear;
    }

    #search_wrap:focus-within {
        background-color: rgba(51, 81, 163, 0.219);
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

</style>