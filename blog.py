from datetime import datetime

def build_blog_post(topic: str, prompt: str, body: str, model: str, temperature: float) -> str:
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

    return front_matter + introduction + body + footer
