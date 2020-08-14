import PySimpleGUI as sg
import requests
import time

# base variables
apiServerTestURL = "https://api.rawg.io/api/games/grand-theft-auto-v"
testResponse = requests.get(apiServerTestURL)

col = [
    [sg.Text("GameFinder", justification="center", font=("", 36))],
    [sg.Input("", key="_INPUT_"), sg.Button("Search", key="_SEARCH_")],    
    [sg.Output(size=(120, 30), font=("", 12), key="_OUTPUT_")],
    [sg.Image(key="_IMAGE_")],
    [sg.Button("Check Connectivity", font=("", 16), auto_size_button=True, key="_CONN_CHECK_"),
    sg.Button("Exit", font=("", 16), auto_size_button=True, key="_EXIT_")]
    ]

layout = [
    [sg.Column(col, element_justification="center")]
]

# MainFrame
window = sg.Window("Game - Finder", layout).finalize()
window["_OUTPUT_"].TKOut.output.config(wrap='word')
checkEnable = True

def checkConnection():
    if testResponse.status_code != 200:
        print("\n[-] Can't connect to API Server, try again later.")
    else:
        print("\n[+] Successfully Connected to Server")

def checkGame(GameName):
    window.FindElement("_OUTPUT_").Update("")
    gameResponse = requests.get("https://api.rawg.io/api/games/" + GameName.replace(" ", "-"))
    dataJson = gameResponse.json()
    if gameResponse.status_code != 200:
        print("[-] Can't find game, check spelling or try again later.")
    else:
        print("[+] ===== Found Game =====")
        print("\nGamename: " + dataJson["name_original"])
        print("\nDescription: " + dataJson["description_raw"])
        try:
            print("\nMetacritic Score: " + str(dataJson["metacritic"]))
        except:
            print("\nCould not find Metacritic Score")
        print("\nRelease Date: " + dataJson["released"])
        
# MainLoop
while True:
    event, values = window.read() # write events/values in respective variables
    # end program wenn window is closed or button pressed
    if event == sg.WIN_CLOSED or event == "_EXIT_":
        break
    if event == "_CONN_CHECK_":
        checkConnection()
        window.Refresh()
    if event == "_SEARCH_":
        checkGame(values["_INPUT_"])
        window.Refresh()

window.close()