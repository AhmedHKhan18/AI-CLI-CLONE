from dotenv import load_dotenv, find_dotenv, set_key
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()

def ensure_api_key():
    dotenv_path = find_dotenv() or ".env"
    load_dotenv(dotenv_path)

    api_key = os.getenv("GEMINI_API_KEY")

    # if missing or empty, ask user
    if not api_key:
        print("⚠️ API KEY not found in .env file.")
        api_key = input("🔑 Please enter your API key: ").strip()

        if not api_key:
            raise ValueError("❌ API key cannot be empty!")

        # save it to .env
        set_key(dotenv_path, "GEMINI_API_KEY", api_key)
        load_dotenv(dotenv_path, override=True)
        print("✅ API key saved successfully to .env file!")

    # else:
    #     print("✅ API KEY loaded successfully.")

    return api_key


GEMINI_API_KEY = ensure_api_key()

gemini_api_key = os.getenv("GEMINI_API_KEY")
# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
)