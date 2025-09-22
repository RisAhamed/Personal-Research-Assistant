# Personal Research Assistant - Warp Configuration

## Project Context
- Tech Stack: Python 3.11, LangChain, Streamlit, Docker
- Deployment: Render.com with CI/CD via GitHub Actions
- APIs: OpenRouter, Groq, Tavily

## Preferred Commands
- `streamlit run src/main.py` - Run development server
- `./deploy.sh` - Run full deployment pipeline
- `pytest tests/` - Run test suite

## Environment
- Always use virtual environment: `venv`
- Use pip-tools: `pip-compile requirements.in`