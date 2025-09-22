# Personal Research Assistant

🤖 **AI-Powered Research Assistant** built with LangChain, Streamlit, and deployed on Render.

A sophisticated multi-agent system that plans, executes, and synthesizes comprehensive research reports on any topic using advanced web search and content analysis.

## ✨ Features

- **Intelligent Planning**: Creates structured research plans using Claude Haiku
- **Multi-Agent Execution**: Uses specialized agents for search and synthesis
- **Advanced Web Search**: Leverages Tavily API for comprehensive web research
- **Real-time Updates**: Live progress updates during research execution
- **Professional Reports**: Generates well-structured, comprehensive research reports
- **Cloud Deployment**: Ready for deployment on Render with CI/CD automation

## 🚀 Quick Start

### Prerequisites

- Python 3.11.13+
- Docker (optional, for local containerization)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd personal-research-assistant
   ```

2. **Set up Python virtual environment**
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install pip-tools and compile dependencies**
   ```bash
   pip install pip-tools
   pip-compile requirements.in
   pip install -r requirements.txt
   ```

4. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Configure environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env with your API keys (see API Keys section below)
   ```

6. **Run locally**
   ```bash
   streamlit run src/main.py
   ```

   Visit `http://localhost:8501` in your browser.

## 🔑 API Keys Setup

You'll need to obtain API keys from the following services:

### 1. OpenRouter API
- Visit: https://openrouter.ai/
- Sign up and get your API key
- Set `OPENROUTER_API_KEY` in your `.env` file

### 2. Groq API
- Visit: https://console.groq.com/
- Create an account and generate an API key
- Set `GROQ_API_KEY` in your `.env` file

### 3. Tavily API
- Visit: https://tavily.com/
- Sign up for a free account
- Get your API key from the dashboard
- Set `TAVILY_API_KEY` in your `.env` file

### Environment Variables Template

Copy `.env.example` to `.env` and fill in your values:

```bash
# OpenRouter Configuration (Required)
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
YOUR_SITE_URL=https://your-site.com
YOUR_SITE_NAME=Personal Research Assistant

# Groq Configuration (Required)
GROQ_API_KEY=your_groq_api_key_here

# Tavily Configuration (Required)
TAVILY_API_KEY=your_tavily_api_key_here
```

## 🌐 Deploying to Render

### Option 1: Using Infrastructure-as-Code (Recommended)

1. **Create a new GitHub repository** and push this code

2. **Connect to Render using render.yaml**:
   - Go to https://dashboard.render.com/
   - Click "New" → "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` file
   - Set the environment variables in the Render dashboard

### Option 2: Manual Setup via Render Dashboard

1. **Create Web Service**:
   - Go to https://dashboard.render.com/
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Configure as follows:

2. **Service Configuration**:
   - **Name**: `research-assistant`
   - **Environment**: `Docker`
   - **Region**: `Singapore` (Asia/India proximity)
   - **Branch**: `main`
   - **Plan**: `Free`
   - **Dockerfile Path**: `./Dockerfile`

3. **Environment Variables**:
   Set these in the Render dashboard:
   ```
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
   YOUR_SITE_URL=https://your-render-app-url
   YOUR_SITE_NAME=Personal Research Assistant
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   PORT=8501
   ```

4. **Deploy Settings**:
   - Enable "Auto-Deploy" for automatic deployments on push
   - The service will build and deploy automatically

## 🔄 CI/CD Pipeline

The project includes a complete GitHub Actions workflow that:

- ✅ **Quality Checks**: Runs linting (ruff, black, isort) and tests
- 🐳 **Container Build**: Builds Docker images with caching
- 🔍 **Security Scan**: Scans images for vulnerabilities with Trivy
- 📦 **Registry Push**: Optionally pushes to GitHub Container Registry
- 🚀 **Auto Deploy**: Triggers Render deployment on successful builds

### Setting up CI/CD

1. **GitHub Secrets** (Optional - for advanced features):
   - `RENDER_DEPLOY_HOOK_URL`: Get from Render service → Settings → Deploy Hook
   - `GITHUB_TOKEN`: Automatically available for registry push

2. **Workflow Triggers**:
   - Push to `main` or `develop` branches
   - Pull requests to `main`
   - Manual workflow dispatch

## 🛠️ Development Workflow

### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and ensure quality:
   ```bash
   # Format code
   black .
   isort .
   ruff check . --fix
   
   # Run tests
   pytest
   ```

3. **Commit using conventional commits**:
   ```bash
   git commit -m "feat: add new research capability"
   ```

4. **Push and create PR**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Local Testing

```bash
# Run the deployment script locally
./deploy.sh

# Or run individual steps
ruff check . --fix
black .
pytest
docker build -t research-assistant .
```

## 📁 Project Structure

```
personal-research-assistant/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── src/
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── core.py             # Main agent orchestration logic
│   │   └── test_agent.py       # Agent testing script
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── web_tool.py         # Tavily search & web scraping
│   │   └── test_tools.py       # Tools testing script
│   ├── ui/
│   │   ├── __init__.py
│   │   └── components.py       # UI components (if needed)
│   └── main.py                 # Streamlit application entry point
├── tests/
│   ├── __init__.py
│   └── test_smoke.py           # Smoke tests for CI
├── .dockerignore
├── .env.example                # Environment variables template
├── .gitignore
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── deploy.sh                   # Local deployment script
├── Dockerfile                  # Multi-stage container build
├── pyproject.toml              # Project configuration
├── README.md                   # This file
├── render.yaml                 # Render infrastructure-as-code
├── requirements.in             # High-level dependencies
└── requirements.txt            # Compiled dependencies (generated)
```

## 🔧 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Make sure you're in the virtual environment
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\Activate.ps1  # Windows PowerShell

# Reinstall dependencies
pip install -r requirements.txt
```

**2. API Key Errors**
- Verify all required API keys are set in `.env`
- Check for typos in environment variable names
- Ensure API keys are valid and have sufficient quota

**3. Docker Build Issues**
```bash
# Clear Docker cache
docker system prune -a

# Rebuild without cache
docker build --no-cache -t research-assistant .
```

**4. Render Deployment Issues**
- Check build logs in Render dashboard
- Verify all environment variables are set
- Ensure Dockerfile is in the repository root
- Check that PORT environment variable is set to 8501

### Windows-Specific Commands

| Task | Linux/macOS | Windows PowerShell |
|------|-------------|--------------------|
| Activate venv | `source venv/bin/activate` | `.\venv\Scripts\Activate.ps1` |
| Copy env file | `cp .env.example .env` | `Copy-Item .env.example .env` |
| Make executable | `chmod +x deploy.sh` | Not needed |
| Run deploy script | `./deploy.sh` | `bash deploy.sh` |

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [LangChain Documentation](https://docs.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Tavily API Documentation](https://docs.tavily.com/)
- [OpenRouter API Documentation](https://openrouter.ai/docs)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes following the code quality standards
4. Add tests for new functionality
5. Ensure all tests pass and pre-commit hooks succeed
6. Submit a pull request with a clear description

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Built with ❤️ using LangChain, Streamlit, and modern DevOps practices.**

#   P e r s o n a l - R e s e a r c h - A s s i s t a n t  
 