import requests

url = "https://mountain-api1.p.rapidapi.com/api/mountains"


headers = {
	"x-rapidapi-key": "b3c1599eeamsh15f5406714c8819p11548bjsn28eb8925c3bc",
	"x-rapidapi-host": "mountain-api1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

#Nos retorna un vector con todos los elementos
print(response.json()[2]['altitude'])