import requests as re
from dotenv import load_dotenv
import os
import json
import pandas as pd
import sqlalchemy as sqla
from datetime import datetime as dt

load_dotenv()


def collect_jobs() -> list:
    """
    Query Google Jobs API and save results to a json array.

    Returns a list of dictionaries, each dict containing job listing information.
    """

    SERP_KEY = os.getenv("SERP")
    jobs = []

    for page in range(0, 100, 10):
        raw = re.get(f"https://serpapi.com/search.json?engine=google_jobs&q=intern+2024&location=Toronto%2C+Ontario%2C+Canada&google_domain=google.ca&gl=ca&hl=en&start={page}&chips=date_posted%3Aweek&lrad=200&api_key={SERP_KEY}")
        
        # Checking if no more search results were returned
        if "error" not in raw.json().keys():
            new = raw.json()["jobs_results"]
            jobs = jobs + new
        else:
            break
    
    return json.dumps(jobs)


# Utility function. Should modify to accept existing filename as an arg
def append_json(data:dict) -> None:
    """Append json object/file to an array of job listings stored in an existing .json file"""

    original = []
    with open("internships_S24.json", "r") as f:
       
        original = list(json.load(f))
        original.append(data)

    with open("internships_S24.json", "w") as f:
        json.dump(original, f)


def clean(data:str) -> pd.DataFrame:
    """Clean up job listings in json string format to be appended to database table."""
    
    jobs = pd.read_json(data)
    # jobs.drop(["extensions", "job_highlights", "thumbnail"], axis=1, inplace=True) # Removing unecessary columns
    detected_extensions = jobs["detected_extensions"].apply(pd.Series) # Splitting json formatted column of objects into a pandas series
    related_links = jobs["related_links"].apply(pd.Series)

    dict1 = [i for i in related_links[0].tolist()]
    dict2 = [i for i in related_links[1].tolist()]

    # If multiple "link" values are found in search result object, take only google jobs link.
    rel_links = []
    for i in range(len(dict1)):
        if not pd.isna(dict2[i]):
            rel_links.append(dict2[i])
        else:
            rel_links.append(dict1[i])
    
    related_links = pd.Series(rel_links).apply(pd.Series) # Converting "link" and "text" series back to df
    jobs_clean = (pd.concat([jobs.drop(["detected_extensions", "related_links"], axis=1), detected_extensions, related_links], axis=1)).astype(str) # Recombining all cols
    jobs_clean = jobs_clean[["title", "company_name", "location", "via", "description", "job_id", "posted_at", "schedule_type", "link", "text"]]
    jobs_clean["dateAdded"] = dt.date(dt.now())
    
    return jobs_clean
    

if __name__ == "__main__":

    engine = sqla.create_engine("sqlite:///data/internships_2024.db")
    connection = engine.connect()
    
    jobs_jstr = collect_jobs()
    jobs_df = clean(jobs_jstr)
    jobs_df.to_sql("internships", con=engine, index=False, if_exists="append")

    connection.close()
