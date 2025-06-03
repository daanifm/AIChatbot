#src/config.py
from openai import OpenAI

def init_client():
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="OpenRouter ApiKey",
    )
    return client
