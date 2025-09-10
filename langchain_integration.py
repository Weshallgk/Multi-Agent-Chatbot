import os
from dotenv import load_dotenv
from python_a2a.langchain import to_langchain_agent, to_langchain_tool
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

# Load environment variables
load_dotenv()

# A2A → LangChain
a2a_agent = to_langchain_agent("http://localhost:5001")

# MCP → LangChain
stock_tool = to_langchain_tool("http://localhost:6001", "equity_analyzer")
news_tool = to_langchain_tool("http://localhost:6001", "market_intelligence")

# Define wrapper functions
def ask_expert(q): 
    try:
        return a2a_agent.invoke(q).get('output', str(a2a_agent.invoke(q)))
    except Exception as e:
        return f"A2A expert error: {str(e)}"

def fetch_data(q): 
    try:
        return stock_tool.invoke(q)
    except Exception as e:
        return f"Stock data error: {str(e)}"

def fetch_news(q): 
    try:
        return news_tool.invoke(q)
    except Exception as e:
        return f"News fetch error: {str(e)}"

# Assemble Tool objects
tools = [
    Tool(name="FinancialAdvisor", func=ask_expert, description="Get expert financial intelligence and investment strategy advice."),
    Tool(name="EquityAnalyzer", func=fetch_data, description="Comprehensive equity analysis with stock metrics, price movements, and financial ratios."),
    Tool(name="MarketIntelligence", func=fetch_news, description="Real-time market intelligence and financial news gathering.")
]

# Initialize meta-agent with OpenRouter
llm = ChatOpenAI(
    model="openrouter/sonoma-dusk-alpha",
    temperature=0.0,
    openai_api_key=os.environ.get('OPENROUTER_API_KEY'),
    openai_api_base="https://openrouter.ai/api/v1"
)

meta_agent = initialize_agent(
    tools, llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors=True, max_iterations=3
)