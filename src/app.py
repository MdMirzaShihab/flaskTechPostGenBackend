from flask import Flask
from src.config.db import init_db
from src.routes.content_routes import content_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173", "https://technews.mirzashihab.com"])

    init_db(app)
    app.register_blueprint(content_routes, url_prefix="/api/posts")

    @app.route("/")
    def home():
        return {"message": "Welcome to TechPostGen API Server"}

    return app
