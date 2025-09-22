# test_agent.py
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file as early as possible
load_dotenv()

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core import run_agent_orchestrator

def main():
    """A simple script to test our full agent orchestrator."""
    
    research_goal = "What is the future of renewable energy, specifically focusing on solar and wind power advancements in the last two years?"
    
    final_report = run_agent_orchestrator(research_goal)
    
    print("\n" + "="*50)
    print("--- FINAL RESEARCH REPORT ---")
    print(final_report)
    print("="*50 + "\n")

if __name__ == '__main__':
    main()