import requests

def get_crypto_price(coin_id):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if coin_id in data:
            price = data[coin_id]["usd"]
            print(f"{coin_id.capitalize()} fiyatı: ${price}")
        else:
            print("Kripto para bulunamadı.")
    else:
        print("API hatası:", response.status_code)

# Kullanıcıdan veri al
coin = input("Takip etmek istedigin kripto para (ornek: bitcoin, ethereum, dogecoin): ").lower()
get_crypto_price(coin)
