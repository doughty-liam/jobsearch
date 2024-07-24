<template>
	<div id="mainContainer">
		<div id="listContainer">
			<ul v-for="job in jobs" :key="job.id" id="joblist">
				<jobPosting :title="job.title" :location="job.location" :company="job.companyName" :id="job.id" :applied="job.applied"
					v-on:click="updateJobDetails(job.id, job.title, job.companyName, job.location, job.description)">
				</jobPosting>
			</ul>
			<div id="resultsNav">
				<!-- This whole div should be its own component -->
				<button id="pageBack" class="pageNav" @click="nextPage(0)">&#8249;</button>
				<div id="pageNum">{{ pageNum }}</div>
				<button id="pageForward" class="pageNav" @click="nextPage(1)">&#8250;</button>
			</div>
		</div>
	</div>
</template>

<script>

import jobPosting from './components/jobPosting.vue'
/* import sortOptions from './components/sortOptions.vue'
import jobDetails from './components/jobDetails.vue'
import sortMenu from './components/sortMenu.vue' */
import { ref, watch } from 'vue'
import gql from 'graphql-tag'
import { provideApolloClient, useQuery } from '@vue/apollo-composable'
import client from './apollo-config'


export default {
	components: {
		jobPosting,
/* 		sortOptions,
		jobDetails,
		sortMenu */
	},

	setup() {
		const jobsPerPage = ref(20)
		const offset = ref(0)
		const pageNum = ref(1)
		const jobs = ref([])
		const selectedJob = ref({})


		provideApolloClient(client)
		const { result, fetchMore } = useQuery(gql`
			query getRankedJobs($first: Int, $skip: Int) {
				jobsBySimilarity(first: $first, skip: $skip) {
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
			if (newResult && newResult.jobsBySimilarity) {
				jobs.value = newResult.jobsBySimilarity
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
					
					jobs.value = fetchMoreResult.jobsBySimilarity
					console.log(jobs.value)

				}
			})

		}

		/* const updateJobDetails = (id, title, companyName, location, description) => {
			companyName = companyName + " | ";

			selectedJob.value = {
				id: id,
				title: title,
				company: companyName,
				location: location,
				description: description
			}

			const page_title = document.getElementById("page_title");
			const detailsContainer = document.getElementById("details");

			page_title.innerHTML = title;
			detailsContainer.style.visibility = "visible";
		} */

		return {
			jobs,
			offset,
			jobsPerPage,
			pageNum,
			nextPage,
			//updateJobDetails,
			selectedJob
		}
	}
}

</script>

<style>
#mainContainer {
	background-color: rgb(23, 24, 29);
	display: flex;
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	height: 100vh;
	width: 100%;
	margin: auto;
	justify-content: center;
}

#listContainer {
	height: 100vh;
	width: 40%;
	overflow-y: scroll;
}

#pageNum {
	height: 100%;
	width: 15%;
	text-align: center;
	line-height: 50px;
	font-size: 16pt;
	color: rgb(193, 193, 193);
}

.pageNav {
	background-color: transparent;
	color: rgb(193, 193, 193);
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

#joblist {
	margin: 0px;
	margin-left: 5px;
	padding: 0px;
}

</style>
