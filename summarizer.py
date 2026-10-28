from openai import OpenAI
from dotenv import load_dotenv
from scraper import fetch_website_contents
import os

load_dotenv()
openai = OpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url=os.getenv("GROQ_API_BASE_URL"))

def summarize(url):
    website_contents = fetch_website_contents(url)
    if website_contents.startswith("Could not fetch the website"):
        return website_contents

    system_prompt = """You analyze the contents of a website and
give a short, friendly summary. Ignore navigation menus.
Respond in markdown."""


    user_prompt = f"Summarize the following content in a concise manner:\n\n{website_contents}"

    try:
        response = openai.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        return f"Error during summarization: {e}"