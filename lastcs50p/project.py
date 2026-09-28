import os
from dotenv import load_dotenv
import requests
import json
import sys

load_dotenv()

api_key = os.getenv("COIN_API_KEY")


def main():
    print("WELCOME TO QUICK PRICE CHEKER")
    print("CHOOSE EXCHANGE:")
    print("1. Coin")
    print("2. Binance")
    print("3. Exit")
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
            bitcoin_list = serch_usdt_pair(get_curence_binance_list())
            print_list(bitcoin_list)
            in_coin = input("Enter the valid conit to get curent price: ").strip().upper()
            if in_coin in bitcoin_list:
                print(format_price(get_curent_binance_price(in_coin)))
                break
            else:
                print("Currency are incorect, try agin")
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

if __name__ == "__main__":
    main()

