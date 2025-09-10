import re
import json
import yfinance
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from flask import Flask, request, jsonify

app = Flask(__name__)

def stock_data_tool(input_str: str = ""):
    """Fetch stock data for given ticker symbols or company names."""
    if not input_str:
        return {"error": "No input provided."}
    
    # Extract tickers
    tickers = []
    if ',' in input_str:
        tickers = [t.strip().upper() for t in input_str.split(',')]
    else:
        tickers = [w.upper() for w in re.findall(r"\b[A-Za-z]{1,5}\b", input_str)]
    
    # Smart company name recognition
    common = {
        'apple':'AAPL', 'nvidia':'NVDA', 'microsoft':'MSFT', 'google':'GOOGL', 'tesla':'TSLA',
        'amazon':'AMZN', 'meta':'META', 'facebook':'META', 'netflix':'NFLX', 'adobe':'ADBE',
        'salesforce':'CRM', 'oracle':'ORCL', 'intel':'INTC', 'amd':'AMD', 'zoom':'ZM'
    }
    if not tickers:
        for name, t in common.items():
            if name in input_str.lower(): 
                tickers.append(t)
    
    if not tickers:
        return {"error": "No valid ticker symbols found."}
    
    results = {}
    for t in tickers:
        try:
            tk = yfinance.Ticker(t)
            hist = tk.history(period="1mo")
            if hist.empty:
                results[t] = {"error": "No data."}
                continue
            first, last = hist.iloc[0], hist.iloc[-1]
            change = float(last['Close'] - first['Close'])
            pct = change / float(first['Close']) * 100
            info = tk.info
            summary = {
                "latest_price": float(last['Close']),
                "price_change": change,
                "percent_change": pct,
                "52_week_high": info.get('fiftyTwoWeekHigh'),
                "52_week_low": info.get('fiftyTwoWeekLow'),
                "market_cap": info.get('marketCap'),
                "pe_ratio": info.get('trailingPE')
            }
            results[t] = summary
        except Exception as e:
            results[t] = {"error": str(e)}
    
    return results

def web_scraper_tool(input_str: str = ""):
    """Scrape latest headlines and company snapshot from Finviz."""
    ticker = input_str.upper() if input_str else ""
    
    try:
        if ticker:
            url = f"https://finviz.com/quote.ashx?t={ticker.lower()}"
        else:
            url = "https://finviz.com/news.ashx"
            
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        resp = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        news = []
        for row in soup.select('#news-table tr')[:5]:
            cells = row.find_all('td')
            if len(cells) >= 2:
                date, title = cells[0], cells[1]
                link = title.a['href'] if title.a else ""
                if link and not link.startswith('http'):
                    link = urljoin(url, link)
                news.append({"date": date.text, "title": title.text.strip(), "link": link})
        
        details = {}
        snap = soup.find('table', {'class':'snapshot-table2'})
        if snap:
            for r in snap.find_all('tr'):
                cells = r.find_all('td')
                for i in range(0, len(cells), 2):
                    if i+1 < len(cells):
                        details[cells[i].text] = cells[i+1].text
        
        return {"news_items": news, "snapshot": details}
    except Exception as e:
        return {"error": f"Error fetching news: {str(e)}"}

@app.route('/tools', methods=['GET'])
def get_tools():
    """Return available MCP tools."""
    tools = [
        {
            "name": "equity_analyzer",
            "description": "Advanced equity analysis tool that retrieves comprehensive stock metrics, price movements, and financial ratios.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "input": {
                        "type": "string",
                        "description": "Stock ticker symbols, company names, or comma-separated list for batch analysis"
                    }
                },
                "required": ["input"]
            }
        },
        {
            "name": "market_intelligence",
            "description": "Real-time market intelligence gathering from financial news sources and company-specific updates.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "input": {
                        "type": "string",
                        "description": "Company ticker for targeted news or leave empty for general market intelligence"
                    }
                }
            }
        }
    ]
    return jsonify(tools)

@app.route('/call_tool', methods=['POST'])
def call_tool():
    """Execute MCP tool calls."""
    data = request.get_json()
    tool_name = data.get('name')
    arguments = data.get('arguments', {})
    
    if tool_name == 'equity_analyzer':
        result = stock_data_tool(arguments.get('input', ''))
    elif tool_name == 'market_intelligence':
        result = web_scraper_tool(arguments.get('input', ''))
    else:
        result = {"error": f"Unknown tool: {tool_name}"}
    
    return jsonify({"result": result})

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "server": "MCP Finance Tools"})

if __name__ == '__main__':
    print("🚀 Starting MCP Financial Intelligence Server on port 6001...")
    print("Available tools: equity_analyzer, market_intelligence")
    app.run(host='0.0.0.0', port=6001, debug=False)