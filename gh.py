import string
from github import Github


def commit_blog_post(personal_access_token: str, topic: str, content: str) -> None:
    g = Github(personal_access_token)
    repo = g.get_repo("blairnangle/blairnangle-dot-com")
    subdir = topic.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '-')
    repo.create_file(
        path=f"./src/content/posts/generative/{subdir}/index.mdx",
        message=f"[RoboBlog] Create generative blog post: {topic}",
        content=content
    )
