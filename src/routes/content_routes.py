from flask import Blueprint
from src.controllers.content_controller import create_post, fetch_all_posts

content_routes = Blueprint("content_routes", __name__)

content_routes.route("/generate", methods=["POST"])(create_post)
content_routes.route("/history", methods=["GET"])(fetch_all_posts)
