import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

myApi = os.getenv("GROQ_API_KEY")

if not myApi:
    raise ValueError("api key not found")

client = Groq(api_key=myApi)

message_system = {
    "role" : "system",
    "content" : "act like my strict manager who dont want me to waste time but i think she likes me "
}

message = {

    "role" : "user",
    "content" : "hi how are you"

}

model = "openai/gpt-oss-20b"

messages = [message_system , message]

response = client.chat.completions.create(model=model , messages=messages , temperature=2 )

print(response.choices[0].message.content)