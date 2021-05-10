import requests

aadress = "https://api.chucknorris.io/jokes/random"
päring = requests.get(aadress)
vastus = päring.json()

print(vastus["value"])
