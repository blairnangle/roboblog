#!/usr/bin/env python3

import os
import random

import blog
import gh
import oai
import wn

author = random.choice([
    "Roddy Doyle",
    "Lady Gregory",
    "Seamus Heaney",
    "C. S. Lewis",
    "George Bernard Shaw",
    "Colm Tóibín",
    "Oscar Wilde",
    "W. B. Yeats",
])

model = "text-davinci-003"
word_of_the_day = wn.fetch_word_of_the_day(api_key=os.getenv("WORDNIK_API_KEY"))
print(f"word of the day: {word_of_the_day}")
prompt = f"Write a short story about {word_of_the_day} in the style of {author}"
print(f"prompt: {prompt}")
temperature = round(random.uniform(0, 1), 1)
topic = f"A short story about {word_of_the_day} in the style of {author}"
print(f"topic: {topic}")
openai_api_key = os.getenv("OPENAI_API_KEY")
body = oai.generate_completion(api_key=openai_api_key, model=model, prompt=prompt, temperature=temperature)
blog_post_content = blog.build_blog_post(topic=topic, prompt=prompt, body=body, model=model, temperature=temperature)
gh.commit_blog_post(personal_access_token=os.getenv("PERSONAL_ACCESS_TOKEN"), topic=topic, content=blog_post_content)
