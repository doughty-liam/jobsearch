<template>
	<div id="main">
		<menuBar id="menu" @refresh="simpleRefresh()" @update-keywords="newKeywords" @selectQuery="filterQuery"></menuBar>
		<div class="filter-container">
			<!-- This should be its own filter-menu -->
			<div class="filter-menu">
				<a class="filter-option filter-shortlisted" style="margin-left: 10px;">shortlisted</a>
				<input type="checkbox" style="margin-left: 5px;" v-model="shortlisted">
				<a class="filter-option filter-applied" style="margin-left: 10px;">applied</a>
				<input type="checkbox" style="margin-left: 5px;" v-model="applied">
			</div>
		</div>
		<div id="listContainer">
			<div v-if="loading" class="loader"></div>
			<ul v-for="job in jobs" :key="job.id" id="joblist">
				<jobPosting @refresh="simpleRefresh()" :title="job.title" :location="job.location" :company="job.companyName" :id="job.id" :applied="job.applied"  :link="job.link" :description="job.description" :shortlisted="job.shortlisted">
				</jobPosting>
			</ul>
		</div>
		<div id="resultsNav">
			<!-- This whole div should be its own component -->
			<div id="pagenav-buttons">
				<button id="pageBack" class="pageNav" @click="nextPage(0)">&#8249;</button>
				<div id="pageNum">{{ pageNum }}</div>
				<button id="pageForward" class="pageNav" @click="nextPage(1)">&#8250;</button>
			</div>
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

/* TO DO
1. Double-check logic for refreshing with new keywords - ensure that page/offset params
   will be reset.
2. Fix animation when expanding a job.	
*/
export default {
	components: {
		jobPosting,
		menuBar
	},

	data() {
		return {
			shortlistedJobsQ: gql`
			query getShortlisted($first: Int, $skip: Int, $keywordStr: String){
				shortlistedJobs(first: $first , skip: $skip, keywordStr: $keywordStr ){
					id
					title
					companyName
					description
					applied
					link
					shortlisted
				}
			}`,
		}
	},

	setup() {
		const jobsPerPage = ref(20)
		const keywordStr = ref("")
		const offset = ref(0)
		const pageNum = ref(1)
		const jobs = ref([])
		const selectedJob = ref({})
		const shortlisted = ref(false)
		const applied = ref(false)

		const jobsQuery = ref(gql`
		query jobs($first: Int, $skip: Int, $filterParams: FilterParamsType){
			jobs(first: $first , skip: $skip, filterParams: $filterParams ){
				id
				title
				companyName
				location
				description
				applied
				link
				shortlisted
			}
		}`)

		provideApolloClient(client)
		const { result, fetchMore, loading, refetch } = useQuery(jobsQuery,
			{
				first: jobsPerPage.value,
				skip: offset.value,
				filterParams: {
					shortlisted: shortlisted,
					applied: applied,
					keywordStr: keywordStr
				}
			}
		)

		watch(result, (newResult) => {
			if (newResult && newResult.jobs) {
				jobs.value = newResult.jobs
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
					skip: offset.value,
					filterParams: {
						shortlisted: shortlisted.value,
						applied: applied.value,
						keywordStr: keywordStr.value
					}
				},
				updateQuery: (result, {fetchMoreResult}) => {
					if(!fetchMoreResult) return result
					
					jobs.value = fetchMoreResult.jobs
				}
			})

		}

		const newKeywords = async (keywords) => {
			offset.value = 0;
			pageNum.value = 1;
			keywordStr.value = keywords;

			refetch({
				first: jobsPerPage.value,
				skip: offset.value,
				filterParams: {
					shortlisted: shortlisted.value,
					applied: applied.value,
					keywordStr: keywordStr.value
				}
			})
		}

		const simpleRefresh = async () => {
			refetch({
				first: jobsPerPage.value,
				skip: offset.value,
				filterParams: {
					shortlisted: shortlisted.value,
					applied: applied.value,
					keywordStr: keywordStr.value
				}
			})
		}


		return {
			offset,
			jobs,
			jobsPerPage,
			pageNum,
			nextPage,
			keywordStr,
			applied,
			shortlisted,
			newKeywords,
			selectedJob,
			refetch,
			simpleRefresh,
			jobsQuery,
			loading
		}
	},
}

</script>

<style>

	@font-face {
		font-family: "Barlow Regular";
		src: url("../fonts/Barlow-Regular.ttf ");
	}

	#main {
		height: 100vh;
		width: 100vw;
	}

	#menu {
		position: absolute;
		top: 0;
		width: 100%;
		height: 5vh;
		min-height: 45px;
		max-height: 70px;
	}

	.filter-container {
		position: absolute;
		top: 5vh;
		height: 5vh;
		width: 100%;
		background-color: rgb(17 25 37);
		display: flex;
		align-items: center;
		text-align: center;
		justify-content: center;
	}

	.filter-option {
		height: 100%;
		font-family: 'Barlow Regular';
		font-size: 14pt;
		align-content: center;
		margin: auto;
		color: white;
	}

	#listContainer {
		position: absolute;
		display: flex;
		flex-direction: column;
		align-items: center;
		top: 10vh;
		height: 85vh;
		width: 100%;
		overflow-y: scroll;
		background-color: rgb(17 25 37);
	}
	
	.loader {
		border: 16px solid #f3f3f3; /* Light grey */
		border-top: 16px solid #226694; /* Blue */
		border-radius: 50%;
		margin: auto;
		width: 100px;
		height: 100px;
		animation: spin 1s linear infinite;
	}

	@keyframes spin {
		0% { transform: rotate(0deg); }
		100% { transform: rotate(360deg); }
	}

	#joblist {
		height: 80%;
		width: 40%;
		padding: 0;
		margin: auto;
		background-color:rgb(17 25 37);
	}


	#resultsNav {
		position: absolute;
		top: 95vh;
		height: 5vh;
		width: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: rgb(17 25 37);
	}

	#pagenav-buttons {
		width: 8%;
		height: 100%;
		display: inline-flex;
	}

	#pageNum {
		font-family: Barlow Regular;
		height: 100%;
		width: 30%;
		align-content: center;
		text-align: center;
		font-size: 18pt;
		line-height: 100%;
		color: rgb(217, 217, 217);
	}

	.pageNav {
		background-color: transparent;
		color: rgb(217, 217, 217);
		width: 40px;
		border: none;
		font-size: 30pt;
		height: 90%;
		
	}

	.pageNav:hover {
		transition-duration: 300ms;
		color: #0d5c87;
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
