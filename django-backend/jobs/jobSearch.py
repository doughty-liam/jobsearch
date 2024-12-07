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

class jobPuller():

    def __init__(self):
        load_dotenv()
        
    
    def collect_jobs(self) -> list:
        """
        Query Google Jobs API and save results to a json array.

        Returns a list of dictionaries, each dict containing job listing information.
        """

        SERP_KEY = os.getenv("SERP")
        jobs = []

        for page in range(0, 10, 10):
            raw = re.get(f"https://serpapi.com/search.json?engine=google_jobs&q=new+grad&location=Toronto&lrad=200&api_key={SERP_KEY}")
            # Checking if no more search results were returned
            if "error" not in raw.json().keys():
                new = raw.json()["jobs_results"]
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
        
        jobs = pd.read_json("response.json")
        print(jobs.columns)
        # detected_extensions = jobs["detected_extensions"].apply(pd.Series) # Splitting json formatted column of objects into a pandas series
        apply_options = jobs["apply_options"].apply(pd.Series)

        application_links = []
        for job in jobs_clean["apply_options"]: # Each element is a list of objects
            link_found = False
            for option in job:
                j = dict(option)
                if j["title"] == "LinkedIn":
                    application_links.append(j["link"])
                    link_found = True
            if link_found == False:
                application_links.append("Unknown")
        
        
        apply_options = pd.Series(application_links, name="Link") # Converting "link" and "text" series back to df
        jobs_clean = pd.concat([jobs, apply_options], axis=1)
        jobs_clean = jobs_clean[["title", "company_name", "location", "description", "Link"]] # Select only required columns
        jobs_clean["date_added"] = dt.date(dt.now())
        jobs_clean["applied"] = False
        print(jobs_clean)
        return jobs_clean


    def find_similarity(self, text1:str, text2:str):

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([text1, text2])

        similarity = cosine_similarity(vectors)

        return similarity[0][1]


    def getJobs(self) -> None:
        
        engine = sqla.create_engine("sqlite:///db.sqlite3")
        connection = engine.connect()
        
        # jobs_jstr = self.collect_jobs()
        # jobs_df = self.clean(jobs_jstr)
        jobs_df = self.clean("maymay")

        '''
        descriptions = jobs_df[["description"]].to_numpy()
        temp = []

        
        for description in descriptions:
            temp.append(find_similarity(resume_text, description[0]))

        similarity_rating = pd.Series(temp)

        jobs_df.insert(6, "similarity_rating", similarity_rating)
        '''

        # jobs_df.to_sql("jobs_job", con=engine, index=False, if_exists="append")

        connection.close()
