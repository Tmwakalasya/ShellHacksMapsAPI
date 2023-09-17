import requests
api_key = 'ab34610c-1e58-415e-a883-053379f689fe'

def get_crypto_data(crypto_symbol):
    base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {
        "symbol": crypto_symbol,
    }
    headers = {
        "X-CMC_PRO_API_KEY": api_key,
    }
    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if crypto_symbol in data["data"]:
            return data["data"][crypto_symbol]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

crypto_symbol = input("Enter the cryptocurrency symbol (e.g., BTC, ETH): ").upper()
crypto_data = get_crypto_data(crypto_symbol)

if crypto_data:
    print(f"Name: {crypto_data['name']}")
    print(f"Symbol: {crypto_data['symbol']}")
    print(f"Current Price (USD): {crypto_data['quote']['USD']['price']:.2f}")
    print(f"Market Cap (USD): {crypto_data['quote']['USD']['market_cap']:.2f}")
    print(f"Total Volume (USD): {crypto_data['quote']['USD']['volume_24h']:.2f}")
else:
    print(f"No data found for {crypto_symbol}. Check the symbol and try again.")

