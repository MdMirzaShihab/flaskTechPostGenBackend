from flask_pymongo import PyMongo
from src.secret import MONGODB_ATLAS_URL

mongo = PyMongo()

def init_db(app):
    app.config["MONGO_URI"] = MONGODB_ATLAS_URL
    print("Mongo URI:", app.config["MONGO_URI"])  # Log the URI to confirm it's correct
    mongo.init_app(app)