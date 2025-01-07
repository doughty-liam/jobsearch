import requests as re
from dotenv import load_dotenv
import os
import json
import pandas as pd
import sqlalchemy as sqla
from datetime import datetime as dt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class JobPuller():

    def __init__(self):
        load_dotenv()
        
    
    '''
    TO DO
    - Add parameter to be used for the search query
    - Replace spaces in query with '+'
    - Add new query parameters into API connection string

    FRONT END: Add input field for this and button to run getJobs()
    '''

    def collect_jobs(self) -> list:
        """
        Query Google Jobs API and save results to a json array.

        Returns a list of dictionaries, each dict containing job listing information.
        """

        SERP_KEY = os.getenv("SERP")
        jobs = []
        next_page_token = ""

        for page in range(0, 150, 10):
            raw = re.get(f"https://serpapi.com/search.json?engine=google_jobs&q=analyst&location=Toronto&lrad=200&uds=ADvngMjcH0KdF7qGWtwTBrP0nt7d-93B-GLP_EZaqE4a9Xz_M8SJih1fftEvjbhMENwwVd5tsAkcnjKc9b8aleTghZdybJ0LnSFyBQoGQjjxkxT97QLf0SAMA8pbHPeSlqDU4C-vBgGVZFwoFIFRkT9xOVCWY7wt1GIcTpahI-LOapkDA18Bw0WGBkCCcl_3F6tuQYsB8osTWyL9msBSuTbQzcGoqhN-4nF_jv9Xt7D5Zzw6iIulf0bzumFiEB5721oxKDL336rL3StBEjPsP6MYt_KtqSPse7xAGnfu4SaymEzmqqH_ONO402sH5Iba_KEsdiLUsgOp&api_key={SERP_KEY}{next_page_token}")
            # Checking if no more search results were returned
            if "error" not in raw.json().keys():
                results = raw.json()
                new = results["jobs_results"]
                if "serpapi_pagination" in results.keys():
                    next_page_token = "&next_page_token=" + results["serpapi_pagination"]["next_page_token"]
                jobs = jobs + new
            else:
                break

        return json.dumps(jobs)


    # Utility function. Should modify to accept existing filename as an arg
    def append_json(self, data:dict) -> None:
        """Append json object/file to an array of job listings stored in an existing .json file"""

        original = []
        with open("internships_S24.json", "r") as f:
        
            original = list(json.load(f))
            original.append(data)

        with open("internships_S24.json", "w") as f:
            json.dump(original, f)


    def clean(self, data:str) -> pd.DataFrame:
        """Clean up job listings in json string format to be appended to database table."""
        
        jobs = pd.read_json(data)   
        if("apply_options" in jobs.keys()):     
            apply_options = jobs["apply_options"].apply(pd.Series)

        application_links = []

        for job in jobs["apply_options"]: # Each element is a list of objects
            link_found = False
            for option in job:
                j = dict(option) # Convert json string to dict
                if j["title"] == "LinkedIn":
                    application_links.append(j["link"])
                    link_found = True
            if link_found == False:
                if len(job) > 0:
                    application_links.append(dict(job[0])["link"])
                else:
                    application_links.append("Unknown") # No external link provided
        
        
        apply_options = pd.Series(application_links, name="link") # Converting "link" and "text" series back to df
        jobs_clean = pd.concat([jobs, apply_options], axis=1)
        jobs_clean = jobs_clean[["title", "company_name", "location", "description", "link"]] # Select only required columns
        jobs_clean["date_added"] = dt.date(dt.now())
        jobs_clean["shortlisted"] = False
        jobs_clean["applied"] = False
        return jobs_clean


    def find_similarity(self, text1:str, text2:str):

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([text1, text2])

        similarity = cosine_similarity(vectors)

        return similarity[0][1]


    def getJobs(self) -> None:
        
        engine = sqla.create_engine("sqlite:///db.sqlite3")
        connection = engine.connect()
        
        jobs_jstr = self.collect_jobs()

        jobs_df = self.clean(jobs_jstr)
        jobs_df.to_sql("jobs_job", con=engine, index=False, if_exists="append")

        connection.close()
