# Flask Tech Post Generator Backend

This is the backend for generating tech posts using either **GeminiAI** or **OpenAI**. The backend is built using **Flask** and connects to **MongoDB** to store and retrieve generated posts.

## Prerequisites

- Python 3.8+
- MongoDB Atlas account (or local MongoDB installation)
- API keys for **GeminiAI** and/or **OpenAI** (stored in `.env` file)

## Installation Guide

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/MdMirzaShihab/flaskTechPostGenBackend.git
cd flaskTechPostGenBackend
```

### 2. Set Up Virtual Environment
To keep dependencies isolated, it's recommended to use a virtual environment. You can create and activate it using the following commands:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Once the virtual environment is activated, install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root of the project (same level as `README.md`) and add the following environment variables:

```bash
MONGODB_ATLAS_URL=mongodb+srv://<your_mongo_user>:<your_mongo_password>@<cluster_url>/tech_posts?retryWrites=true&w=majority
OPENAI_API_KEY=your_openai_api_key
GEMINIAI_API_KEY=your_gemini_api_key
```
Make sure to replace the placeholders with your actual MongoDB credentials and API keys.

### 5. Run the Flask Application
To run the Flask application locally, use the following command:

```bash
python src/run.py
```
The server will start running locally at `http://127.0.0.1:3001`.

### 6. API Endpoints
POST /api/posts/generate: Create a new tech post using GeminiAI (or OpenAI by modifying the controller) ❗This endpoint is not currently working❗.
GET /api/posts/history: Retrieve all generated tech posts, sorted by the creation date. ✅ This endpoint is currently working ✅ .
### 7. Test the API
You can test the endpoints using tools like Postman or curl.

Example: Get Post History

```bash
curl http://127.0.0.1:3001/api/posts/history
```
