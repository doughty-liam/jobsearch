<template> <!-- this not working, check if applied is bool or not -->
    <template v-if="applied==1"> <!-- show checkmark if applied -->
        <div id="appliedLabel">
            <div id="checkTop" class="checkMark"></div>
            <div id="checkBottom" class="checkMark"></div>
        </div>
    </template>
</template>

<script>

    export default {
        props: {
            applied: {required: true, type: Boolean}
        }
    }

</script>

<style>

    #appliedLabel {
        height: 50px;
        width: 50px;
        margin: auto;
        color: #ffffff;
    }

    #checkTop {
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 25px;
        height: 6px;

        transform: rotate(-50deg);
    }

    #checkBottom {
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 15px;
        height: 6px;

        transform: rotate(40deg) translateY(5px) translateX(-5px);
    }

    .checkMark {
        background-color: green;
    }

</style>