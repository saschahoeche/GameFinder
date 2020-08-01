import requests

apiServerURL = "https://api.rawg.io/api/games/grand-theft-auto-v"

response = requests.get(apiServerURL)

# check if server response, then get json
if response.status_code != 200:
    print("[-] Can't connect to API Server, please check URL or try again later.")
else:
    print("[+] Successfully Connected to Server \n")
    dataJson = response.json()
    gameName = dataJson["name_original"]
    description = dataJson["description_raw"]
    metacritic = dataJson["metacritic"]
    releaseDate = dataJson["released"]
    gameImg = dataJson["background_image"]


print(gameName, metacritic, releaseDate, gameImg)

