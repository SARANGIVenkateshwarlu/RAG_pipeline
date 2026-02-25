import os
import requests

#groq_api_key = os.environ("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"

payload = {
    "model": "openai/gpt-oss-120b",
    "messages": [{"role": "user", "content": "test"}],
    "max_tokens": 10,
}

headers = {
    "Authorization": f"Bearer {groq_api_key}",
    "Content-Type": "application/json",
}

r = requests.post(url, json=payload, headers=headers)
print(r.status_code, r.text)

