# parser that i used for dataset 
# write by efe in 2026 
# i probably die alone in my bedroom

import requests
import jsonlines
import time

board = ["sci", "gd", "ai", "pr", "ra", "psy", "sci"]
output = "dataset_2ch_ai.jsonl"

def parse_thread(board, thread_id):
    url = f"https://2ch.hk/{board}/res/{thread_id}.json"
    r = requests.get(url)
    data = r.json()
    posts = []
    for post in data["threads"][0]["posts"]:
        text = post.get("comment", "")
        if text and len(text) > 20:
            posts.append(text)
    return posts

with jsonlines.open(output, "w") as writer:
    for board in board:
        catalog_url = f"https://2ch.hk/{board}/catalog.json"
        catalog = requests.get(catalog_url).json()
        for thread in catalog["threads"][:100]:
            thread_id = thread["num"]
            try:
                posts = parse_thread(board, thread_id)
                for p in posts:
                    writer.write({"text": p})
                print(f"{board}/{thread_id}: {len(posts)} posts")
            except Exception as e:
                print(f"Error {board}/{thread_id}: {e}")
            time.sleep(1)

