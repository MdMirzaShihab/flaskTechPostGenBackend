from src.config.db import mongo
from datetime import datetime

def save_post(post_content):
    post = {"postContent": post_content, "createdAt": datetime.utcnow()}
    result = mongo.db.tech_posts.insert_one(post)
    return result.inserted_id

def get_all_posts():
    try:
        posts = mongo.db.contents.find().sort("createdAt", -1)  # Query from 'contents' collection
        posts_list = list(posts)
        print("Posts Retrieved: ", posts_list)  # Log the data received
        return posts_list
    except Exception as e:
        print("Error retrieving posts: ", str(e))  # Log any errors
        raise