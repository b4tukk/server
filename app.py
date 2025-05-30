def get_crypto_price(coin_id):
    import requests

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
            return {"price": price}
        else:
            return {"error": "Kripto para bulunamadı."}
    else:
        return {"error": f"API hatası: {response.status_code}"}