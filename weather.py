import json
import requests
def main():
    city = input("Enter city: ")
    url = "https://api.openweathermap.org/data/2.5/weather"
    API_key = "ffde2744cf36417220e1ddca983a2a7d"
    
    api_request(city, url, API_key)
def api_request(city, url, key):
    par = {
            "q": city,
            "appid": key,
            "units": "metric" 
            }
    response = requests.get(url, params = par)
    #print(json.dumps(response.json(), indent = 2))
    json_answer = response.json()
    for k, v in json_answer["main"].items():
        print(f"{k}:{v}")

if __name__ == "__main__":
    main()