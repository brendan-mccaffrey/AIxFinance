# AI x Finance Hackathon

_Princeton, March 2026 — Hosted by [TradeXYZ](https://x.com/tradexyz)_

---

## In the News

TradeXYZ is building the next-generation perpetual futures exchange for 24/7 trading across traditional asset classes on Hyperliquid.

- [S&P Global — S&P 500 Licensed to TradeXYZ for Perpetual Contracts on Hyperliquid](https://www.spglobal.com/spdji/en/index-announcements/article/sp-dow-jones-indices-licenses-sp-500-to-trade-xyz-for-perpetual-contracts-on-hyperliquid/)
- [WSJ — S&P 500 Owner Jumps Into 24/7 Futures for Index on Crypto Exchange](https://www.wsj.com/finance/s-p-500-owner-jumps-into-24-7-futures-for-index-on-crypto-exchange-6c65696b)
- [WSJ — Oil Futures Perpetual Contracts](https://www.wsj.com/finance/commodities-futures/oil-futures-perpetual-contracts-d5496e5a)
- [Bloomberg — Booming Crypto Exchange Gets Official S&P Data in TradFi Push](https://www.bloomberg.com/news/articles/2026-03-18/booming-crypto-exchange-gets-official-s-p-data-in-tradfi-push)
- [Bloomberg — Oil Trades Are Booming on 24/7 Crypto Exchange Hyperliquid](https://www.bloomberg.com/news/articles/2026-03-09/oil-trades-are-booming-on-24-7-crypto-exchange-hyperliquid)
- [Bloomberg — Oil, Gold Rally on Hyperliquid as 24/7 Crypto Prices Iran Risk](https://www.bloomberg.com/news/articles/2026-02-28/oil-gold-rally-on-hyperliquid-as-24-7-crypto-prices-iran-risk)
- [Bloomberg — Hyperliquid Grows Into a Major Player in Crypto Derivatives](https://www.bloomberg.com/news/newsletters/2025-05-13/hyperliquid-grows-into-a-major-player-in-crypto-derivatives)

---

## Credits & Getting Started

- [Anthropic Credits: `3ad57a8e-d76b-4ad5-bd74-030935598bf7`](https://claude.com/offers?offer_code=3ad57a8e-d76b-4ad5-bd74-030935598bf7)
- [OpenAI / Codex Student Credits](https://developers.openai.com/community/students)
- **For testnet funds, inquire with judges.**

---

## Trading Platforms

### TradeXYZ

|               |                                          |
| ------------- | ---------------------------------------- |
| Web App       | [app.trade.xyz](https://app.trade.xyz)   |
| Documentation | [docs.trade.xyz](https://docs.trade.xyz) |
| X / Twitter   | [@tradexyz](https://x.com/tradexyz)      |

### Hyperliquid

|                 |                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------- |
| Web App         | [app.hyperliquid.xyz](https://app.hyperliquid.xyz)                                             |
| Documentation   | [Hyperliquid Docs](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api)         |
| Builder Codes   | [Docs](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/builder-codes#api-for-builders) |
| Historical Data | [Docs](https://hyperliquid.gitbook.io/hyperliquid-docs/historical-data#asset-data)             |

**SDKs:** [Python](https://github.com/hyperliquid-dex/hyperliquid-python-sdk) · [Rust](https://github.com/infinitefield/hypersdk) · [TypeScript (nktkas)](https://github.com/nktkas/hyperliquid) · [TypeScript (nomeida)](https://github.com/nomeida/hyperliquid)

**Explorers:** [Hypurrscan](https://hypurrscan.io/) · [Hyperdash](https://hyperdash.com/explore)

---

## Free APIs — Market Data

| API                                                               | What You Get (Free Tier)                                                                | Best For                                                                    |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [**yfinance**](https://github.com/ranaroussi/yfinance)            | Historical OHLCV, fundamentals, dividends. No API key needed.                           | Quick prototyping, backtesting. Easiest way to get started in Python.       |
| [**Alpaca**](https://alpaca.markets)                              | Real-time + historical US equities, paper trading with execution. Free account.         | End-to-end: data _and_ simulated order execution in one SDK.                |
| [**Alpha Vantage**](https://www.alphavantage.co/)                 | Time series, 50+ technical indicators, fundamentals, forex, crypto. 25 req/day free.    | Technical analysis pipelines. Has an MCP server for LLM agent integration.  |
| [**Finnhub**](https://finnhub.io/)                                | Real-time US quotes, fundamentals, filings, earnings, news, sentiment. 60 req/min free. | Most generous free tier for real-time data.                                 |
| [**Polygon.io**](https://polygon.io/)                             | EOD data, limited real-time. 5 req/min free.                                            | WebSocket streaming, tick-level data (paid tiers unlock the full firehose). |
| [**Financial Modeling Prep**](https://financialmodelingprep.com/) | SEC EDGAR fundamentals, 30+ years of historicals, financial ratios. 250 req/day free.   | Fundamental analysis — balance sheets, income statements, ratios.           |
| [**FRED API**](https://fred.stlouisfed.org/docs/api/fred/)        | US macro data — GDP, CPI, interest rates, employment. Free with key.                    | Macro-overlay signals, regime detection.                                    |
| [**CoinGecko**](https://www.coingecko.com/en/api)                 | Crypto prices, volume, market cap, historical data. Free tier available.                | Crypto-focused projects.                                                    |

### Quick Start — Pull Data in 3 Lines

```python
import yfinance as yf
df = yf.download("AAPL", start="2024-01-01")
print(df.tail())
```

---

## News & Sentiment APIs

| API                                               | What It Does                                                  |
| ------------------------------------------------- | ------------------------------------------------------------- |
| [**NewsAPI**](https://newsapi.org/)               | Headlines and articles from 150K+ sources. Free for dev use.  |
| [**Reddit API**](https://www.reddit.com/dev/api/) | Pull posts/comments from r/wallstreetbets, r/stocks, etc.     |
| [**Tavily**](https://tavily.com/)                 | Search API purpose-built for LLM agents. Free tier available. |

---

## The State of AI Trading (March 2026)

### The Core Idea

LLMs can now ingest market data, news, and fundamentals, reason about them, and output structured trade decisions. The field has moved from "can LLMs analyze sentiment?" to "can LLM _agents_ trade profitably in real markets?" The answer so far: it's hard, but the architecture matters more than the model.

### Key Research

- **"TradingAgents: Multi-Agents LLM Financial Trading Framework"** ([arXiv](https://arxiv.org/abs/2412.20138), [GitHub](https://github.com/TauricResearch/TradingAgents)) — Open-source multi-agent framework mirroring real trading firms: fundamental analysts, sentiment analysts, technical analysts, risk managers, and traders as separate LLM agents that debate and collaborate. Outperforms single-agent baselines on cumulative returns and Sharpe ratio.

- **"StockBench: Can LLM Agents Trade Stocks Profitably In Real-world Markets?"** ([arXiv](https://arxiv.org/abs/2510.02209)) — A contamination-free benchmark where LLM agents trade top-20 DJIA stocks over 82 real trading days. Finding: most models _struggle to beat buy-and-hold_, but some show strong risk management. Static QA performance doesn't predict trading ability.

- **"LLM Agent in Financial Trading: A Survey"** ([arXiv](https://arxiv.org/abs/2408.06361)) — Comprehensive survey of architectures, data inputs, and backtesting results. Good starting point for understanding the design space.

- **"Can LLM-based Financial Investing Strategies Outperform the Market in Long Run?"** ([SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5287013)) — Sobering result: LLM timing strategies tested over 20 years and 100+ symbols show degraded performance at scale. Models tend to be too conservative in bull markets and too aggressive in bear markets.

- **"Large Language Models in Equity Markets"** ([Frontiers](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1608365/full)) — Review of 84 studies covering forecasting, sentiment analysis, portfolio management, and algorithmic trading with LLMs.

### What's Happening in Industry

Multi-agent architectures are becoming the dominant paradigm — separate agents for research, risk, execution, and portfolio management rather than one monolithic prompt. The hard problem isn't "can the model reason about markets?" — it's risk management, position sizing, and knowing when _not_ to trade.

---

## Inspiration: Alpha Arena by Nof1

[**Alpha Arena**](https://nof1.ai/) was the world's first live AI trading benchmark — six frontier LLMs (GPT-5, Claude, Gemini, DeepSeek, Grok, Qwen), each given $10,000 in real capital, trading crypto perpetuals autonomously on Hyperliquid with zero human intervention. All wallets were on-chain and fully transparent.

**Key takeaways from Season 1:**

- **Qwen 3 Max won** with a 12.11% return by trading infrequently (only 43 trades in 17 days) and using strict stop-loss/take-profit rules.
- **DeepSeek** hit +125% mid-competition but gave most of it back — classic overfit to momentum.
- **Trade frequency correlated inversely with final returns** — the models that traded less, won more.
- Biggest lesson: **risk management > raw intelligence.** The smartest model means nothing if it can't size positions and cut losses.

Nof1's thesis: financial markets are the ultimate training environment for AI — adversarial, non-stationary, and the only benchmark that gets harder as AI gets smarter.

---

## Example Architecture

### Single-Agent Loop

```
Market Data → LLM Prompt → Structured JSON Decision → Execute
     ↑                                                    |
     └────────────── Portfolio State ←─────────────────────┘
```

Feed the LLM current prices, portfolio state, and recent news. Ask it to output a JSON with `{action, ticker, size, confidence}`. Loop every N minutes.

### Example Stack

```
Python 3.11+
├── yfinance            # market data
├── alpaca-py           # paper trading + execution
├── anthropic / openai  # LLM inference
├── pandas              # data manipulation
├── tavily-python       # news search for agents
└── streamlit           # quick dashboard
```

---

## Tips from the Trenches

1. **Start with paper trading.** Alpaca's paper trading API is free and realistic. Don't touch real money at a hackathon.
2. **Log everything.** Every LLM call, every decision, every trade. Your reasoning traces are your most valuable output — they're what you'll learn from and present to judges.
3. **Eval > vibes.** Define your metrics upfront: cumulative return, Sharpe ratio, max drawdown, win rate. Build a simple dashboard to track them.
4. **The model that trades less usually wins.** Frequency is the enemy of hackathon trading bots. Build in a "do nothing" option and make it the default.

---

## Additional Resources

- [TradingAgents GitHub](https://github.com/TauricResearch/TradingAgents) — open-source multi-agent trading framework
- [Alpha Vantage API Docs](https://www.alphavantage.co/documentation/) — comprehensive market data API
- [Alpaca Docs](https://docs.alpaca.markets/) — paper trading + market data
- [Finnhub API Docs](https://finnhub.io/docs/api) — real-time quotes and fundamentals
- [Nof1 / Alpha Arena](https://nof1.ai/) — live AI trading benchmark
- [StockBench Paper](https://arxiv.org/abs/2510.02209) — LLM trading agent benchmark

---

_Built for the Princeton AI x Finance Hackathon. Good luck, and remember: risk management > raw returns._
