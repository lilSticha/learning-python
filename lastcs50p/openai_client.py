import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing from your .env file.")

client = OpenAI(api_key=api_key)

stock_exchange = "Binance"
money = 500
coins = [
    "HYPE", "BTC", "ETH", "BNB", "BCC", "NEO", "LTC",
    "ADA", "QTUM", "XRP", "EOS", "TUSD", "IOTA", "XLM"
]

prompt = f"""You are a cryptocurrency research assistant.
I want to invest in {stock_exchange}. I have {money} dollars to invest.
Analyze these cryptocurrencies: {coins}.

Give three options for long-term consideration and three for short-term
consideration. Follow this format:
Long-term considerations:
first coin - explain why (one sentence)
second coin - explain why (one sentence)
third coin - explain why (one sentence)
Short-term considerations:
first coin - explain why (one sentence)
second coin - explain why (one sentence)
third coin - explain why (one sentence)

Mention key risks. This is informational, not personalized financial advice.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
)

print(response.output_text)