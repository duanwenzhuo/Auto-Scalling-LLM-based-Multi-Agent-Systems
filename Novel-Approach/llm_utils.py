import os

from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

load_dotenv()

selection = os.getenv("LLM_SELECTION")

if selection == "openai":
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        raise RuntimeError(
            "Missing OPENAI_API_KEY. Please set it in your environment or .env file."
        )

    client_options = {"api_key": openai_key}
    openai_base_url = os.getenv("OPENAI_BASE_URL")
    if openai_base_url:
        client_options["base_url"] = openai_base_url

    client = OpenAI(**client_options)
elif selection == "gemini":
    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        raise RuntimeError(
            "Missing GEMINI_API_KEY. Please set it in your environment or .env file."
        )

    client = OpenAI(
        api_key=gemini_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
else:
    client = None


def callLLM(messages):
    if client is None:
        raise RuntimeError(
            "LLM client is not configured. Please set LLM_SELECTION and the corresponding API key in .env."
        )

    try:
        if selection == "openai":
            response = client.chat.completions.create(
                messages=messages,
                model="gpt-4o",
                response_format={"type": "text"},
            )
        elif selection == "gemini":
            response = client.chat.completions.create(
                messages=messages,
                model="gemini-2.5-flash",
                response_format={"type": "text"},
            )
        else:
            raise RuntimeError(f"Unsupported LLM_SELECTION value: {selection}")

        content = response.choices[0].message.content.strip("'").strip('"')
        return content
    except OpenAIError as exc:  # includes HTTP/API errors like 401
        detail = getattr(exc, "response", None)
        if detail is not None and hasattr(detail, "status_code"):
            raise RuntimeError(f"LLM API error (status {detail.status_code}): {exc}") from exc
        raise RuntimeError(f"LLM API error: {exc}") from exc
