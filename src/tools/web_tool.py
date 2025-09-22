# src/tools/web_tool.py

import os
import requests
from bs4 import BeautifulSoup
from langchain.tools import tool
from pydantic import BaseModel, Field
from tavily import TavilyClient

# --- Pydantic Schemas for Structured Inputs ---
# We can still define these for clarity and potential future use,
# but the tool functions will accept primitive types directly.

class SearchInput(BaseModel):
    query: str = Field(description="The search query to find relevant web pages.")

class ScrapeInput(BaseModel):
    url: str = Field(description="The URL of the webpage to scrape.")

# --- The Tools ---

@tool
def search_tavily(query: str) -> str:
    """
    Uses the Tavily search engine to find information on the web.
    Tavily is optimized for AI agents and provides clean, relevant results.
    """
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    try:
        response = client.search(
            query=query,
            search_depth="advanced", # Use advanced search for more comprehensive results
            max_results=5 # Get the top 5 results
        )
        # Format the results into a single, clean string for the agent
        results = [f"URL: {res['url']}\nTitle: {res['title']}\nContent: {res['content']}" for res in response['results']]
        return "\n\n".join(results)
    except Exception as e:
        return f"Error during Tavily search: {e}"

@tool
def scrape_website(url: str) -> str:
    """
    Scrapes the text content from a given URL.
    This tool is used to read the full content of the pages found by the search tool.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract text from main content tags, removing script and style elements
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
            
        text = soup.get_text(separator='\n', strip=True)
        # Encode to ascii and ignore errors to remove non-ascii characters
        return text.encode('ascii', 'ignore').decode('ascii')[:2000]
    except Exception as e:
        return f"Error scraping website {url}: {e}"
