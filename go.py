#!/usr/bin/env python3

import os
import random
import string
from datetime import datetime
import math
import requests
import openai
from github import Github

state = random.choice(["Alabama",
                       "Alaska",
                       "Arizona",
                       "Arkansas",
                       "California",
                       "Colorado",
                       "Connecticut",
                       "Delaware",
                       "Florida",
                       "Georgia",
                       "Hawaii",
                       "Idaho",
                       "Illinois",
                       "Indiana",
                       "Iowa",
                       "Kansas",
                       "Kentucky",
                       "Louisiana",
                       "Maine",
                       "Maryland",
                       "Massachusetts",
                       "Michigan",
                       "Minnesota",
                       "Mississippi",
                       "Missouri",
                       "Montana",
                       "Nebraska",
                       "Nevada",
                       "New Hampshire",
                       "New Jersey",
                       "New Mexico",
                       "New York",
                       "North Carolina",
                       "North Dakota",
                       "Ohio",
                       "Oklahoma",
                       "Oregon",
                       "Pennsylvania",
                       # "Rhode Island",
                       "South Carolina",
                       "South Dakota",
                       "Tennessee",
                       "Texas",
                       "Utah",
                       # "Vermont",
                       "Virginia",
                       "Washington",
                       # "West Virginia",
                       "Wisconsin",
                       # "Wyoming"
                       ])

city_data = requests.request(method="GET", url=f"https://data.opendatasoft.com/api/records/1.0/search/?dataset=us-cities-demographics%40public&q=&facet=city&facet=state&refine%2Estate={state}").json()["records"][math.floor(random.uniform(0, 5))]["fields"]
city = city_data["city"]

openai.api_key = os.getenv("OPENAI_API_KEY")
# model = random.choice([model["id"] for model in openai.Model.list()["data"]])
model = "text-davinci-002"
topic = f"{city}, {state}"
tone = random.choice([
    "satirical", "downbeat", "humorous", "passive-aggressive", "biased", "historical"
])
prompt = f"Write a {tone} blog post about {topic} in complete sentences"
temperature = round(random.uniform(0, 1), 1)
body = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    max_tokens=1000,
    temperature=temperature
)["choices"][0]["text"].strip() + "\n"

front_matter = f"""---
title: "RoboBlog: {topic}"
date: "{str(datetime.today().strftime("%Y-%m-%d"))}"
publish: true
excerpt: "{body[:50]}…"
postType: "generative"
---
#
"""

introduction = f"""
***{prompt}***

"""

footer = f"""
---
**Written using [Open AI](https://openai.com/)'s `{model}` model with a temperature of {str(temperature)}.**
"""

github_personal_access_token = os.getenv("PERSONAL_ACCESS_TOKEN")
g = Github(github_personal_access_token)
repo = g.get_repo("blairnangle/blairnangle-dot-com")
subdir = topic.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '-')
repo.create_file(
    path=f"./src/content/posts/generative/{subdir}/index.mdx",
    message=f"[RoboBlog] Create generative blog post about {topic}",
    content=front_matter + introduction + body + footer
)
