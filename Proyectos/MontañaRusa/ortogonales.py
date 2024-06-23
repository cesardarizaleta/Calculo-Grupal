import requests

url = "https://mountain-api1.p.rapidapi.com/api/mountains"

querystring = {"name":"Mount Everest"}

headers = {
	"x-rapidapi-key": "b3c1599eeamsh15f5406714c8819p11548bjsn28eb8925c3bc",
	"x-rapidapi-host": "mountain-api1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())