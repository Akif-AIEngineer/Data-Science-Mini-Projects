# Step 1: Waiter (API) Ko Bulana (Tools On Karna)
import requests
# Step 2: Website Ka Link Daalna ( Jahan Se Data Ko Laayega Waiter (API))
url = "https://dog.ceo/api/breeds/image/random"
# Step 3: Saaf BAG (Data) Utha Kar Laana Hai
data = requests.get(url).json()
# Step 4: Bag Se Ham Apni Kaam Ki Cheez Ko Nikal Na
print ("Dog:", data ['message'])
print ("Answer:", data ['status'])