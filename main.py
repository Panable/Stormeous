import threading
import wmi
from PyQt5.QtCore import QTimer, QThread

from stormui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import pythoncom
import pyperclip
import re
import mi
import base64
import requests
import json
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def update_summoner(self, text):
        self.ui.summonerLabel.setText(text)

    def update_state(self, text):
        self.ui.gameState.setText(text)

    def bind_clipboard_button(self, method):
        self.ui.clipboardButton.clicked.connect(method)

    def bind_autoaccept_button(self, method):
        self.ui.autoAcceptToggle.clicked.connect(lambda: method(self.ui.autoAcceptToggle.isChecked()))

    def is_autoaccept(self):
        return self.ui.autoAcceptToggle.isChecked()

    def update_summonerbox(self, text):
        QtCore.QMetaObject.invokeMethod(self.ui.textBrowser, 'setText', QtCore.Qt.QueuedConnection,
                                        QtCore.Q_ARG(str, text))
        QtCore.QCoreApplication.processEvents()

    def reset_champselect(self):
        self.update_summonerbox("<H1>WAITING FOR CHAMPSELECT</H1>")


def toggle_autoaccept(state):
    print(state)


def copy_to_clipboard():
    print("copying to clipboard...")
    url = "https://www.op.gg/multisearch/" + "OCE" + "?summoners="+csvname;
    pyperclip.copy(url)


def make_request(port, auth_token, method, url):
    try:
        obj = requests.Session()
        obj.headers.update({'Authorization': 'Basic ' + auth_token})
        obj.headers.update({'Content-Type': 'application/json'})
        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
        if method == "GET":
            response = obj.get("https://127.0.0.1:" + str(port) + url, verify=False)
        elif method == "POST":
            response = obj.post("https://127.0.0.1:" + str(port) + url, verify=False)
        elif method == "PUT":
            response = obj.put("https://127.0.0.1:" + str(port) + url, verify=False)
        elif method == "DELETE":
            response = obj.delete("https://127.0.0.1:" + str(port) + url, verify=False)
        else:
            return ""
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return ""


csvname = ""

def test_logic():
    threading.Timer(1, test_logic).start()

    command_line = None

    with mi.Application() as a:
        with a.create_session(protocol=mi.PROTOCOL_WMIDCOM) as s:
            proc_name = U'notepad.exe'
            with s.exec_query(
                    U"root\\cimv2", U"select * from Win32_Process") as q:
                i = q.get_next_instance()
                while i is not None:
                    if i[U'name'].lower() == U"LeagueClientUx.exe".lower():
                        command_line = i[U'commandline']
                    i = q.get_next_instance()

    if command_line is None:
        return

    riot_token = ("riot:"+re.search('"--riotclient-auth-token=(.*)" "--riotclient-app-port', command_line).group(1)).encode("ISO-8859-1")
    client_token = ("riot:"+re.search('"--remoting-auth-token=(.*)" "--respawn-command', command_line).group(1)).encode("ISO-8859-1")
    riot_token = base64.b64encode(riot_token).decode()
    client_token = base64.b64encode(client_token).decode()
    riot_port = re.search('"--riotclient-app-port=(.*)" "--no-rads" "', command_line).group(1)
    client_port = re.search('"--app-port=(.*)" "--install-directory=', command_line).group(1)

    gameState = "/lol-gameflow/v1/gameflow-phase"
    summoner_name = "/lol-summoner/v1/current-summoner"
    champselect = "/chat/v5/participants/champ-select"
    acceptqueue = "/lol-matchmaking/v1/ready-check/accept"

    current_game_state = make_request(client_port, client_token, "GET", gameState)

    win.update_state(current_game_state)
    nameList = make_request(client_port, client_token, "GET", summoner_name)

    if "displayName" in nameList:
        name = json.loads(nameList)["displayName"]
        win.update_summoner(name)
    else:
        return

    if current_game_state == '"ReadyCheck"' and win.is_autoaccept():
        make_request(client_port, client_token, "POST", acceptqueue)

    if current_game_state != '"ChampSelect"':
        win.reset_champselect()
        return

    champions = make_request(riot_port, riot_token, "GET", champselect)
    data = json.loads(champions)
    participants = data["participants"]
    names = [participant["name"] for participant in participants]


    global csvname

    names_string = []
    for name in names:
        names_string.append(name)

    name_display_value = "<h1>" + "</h1>\n<h1>".join(names_string) + "</h1>"
    win.update_summonerbox(name_display_value)

    csvname = ",".join(names_string)


    #print("riot token:" + riot_token)
    #print("client token:" + client_token)
    #print("client port:" + client_port)
    #print("client_token" + client_token)
    #print("client_token" + client_token)


def logic(w):
    # threading.Timer(0.5, logic, [w]).start()

    if w is None:
        pythoncom.CoInitialize()
        w = wmi.WMI()

    name = "LeagueClientUx.exe"

    cmdline = None

    for process in w.Win32_Process():
        if process.Name == name:
            tmp1 = process.Commandline
            tmp2 = tmp1.split(' ', 1)
            args = tmp2[1]
            cmdline = args
            result = re.search('"--riotclient-auth-token=(.*)" "--riotclient-app-port', args)
            print(result.group(1))
            break
    if cmdline is not None:
        print("NOT NULL")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()

    win.reset_champselect()
    win.update_summoner("negro")
    win.bind_clipboard_button(copy_to_clipboard)
    win.bind_autoaccept_button(toggle_autoaccept)

    # logic(None)
    test_logic()
    sys.exit(app.exec_())
    sys.exit()
