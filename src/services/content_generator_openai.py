import openai
from src.secret import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_content_openai():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Write a concise tech review within 300 chars."}
        ],
        max_tokens=75,
    )
    return response.choices[0].message['content'].strip()
