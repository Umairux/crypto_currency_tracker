import requests

print("\nCrypto Currency Converter")
print("-" * 20)

coin = input("Enter coin name(bitcoin, Ethereum, Solana): ").lower()
currency = input("Enter currency: ").lower()

url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"

response = requests.get(url)
data = response.json()

print(f"{coin} price = {data[coin][currency]} {currency.upper()}")  