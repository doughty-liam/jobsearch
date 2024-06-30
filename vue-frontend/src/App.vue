<template>
	<div id="mainContainer">
		<div id="optionsBar">
			<sortOptions></sortOptions>
		</div>
		<sortMenu id="sortMenu"></sortMenu>
		<div id="main">
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
			<div id="details">
				<jobDetails :key="selectedJob.id" :title="selectedJob.title" :companyName="selectedJob.company"
					:location="selectedJob.location" :description="selectedJob.description"></jobDetails>
			</div>
		</div>
	</div>
</template>

<script>

import jobPosting from './components/jobPosting.vue'
import sortOptions from './components/sortOptions.vue'
import jobDetails from './components/jobDetails.vue'
import sortMenu from './components/sortMenu.vue'
import { ref, watch } from 'vue'
import gql from 'graphql-tag'
import { provideApolloClient, useQuery } from '@vue/apollo-composable'
import client from './apollo-config'


export default {
	components: {
		jobPosting,
		sortOptions,
		jobDetails,
		sortMenu
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

		const updateJobDetails = (id, title, companyName, location, description) => {
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
		}

		return {
			jobs,
			offset,
			jobsPerPage,
			pageNum,
			nextPage,
			updateJobDetails,
			selectedJob
		}
	}
}

</script>

<style>
#mainContainer {
	display: flex;
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
}

#main {
	width: 100%;
}

#optionsBar {
	background-color: #103047;
	display: flex;
	position: absolute;
	width: 100%;
	height: 55px;
	top: 0px;
	left: 0px;
}

#sortMenu {
	position: absolute;
	left: 50px;
	top: 60px;
	visibility: hidden;
}

#main {
	margin-top: 60px;
	display: grid;
	grid-template-columns: 30% 70%;
}

#listContainer {
	height: calc(100vh - 65px);
	width: 100%;
	overflow-y: scroll;
	background-color: rgb(247, 246, 237);
}

#pageNum {
	height: 100%;
	width: 15%;
	text-align: center;
	line-height: 50px;
	font-size: 16pt;
}

.pageNav {
	background-color: transparent;
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
	background-color: rgb(247, 246, 237);
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

#details {
	width: 100%;
	visibility: hidden;
}
</style>
