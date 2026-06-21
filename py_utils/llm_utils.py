from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

LLM_API_KEY = os.environ.get("LLM_API_KEY")
LLM_BASE_URL = os.environ.get("LLM_BASE_URL")
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4.1-mini")

if not LLM_API_KEY:
    raise ValueError("LLM_API_KEY is not set. Please set it in your .env file or environment variables.")

def llm(model, prompt, temperature):
    client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature
    )

    return response.choices[0].message.content

def llm_messages(model, messages, temperature):
    client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    prompt = """
    hi
    """
    print(llm("gpt-4o-mini-2024-07-18", prompt))