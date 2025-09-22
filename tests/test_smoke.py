"""
Minimal smoke tests for CI/CD pipeline.
These tests don't make external API calls to ensure CI can pass without secrets.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def test_main_module_imports():
    """Test that main modules can be imported without errors."""
    try:
        import main  # Streamlit app
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import main module: {e}")


def test_agent_core_imports():
    """Test that agent core module can be imported."""
    try:
        from agent import core
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import agent.core: {e}")


def test_tools_imports():
    """Test that tools module can be imported."""
    try:
        from tools import web_tool
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import tools.web_tool: {e}")


@patch.dict(os.environ, {
    'OPENROUTER_API_KEY': 'test-key',
    'OPENROUTER_BASE_URL': 'https://test.com',
    'YOUR_SITE_URL': 'https://test-site.com',
    'YOUR_SITE_NAME': 'Test Site',
    'GROQ_API_KEY': 'test-groq-key',
    'TAVILY_API_KEY': 'test-tavily-key'
})
def test_openrouter_llm_creation():
    """Test that OpenRouter LLM can be created with mocked environment."""
    try:
        from agent.core import get_openrouter_llm
        # Mock the ChatOpenAI to avoid actual API calls
        with patch('agent.core.ChatOpenAI') as mock_chat:
            mock_instance = MagicMock()
            mock_chat.return_value = mock_instance
            
            llm = get_openrouter_llm()
            assert llm is mock_instance
            mock_chat.assert_called_once()
    except Exception as e:
        pytest.fail(f"Failed to create OpenRouter LLM: {e}")


def test_missing_openrouter_key_raises_error():
    """Test that missing OPENROUTER_API_KEY raises appropriate error."""
    from agent.core import get_openrouter_llm
    
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="OPENROUTER_API_KEY not found"):
            get_openrouter_llm()


@patch.dict(os.environ, {'TAVILY_API_KEY': 'test-key'})
def test_tavily_search_tool_structure():
    """Test that Tavily search tool has expected structure."""
    from tools.web_tool import search_tavily
    
    # Check tool has expected attributes
    assert hasattr(search_tavily, 'name')
    assert hasattr(search_tavily, 'description')
    assert search_tavily.name == 'search_tavily'


def test_scrape_website_tool_structure():
    """Test that scrape website tool has expected structure."""
    from tools.web_tool import scrape_website
    
    # Check tool has expected attributes  
    assert hasattr(scrape_website, 'name')
    assert hasattr(scrape_website, 'description')
    assert scrape_website.name == 'scrape_website'


def test_project_structure():
    """Test that expected project files exist."""
    project_root = os.path.dirname(os.path.dirname(__file__))
    
    expected_files = [
        'src/main.py',
        'src/agent/core.py',
        'src/tools/web_tool.py',
        'Dockerfile',
        'requirements.in',
        'pyproject.toml',
        '.pre-commit-config.yaml'
    ]
    
    for file_path in expected_files:
        full_path = os.path.join(project_root, file_path)
        assert os.path.exists(full_path), f"Expected file {file_path} does not exist"


if __name__ == '__main__':
    pytest.main([__file__])