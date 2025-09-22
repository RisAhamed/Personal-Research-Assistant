# src/agent/core.py

import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

# Import our custom tools
from src.tools.web_tool import search_tavily, scrape_website

# Import the LLM providers
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
load_dotenv()
# --- 1. LLM Configuration ---
# As per your research, we create a configurable way to get the OpenRouter LLM.
def get_openrouter_llm(model_name="google/gemini-pro-1.5-flash"):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables. Please set it in your .env file.")
    
    base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    
    return ChatOpenAI(
        api_key=api_key,
        base_url=base_url,
        model=model_name,
        default_headers={
            "HTTP-Referer": os.getenv("YOUR_SITE_URL", ""),
            "X-Title": os.getenv("YOUR_SITE_NAME", "Personal Research Assistant"),
        }
    )

# --- 2. The Planner Component ---
def create_planner_chain():
    """Creates a chain that generates a research plan."""
    planner_prompt = """
    You are an expert research planner. Your job is to create a detailed, step-by-step plan 
    to answer the user's research question.

    The plan should be a numbered list of tasks. Each task must be a clear instruction 
    for an executor agent. The executor agent has access to two tools:
    1. `search_tavily(query: str)`: To search the web.
    2. `scrape_website(url: str)`: To read the content of a webpage.

    The final step of the plan MUST be: "Synthesize all collected information into a final, comprehensive report."
    Keep the Search clean and short , only use the necessry infromation.

    User's Research Question:
    {goal}
    """
    prompt = ChatPromptTemplate.from_template(planner_prompt)
    # A powerful model is best for strategic planning
    llm = get_openrouter_llm(model_name="anthropic/claude-3-haiku") 
    return prompt | llm | StrOutputParser()

# --- 3. The Executor Component ---
def create_executor_agent():
    """Creates a ReAct agent to execute plan steps."""
    tools = [search_tavily, scrape_website]
    # A fast model is good for tactical execution
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"), temperature = 0.2)
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True, 
        handle_parsing_errors=True
    )

# --- 4. The Orchestrator Logic ---
def run_agent_orchestrator(goal: str):
    """
    Runs the full Plan-and-Execute process as a generator, yielding updates.
    """
    planner = create_planner_chain()
    executor = create_executor_agent()

    # 1. Generate the plan
    yield {"type": "status", "message": "🧠 Generating a research plan..."}
    plan_str = planner.invoke({"goal": goal})
    yield {"type": "plan", "plan": plan_str}
    
    plan_steps = [step.strip() for step in plan_str.split("\n") if step.strip() and step[0].isdigit()]

    # 2. Execute the plan
    execution_results = []
    for i, step in enumerate(plan_steps):
        if "synthesize" in step.lower():
            continue
            
        yield {"type": "status", "message": f"⏳ Executing step {i+1}: {step}"}
        try:
            result = executor.invoke({"input": step})
            yield {"type": "step_result", "step": i+1, "result": result["output"]}
            execution_results.append(result["output"])
        except Exception as e:
            yield {"type": "error", "step": i+1, "error": str(e)}
            execution_results.append(f"Error on step {i+1}: {e}")

    # 3. Synthesize the final report
    yield {"type": "status", "message": "✍️ Synthesizing the final report..."}
    synthesis_context = "\n\n".join(execution_results)
    
    synthesis_prompt = ChatPromptTemplate.from_template(
        """
        You are a research report writer... (same synthesis prompt as before), keep it short and sharp
        Original Goal: {goal}
        Collected Information: {context}
        Final Report:
        """
    )
    synthesis_llm = get_openrouter_llm(model_name="anthropic/claude-3-haiku")
    synthesis_chain = synthesis_prompt | synthesis_llm | StrOutputParser()
    
    final_report = synthesis_chain.invoke({"goal": goal, "context": synthesis_context})
    yield {"type": "final_report", "report": final_report}