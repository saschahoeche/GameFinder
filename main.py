import PySimpleGUI as sg
import requests
import time

# base variables
apiServerTestURL = "https://api.rawg.io/api/games/grand-theft-auto-v"
testResponse = requests.get(apiServerTestURL)

col = [
    [sg.Text("GameFinder", justification="center", font=("", 36))],
    [sg.Button("Check Connectivity", font=("", 16), auto_size_button=True, key="_CONN_CHECK_")],
    [sg.Output(size=(80, 20), font=("", 14))]
    ]

layout = [
    [sg.Column(col, element_justification="center")]
]

'''
def jsonCaller():
    apiServerURL = "https://api.rawg.io/api/games/grand-theft-auto-v"

    response = requests.get(apiServerURL)

    # check if server response, then get json
    if response.status_code != 200:
        print("[-] Can't connect to API Server, try again later.")
    else:
        print("[+] Successfully Connected to Server \n")
        dataJson = response.json()
        gameName = dataJson["name_original"]
        # description = dataJson["description_raw"]
        metacritic = dataJson["metacritic"]
        releaseDate = dataJson["released"]
        gameImg = dataJson["background_image"]

    print(gameName, metacritic, releaseDate, gameImg)
'''

# MainFrame
window = sg.Window("Game - Finder", layout)
checkEnable = True

def checkConnection():
    if testResponse.status_code != 200:
        print("[-] Can't connect to API Server, try again later.")
    else:
        print("[+] Successfully Connected to Server \n")

# MainLoop
while True:
    event, values = window.read() # write events/values in respective variables
    # end program wenn window is closed or button pressed
    if event == sg.WIN_CLOSED or event == "_EXIT_":
        break
    if event == "_CONN_CHECK_":
        checkConnection()
        window.Refresh()

window.close()