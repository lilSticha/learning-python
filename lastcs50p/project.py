import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json
import sys

load_dotenv()

api_key = os.getenv("COIN_API_KEY")
#gemini_api_key = os.getenv("GEMINI_API_KEY")
api_key = os.getenv("OPENAI_API_KEY")

def main():
    print("WELCOME TO QUICK PRICE CHEKER")
    print("CHOOSE EXCHANGE:")
    print("1. Coin")
    print("2. Binance")
    print("3. AI recomandation")
    print("4. Exit")
    choise = input("Enter your choise:")
    if choise.strip() == '1' or choise.strip().upper() == "COIN":
        # while True:
        #     cur_list = get_currency_list()
        #     print_list(cur_list)
        #     currency = input("Enter currency what you want to check:").strip().upper()
        #     if currency in cur_list:
        #         print(f"{get_currecny_price(currency)}")
        #         break
        #     else:
        #         print("Currency are incorect, try agin")
        print("ok")
    elif choise.strip() == '2' or choise.strip().upper() == "BINANCE":
        while True:
            cur_list = serch_usdt_pair(get_curence_binance_list())
            print_list(cur_list)
            in_coin = input("Enter the valid coin to get curent price: ").strip().upper()
            if in_coin in cur_list:
                print(format_price(get_curent_binance_price(in_coin)))
                break
            else:
                print("Currency are incorect, try agin")
    elif choise.strip() == '3' or choise.strip().upper() == "AI" or choise.strip().upper() == "AI recomandation":
        print("Hej! I am yout ai investment helper. I will analyse curent curecy status and will recoment the best way to long and term investment!")
        while True:
            stock_exchange = str(input("""choose your stock exchande from list
1. Coin
2. Binance
            """))
            if stock_exchange == '1':
                stock_exchange = 'Coin'
                list = get_currency_list()
                break
            elif stock_exchange == '2':
                stock_exchange = 'Binance'
                list = get_curence_binance_list()
                break
            else:
                print("Incorect choose, try again enter stockexchange :(")
        
        while True:
            try:
                price = int(input("Enter price what you want to invest, write integer number: "))
                break
            except ValueError:
                print("It is not integer number, try again")

        #have correct stock exchange and price what user want to invest.
        print(ai_recomendation(stock_exchange, price, list)) #too many cumbols in promt!

        
    elif choise == '1':
        sys.exit("Exit")
    else:
        sys.exit("Exit")



def get_currency_list():
    coins = []
    url = "https://rest.coincap.io/v3/assets"
    try:
        responce = requests.get(url + "?apiKey=" + api_key).json()
       # responce.raise_for_status()
       # responce_json = responce.json()
        for coin in responce['data'][0]:
            coins.append(f"{coin['symbol']}")# - {coin['name']}
        return coins
    except requests.RequestException as e:
        sys.exit(f"Request Error: {e}")

def print_list(list):
    for i in range(len(list)):
        print(list[i])

def get_currecny_price(cur) -> float:
    url = "https://rest.coincap.io/v3/price/bysymbol/"
    try:
        responce = requests.get(url+cur+"?apiKey="+api_key).json() #.json()
        #responce_json = responce.json()
        price = float(responce['data'][0]) # responce_json
        return price
    except requests.RequestException:
         sys.exit(f"Request Error {responce.status_code()}")


def get_curence_binance_list():
    coins = []
    url = "https://api.binance.com/api/v3/exchangeInfo"
    try:
        responce = requests.get(url).json() #.json()
        return responce
        #responce_json = responce.json()
    #     for i in responce['symbols']: #.json
    #         if i['quoteAsset'] == "USDT":
    #             coins.append(i['baseAsset'])
    #     return coins
    except requests.RequestException as e:
         sys.exit(f"Request Error: {e}")

def serch_usdt_pair(json:list) -> list:
    coins = []
    for i in json['symbols']:
        if i['symbol'].endswith('USDT'):
            coins.append(i['symbol'].replace('USDT', ''))
    return coins


def get_curent_binance_price(coin:str):
    url = "https://api.binance.com/api/v3/ticker/price?symbol="
    try:
        responce = requests.get(f"{url}{coin}USDT").json()
        #print(type(responce['price']))
        return float(responce['price'])
    except requests.RequestException as e:
        sys.exit(f"Request Error: {e}")

def format_price(price:float) -> float:
    return f"${price:,.2f}"

def ai_recomendation(exchange:str, price:int, coin_list:list) -> str:
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing from your .env file.")

    client = OpenAI(api_key=api_key)
    prompt = f"""You are a cryptocurrency research assistant.
    I want to invest in {exchange}. I have {price} dollars to invest.
    Analyze all this coins: {coin_list}.

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
    return response.output_text
    

if __name__ == "__main__":
    main()

