<template>
	<div id="main">
		<menuBar id="menu" @update-keywords="newKeywords" @selectQuery="newQuerySelected"></menuBar>
		<div id="listContainer">
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
			query getShortlisted($first: Int, $skip: Int, $keywordSet: String){
				shortlistedJobs(first: $first , skip: $skip, keywordSet: $keywordSet ){
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
		const keywordSet = ref("")
		const offset = ref(0)
		const pageNum = ref(1)
		const jobs = ref([])
		const selectedJob = ref({})

		const allJobsQ = ref(gql`
		query getJobs($first: Int, $skip: Int, $keywordSet: String){
			jobsByDateAdded(first: $first , skip: $skip, keywordSet: $keywordSet ){
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
		const { result, fetchMore, refetch } = useQuery(allJobsQ,
			{
				first: jobsPerPage.value,
				skip: offset.value,
				keywordSet: keywordSet.value
			}
		)

		watch(result, (newResult) => {
			if (newResult && newResult.jobsByDateAdded) {
				jobs.value = newResult.jobsByDateAdded
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
					
					jobs.value = fetchMoreResult.jobsByDateAdded
				}
			})

		}

		const newKeywords = async (keywords) => {
			offset.value = 0;
			pageNum.value = 1;
			keywordSet.value = keywords;
			refetch({
				first: jobsPerPage.value,
				skip: offset.value,
				keywordSet: keywordSet.value
			})
		}

		const simpleRefresh = async () => {
			refetch({
				first: jobsPerPage.value,
				skip: offset.value,
				keywordSet: keywordSet.value
			})
		}


		return {
			offset,
			jobs,
			jobsPerPage,
			pageNum,
			nextPage,
			newKeywords,
			selectedJob,
			refetch,
			simpleRefresh,
			allJobsQ
		}
	},

	methods: {
		newQuerySelected(qname) {	

			if(qname == "all") {
				const {result, loading} = useQuery(this.allJobsQ, {
						first: this.jobsPerPage,
						skip: this.offset,
						keywordSet: ""
					}
				)
				if(!loading) {
					console.log(result)
				}
			} else if(qname == "shortlisted") {

				const {result} = useQuery(this.shortlistedJobsQ, {
						first: this.jobsPerPage,
						skip: this.offset,
						keywordSet: ""
					}
				)

				console.log(result)
				// this.jobs = result.shortlistedJobs
				// console.log(this.jobs)

			} else if(qname == "applied") {
				console.log("Fetching applied jobs")
			}

		}
	}
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
		height: 8%;
	}

	#listContainer {
		position: absolute;
		top: 8%;
		height: 86%;
		width: 100%;
		overflow-y: scroll;
		background-color: rgb(17 25 37);
	}

	#joblist {
		width: 40%;
		padding: 0;
		margin: auto;
		background-color:rgb(17 25 37);
	}


	#resultsNav {
		position: absolute;
		top: 94%;
		height: 6%;
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
		margin: auto;
		align-content: center;
		padding-top: 2%;
		text-align: center;
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
