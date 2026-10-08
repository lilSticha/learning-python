import os
from dotenv import load_dotenv
from google import genai
import requests, time

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
# print(api_key)
if not api_key:
    raise ValueError("GEMINI API KEY is missing :(")

# client = genai.Client(api_key = api_key)
# stock_exchange = "Binance"
# money = 500
# list = ['HYPE', 'BTC', 'ETH', 'BNB', 'BCC', 'NEO', 'LTC', 'ADA','QTUM', 'ADA','XRP', 'EOS', 'TUSD', 'IOTA', 'XLM']

# promt = f"""You are profesional cruptocurency consultant investment.
# You use the currency valuation templates of the world’s leading consultants.
# I want to invest in {stock_exchange} stock exchange, 
# I have {money} dolars to invest,
# Analyse this crupto-curency from that stock exchange: {list}.
# And give me tip for long term investment and short term investment.
# Give only 3 the best coins for each investmant term.
# The answer must strictly follow the template: 
#     Long term investment: 
#     first coin - explaine why(1 sentence)
#     second coin - explaine why(1 sentence)
#     third coin - explaine why(1 sentence)
#     Shourt term investment:
#     first coin - explaine why(1 sentence)
#     second coin - explaine why(1 sentence)
#     third coin - explaine why(1 sentence)
# """
# response = client.models.generate_content(
#     model="gemini-3.8-flash",
#     contents=promt,
# )
# print(response.text)

# for model in client.models.list():
#     print(model.name)


def price_ago(symbol, minutes):
    end_ms = int((time.time() - minutes * 60) * 1000)
    r = requests.get(
        "https://data-api.binance.vision/api/v3/klines",
        params={"symbol": symbol, "interval": "1m",
                "endTime": end_ms, "limit": 1},
        timeout=10,
    )
    r.raise_for_status()
    candle = r.json()[0]
    return float(candle[4])  # close

for label, m in [("10 хв", 10), ("1 год", 60), ("10 год", 600), ("1 день", 1440)]:
    print(label, price_ago("BTCUSDT", m))