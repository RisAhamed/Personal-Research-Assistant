# test_tools.py
import os
from dotenv import load_dotenv
from web_tool import search_tavily, scrape_website

def main():
    """A simple script to test our new tools."""
    load_dotenv()
    
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        print("Error: TAVILY_API_KEY not found.")
        print("Please make sure you have a .env file in the root of your project with TAVILY_API_KEY=<your_api_key>")
        return

    print("--- Testing Tavily Search Tool ---")
    search_result = search_tavily.invoke({"query": "What is the latest news on Llama 3?"})
    print(search_result)

    print("\n" + "="*50 + "\n")

    print("--- Testing Web Scraper Tool ---")
    # We will use a simple, stable URL for testing
    scrape_result = scrape_website.invoke({"url": "https://github.com/meta-llama/llama3"})
    print(scrape_result)

if __name__ == '__main__':
    main()