import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv


load_dotenv()
myApi = os.getenv("GROQ_API_KEY")

if not myApi:
    raise ValueError("api key not found")

client = Groq(api_key= myApi)
prompt = "hi i am aditya"
role = "user"
model = "openai/gpt-oss-20b"

message = {

    "role":role,
    "content":prompt

}

messages = [message]

response = client.chat.completions.create(model=model , messages=messages)

print(response.choices[0].message.content)
