from flask import jsonify
from src.config.db import mongo
from src.models.content_model import save_post, get_all_posts
from src.services.content_generator_gemini import generate_content_gemini
from src.utils.responses import success_response, error_response

def create_post():
    try:
        post_content = generate_content_gemini()  # Swap to OpenAI if needed
        if not post_content:
            return error_response("Content generation failed", 500)

        post_id = save_post(post_content)
        return success_response({"postContent": post_content, "_id": str(post_id)}, "Post created", 201)
    except Exception as e:
        return error_response(str(e), 500)

def fetch_all_posts():
    try:
        posts = get_all_posts()  # Get posts from 'contents' collection
        print("Fetched Posts: ", posts)  # Log the posts before returning
        posts_list = [
            {
                "_id": str(post["_id"]),
                "postContent": post["postContent"],
                "createdAt": post["createdAt"],
            }
            for post in posts
        ]
        print("Formatted Posts: ", posts_list)  # Log the formatted posts
        return success_response(posts_list, "Posts retrieved successfully")
    except Exception as e:
        print("Error fetching posts: ", str(e))  # Log any error
        return error_response(str(e))