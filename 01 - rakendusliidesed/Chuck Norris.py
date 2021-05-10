import requests

aadress = "https://api.chucknorris.io/jokes/random"
päring = requests.get(aadress)
vastus = päring.json()
print(vastus["value"])


tagasiside = input("Kas nali meeldis :D? - ")
if tagasiside == "Jah":
    print("Peabki meeldima! Chuck Norris on JUMAL!!")
elif tagasiside == "jah":
    print("Peabki meeldima! Chuck Norris on JUMAL!!")
elif tagasiside == "jes":
    print("Peabki meeldima! Chuck Norris on JUMAL!!")
elif tagasiside == "Jes":
    print("Peabki meeldima! Chuck Norris on JUMAL!!")
elif tagasiside == "Hell yeah":
    print("Peabki meeldima! Chuck Norris on JUMAL!!")
elif tagasiside == "JAH":
    print("Peabki meeldima! Chuck Norris on JUMAL!!")
elif tagasiside == "ja":
    print("Peabki meeldima! Chuck Norris on JUMAL!!")
elif tagasiside == "Ja":
    print("Peabki meeldima! Chuck Norris on JUMAL!!")
else:
    print("Sinust, poeg, ei saa asja!")
