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
import { computed } from 'vue'
import gql from 'graphql-tag'
import { provideApolloClient, useQuery } from '@vue/apollo-composable'
import client from './apollo-config'

export default {
	name: 'App',
	components: {
		jobPosting,
		sortOptions,
		sortMenu,
		jobDetails
	},
	data() {

		return {
			selectedJob: {},
			menuActive: false,
		}
	},

	methods: {
		updateJobDetails(id, title, companyName, location, description) {

			companyName = companyName + " | ";

			this.selectedJob = {
				id: id,
				title: title,
				company: companyName,
				location: location,
				description: description
			}

			const page_title = document.getElementById("page_title");
			const detailsContainer = document.getElementById("details");
			const postingViewed = document.getElementById(id);

			page_title.innerHTML = title;
			detailsContainer.style.visibility = "visible";
			postingViewed.style.backgroundColor = "#234A74"; // This not working :(

		},
		toggle() {

			/* handle event emitted by filter button press in
			sortOptions */

		}
	},

	setup() {

		provideApolloClient(client);

		/*
			Add in logic to display N number of jobs per page
			skip N*currPageNum
		
		const jobsPerPage
		const currPageNum
		*/
		const { result } = useQuery(gql`
			query {
				jobsBySimilarity(first:10, skip:0) {
				id
				title
				companyName
				location
				description
				applied
			}
			}
			`,
		);

		const jobs = computed(() => result.value?.jobsBySimilarity ?? []);
		return {
			jobs,
		}
	},
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
	background-color: #001d3d;
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
