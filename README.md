# Multi-Agent Financial Intelligence System

An advanced autonomous financial analysis platform powered by **A2A (Agent-to-Agent) Protocol**, **MCP (Model Context Protocol)**, and **LangChain** orchestration. This system combines multiple AI agents to provide comprehensive equity research, market intelligence, and investment insights using OpenRouter's Sonoma Dusk Alpha model.

## 🏗️ Architecture Overview

```
┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│  A2A Server         │    │  LangChain          │    │  MCP Server         │
│  Port 5001          │    │  Meta-Agent         │    │  Port 6001          │
│                     │    │                     │    │                     │
│ Financial           │◄───┤ Query Router        │───►│ Equity Analyzer     │
│ Intelligence        │    │ Tool Orchestrator   │    │ Market Intelligence │
│ Advisor             │    │                     │    │                     │
└─────────────────────┘    └─────────────────────┘    └─────────────────────┘
```

## 🌟 Key Features

- **Real-Time Equity Analysis**: Live stock prices, financial metrics, and performance data
- **Market Intelligence**: Breaking financial news and market sentiment analysis  
- **AI-Powered Insights**: Professional investment analysis via OpenRouter Sonoma Dusk Alpha
- **Multi-Agent Collaboration**: Autonomous coordination between specialized financial agents
- **Comprehensive Coverage**: Support for 15+ major companies with smart name recognition

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenRouter API Key ([Get one here](https://openrouter.ai))

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
Create a `.env` file in the project root:
```env
OPENROUTER_API_KEY=your-openrouter-api-key-here
```

### 3. Run the System
Open **3 separate terminals** and run:

**Terminal 1 - A2A Financial Intelligence Server:**
```bash
python3 a2a_server.py
```

**Terminal 2 - MCP Financial Tools Server:**
```bash
python3 mcp_http_server.py
```

**Terminal 3 - Execute Query:**
```bash
python3 main.py
```

## 📊 System Components

### A2A Financial Intelligence Advisor
- **Location**: [`a2a_server.py`](a2a_server.py)
- **Port**: 5001
- **Model**: OpenRouter Sonoma Dusk Alpha
- **Capabilities**: 
  - Market Intelligence Analysis
  - Portfolio Optimization Strategies  
  - Comprehensive Equity Research

### MCP Financial Tools Server
- **Location**: [`mcp_http_server.py`](mcp_http_server.py)
- **Port**: 6001
- **Tools**:
  - **Equity Analyzer**: Real-time stock data via yfinance
  - **Market Intelligence**: Financial news scraping from Finviz

### LangChain Meta-Agent
- **Location**: [`langchain_integration.py`](langchain_integration.py)
- **Function**: Orchestrates communication between A2A and MCP servers
- **Agent Type**: Chat-based ReAct (Reasoning + Acting)

## 💡 Usage Examples

### Supported Queries
- "What's Tesla's stock performance today?"
- "Get me Microsoft's latest financial metrics and news"
- "How are tech stocks performing this week?"
- "Should I be concerned about rising interest rates affecting my portfolio?"

### Supported Companies
Apple (AAPL), NVIDIA (NVDA), Microsoft (MSFT), Google (GOOGL), Tesla (TSLA), Amazon (AMZN), Meta (META), Netflix (NFLX), Adobe (ADBE), Salesforce (CRM), Oracle (ORCL), Intel (INTC), AMD (AMD), Zoom (ZM)

## 🔧 Configuration

### Environment Variables
- `OPENROUTER_API_KEY`: Your OpenRouter API key for Sonoma Dusk Alpha access

### Server Ports
- **A2A Server**: 5001 (configurable in `a2a_server.py`)
- **MCP Server**: 6001 (configurable in `mcp_http_server.py`)

## 🛠️ Development

### Project Structure
```
Multi-Agent-Financial-Intelligence/
├── .env                      # API configuration (git ignored)
├── .gitignore               # Git ignore rules
├── a2a_server.py           # A2A Financial Intelligence Advisor
├── mcp_http_server.py      # MCP Financial Tools Server
├── langchain_integration.py # Meta-agent orchestrator
├── main.py                 # Demo execution script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

### Adding New Tools
To add new MCP tools, modify `mcp_http_server.py`:

1. **Create tool function**:
```python
def your_new_tool(input_str: str = ""):
    # Your tool logic here
    return {"result": "your data"}
```

2. **Register in `/tools` endpoint**:
```python
{
    "name": "your_tool_name",
    "description": "What your tool does",
    "inputSchema": { ... }
}
```

3. **Add to `/call_tool` endpoint**:
```python
elif tool_name == 'your_tool_name':
    result = your_new_tool(arguments.get('input', ''))
```

## 🔍 API Endpoints

### A2A Server (Port 5001)
- `POST /`: Financial intelligence queries

### MCP Server (Port 6001)  
- `GET /tools`: List available financial tools
- `POST /call_tool`: Execute specific tool
- `GET /health`: Server health check

## 📈 Example Output

```
🚀 Multi-Agent Financial Intelligence System
Query: I need to check Tesla and Microsoft stock performance today

📊 Equity Analysis:
- Tesla (TSLA): $248.50 (+2.3% today)
- Microsoft (MSFT): $378.85 (+1.2% today)

📰 Market Intelligence:
- "Tesla Reports Strong Q3 Delivery Numbers" (Reuters, 2h ago)
- "Microsoft Azure Revenue Beats Expectations" (Bloomberg, 4h ago)

💡 Financial Intelligence:
Based on current market conditions, both TSLA and MSFT show positive momentum...
```

## 🔒 Security

- API keys stored in `.env` file (git ignored)
- No sensitive data logged
- Input sanitization on all endpoints
- Error handling prevents information leakage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **OpenRouter**: Sonoma Dusk Alpha model API
- **Google A2A Protocol**: Agent-to-agent communication framework
- **Model Context Protocol (MCP)**: Standardized tool integration
- **LangChain**: Agent orchestration and reasoning framework
- **Yahoo Finance**: Real-time financial data source
- **Finviz**: Financial news and market intelligence

---

**Built with ❤️ for the future of autonomous financial intelligence**