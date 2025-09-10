from langchain_integration import meta_agent

if __name__ == '__main__':
    print("🚀 Multi-Agent Financial Chatbot")
    print("A2A + MCP + LangChain Architecture")
    print("=" * 50)
    print("Requires:")
    print("1. A2A server running on port 5001")
    print("2. MCP server running on port 6001")
    print("=" * 50)
    
    query = "I need to check Tesla and Microsoft stock performance today along with any breaking financial news"
    print(f"Query: {query}")
    print("=" * 50)
    
    try:
        response = meta_agent.invoke({"input": query})
        print("Meta-Agent Response:")
        print(response.get("output", str(response)))
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Make sure A2A server is running: python3 a2a_server.py")
        print("2. Make sure MCP server is running: python3 mcp_http_server.py")  
        print("3. Check that OPENROUTER_API_KEY is set in .env file")