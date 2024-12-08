<template>
	<div id="mainContainer">
		<menuBar id="menu"></menuBar>
		<div id="listContainer">
			<ul v-for="job in jobs" :key="job.id" id="joblist">
				<jobPosting :title="job.title" :location="job.location" :company="job.companyName" :id="job.id" :applied="job.applied" :description="job.description">
				</jobPosting>
			</ul>
		</div>
		<div id="resultsNav">
				<!-- This whole div should be its own component -->
				<button id="pageBack" class="pageNav" @click="nextPage(0)">&#8249;</button>
				<div id="pageNum">{{ pageNum }}</div>
				<button id="pageForward" class="pageNav" @click="nextPage(1)">&#8250;</button>
		</div>
	</div>
</template>

<script>

import jobPosting from './components/jobPosting.vue'
import menuBar from './components/menuBar.vue'
import { ref, watch } from 'vue'
import gql from 'graphql-tag'
import { provideApolloClient, useQuery } from '@vue/apollo-composable'
import client from './apollo-config'


export default {
	components: {
		jobPosting,
		menuBar
	},

	setup() {
		const jobsPerPage = ref(20)
		const offset = ref(0)
		const pageNum = ref(1)
		const jobs = ref([])
		const selectedJob = ref({})


		provideApolloClient(client)
		const { result, fetchMore } = useQuery(gql`
			query getAllJobs($first: Int, $skip: Int){
				allJobs(first: $first , skip: $skip){
					id
					title
					companyName
					location
					description
					applied
				}
			}`,
			{
				first: jobsPerPage.value,
				skip: offset.value
			}
		)

		watch(result, (newResult) => {
			if (newResult && newResult.allJobs) {
				jobs.value = newResult.allJobs
				console.log(jobs.value)
			}
		})

		const nextPage = async (direction) => {	
			
			if (direction == 1) {
				offset.value += jobsPerPage.value
				pageNum.value += 1
			} else {
				if(offset.value < jobsPerPage.value) {
					offset.value = 0
				} else {
					offset.value -= jobsPerPage.value
					pageNum.value -= 1
				}
			}
			fetchMore({
				variables: {
					skip: offset.value
				},
				updateQuery: (result, {fetchMoreResult}) => {
					if(!fetchMoreResult) return result
					
					jobs.value = fetchMoreResult.allJobs
					console.log(jobs.value)

				}
			})

		}


		return {
			jobs,
			offset,
			jobsPerPage,
			pageNum,
			nextPage,
			selectedJob
		}
	}
}

</script>

<style>
#mainContainer {
	background-color: #0e0e0e;
	display: flex;
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	height: 100vh;
	width: 100%;
	margin: auto;
	justify-content: center;
	align-items: center;
}

#menu {
	position: absolute;
	top: 0;
	width: 100%;
}

#listContainer {
	padding-top: 10px;
	height: calc(100vh - 100px);
	width: 40%;
	overflow-y: scroll;
}

#joblist {
	margin: 0px;
	padding: 0px;
}

#pageNum {
	height: 100%;
	width: 5%;
	text-align: center;
	line-height: 50px;
	font-size: 16pt;
	color: rgb(217, 217, 217);
}

.pageNav {
	background-color: transparent;
	color: rgb(217, 217, 217);
	width: 40px;
	border: none;
	font-size: 30pt;
	height: 100%;
	margin-bottom: 5px;
	
}

.pageNav:hover {
	transition-duration: 300ms;
	color: #0d5c87;
}

#resultsNav {
	position: absolute;
	bottom: 0px;
	height: 50px;
	width: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
}

input::-webkit-inner-spin-button,
input::-webkit-outer-spin-button {
	-webkit-appearance: none;
	margin: 0;
}

::-webkit-scrollbar {
	width: 0px;
	background: transparent;
}

</style>
