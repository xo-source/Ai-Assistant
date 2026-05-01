
import requests
from config import USE_LOCAL, USE_API, MODEL_NAME


#LOCAL OLLAMA
def call_local(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


#OPEN AI API
def call_api(prompt):
    from openai import OpenAI
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


#FALLBACK
def call_mock(prompt):
    return "Mock mode: " + prompt[-80:]


#Model Router
def get_response(prompt):

    if USE_API:
        try:
            return call_api(prompt)
        except:
            return call_mock(prompt)

    if USE_LOCAL:
        try:
            return call_local(prompt)
        except:
            return call_mock(prompt)

    return call_mock(prompt)
