import os
from dotenv import load_dotenv
from python_a2a import OpenAIA2AServer, run_server
from python_a2a import AgentCard, AgentSkill

# Load environment variables
load_dotenv()

# Set OpenAI client to use OpenRouter
os.environ['OPENAI_API_BASE'] = 'https://openrouter.ai/api/v1'
os.environ['OPENAI_API_KEY'] = os.environ.get('OPENROUTER_API_KEY', '')

# Define the agent's profile
agent_card = AgentCard(
    name="Financial Intelligence Advisor",
    description="Advanced AI specialist in equity research, portfolio optimization, and market intelligence.",
    url="http://localhost:5001",
    version="1.2.0",
    skills=[
        AgentSkill(
            name="Market Intelligence",
            description="Deep analysis of market conditions, sector rotations, and economic indicators.",
            examples=["How is the current economic cycle affecting tech valuations?", "Should I be concerned about rising bond yields?"]
        ),
        AgentSkill(
            name="Portfolio Optimization",
            description="Strategic asset allocation and risk-adjusted return maximization techniques.",
            examples=["What's the optimal allocation between growth and value stocks right now?", "How do I hedge against inflation in my portfolio?"]
        ),
        AgentSkill(
            name="Equity Research",
            description="Comprehensive company evaluation using financial metrics and competitive analysis.",
            examples=["What makes a company undervalued in today's market?", "How do I evaluate a company's competitive moat?"]
        )
    ]
)

# Initialize and start the A2A server
a2a_server = OpenAIA2AServer(
    api_key=os.environ['OPENROUTER_API_KEY'],
    model="openrouter/sonoma-dusk-alpha",
    temperature=0.0,
    system_prompt="You are an advanced financial intelligence advisor specializing in equity research and portfolio strategy. Provide data-driven insights with clear reasoning."
)

if __name__ == '__main__':
    run_server(a2a_server, host='0.0.0.0', port=5001)