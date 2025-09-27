import os
from datetime import datetime
import re


def extract_post_date(post: str) -> datetime.date:
    match = re.search(r"(\d{2})-(\d{2})-(\d{4})\.md$", post)
    if match:
        day, month, year = match.groups()
        return datetime(int(year), int(month), int(day))

    return datetime.min


def extract_post_title(post: str) -> str:
    return " ".join(post.split("_")[0].split("-"))


def find_newest_posts(path: str, limit: int = 3) -> list[int]:
    posts = []
    if os.path.exists(path):
        posts = os.listdir(path)

        if len(posts):
            posts = sorted(
                posts,
                key=extract_post_date,
                reverse=True
            )[: limit]

    return posts

