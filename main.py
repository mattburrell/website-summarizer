import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

MODEL = "gpt-4o-mini"

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def fetch_website_content(url):
    """Fetches and returns the text content of a website."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the website. Status code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract visible text from the website
    text = soup.get_text(separator=' ')
    return ' '.join(text.split())  # Remove extra whitespace

def summarize_text(text):
    """Uses OpenAI API to summarize the given text."""
    prompt =f"""
    Perform the following analyses on the website content provided within the triple backticks:
    Main Topic: Identify the main topic of the content and respond with a single word.
    Summary: Summarize the content in 200 words or fewer, focusing on key points and purpose.
    Sentiment: Determine the sentiment of the content and respond with either 'positive' or 'negative'.
    Content: ```{text}```
    """
    response = client.chat.completions.create(
      messages=[
          {"role": "system", "content": "You are a helpful assistant that summarizes text content extracted from a website."},
            {"role": "user", "content": prompt},
      ],
      model=MODEL,
      temperature=0,
    )

    return response.choices[0].message.content

def main():
    url = input("Enter the website URL: ")
    try:
        print("Fetching website content...")
        content = fetch_website_content(url)
        print("Content fetched. Generating summary...")
        summary = summarize_text(content)
        print(f"\nSummary of {url}:")
        print(summary)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
