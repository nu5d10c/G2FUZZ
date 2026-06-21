from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# OPENAI_API_KEY and OPENAI_BASE_URL are standard env vars recognized by
# the OpenAI SDK and OpenAI-compatible services.
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4.1-mini")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is not set. "
        "Please set it in your .env file or environment variables."
    )


def _create_client():
    """Create an OpenAI client using standard environment variables."""
    kwargs = {}
    if OPENAI_BASE_URL:
        kwargs["base_url"] = OPENAI_BASE_URL
    return OpenAI(api_key=OPENAI_API_KEY, **kwargs)


def llm(model, prompt, temperature):
    client = _create_client()

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
    client = _create_client()
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