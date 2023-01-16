import os
import threading
from PyQt5.QtCore import QTimer, QThread
from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip
import re
import base64
import requests
import json
import warnings
from subprocess import check_output


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 381)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStyleSheet("QLabel{\n"
                                 "color:black;\n"
                                 "minimumPointSize: 10\n"
                                 "width: parent.width\n"
                                 "height: parent.height\n"
                                 "fontSizeMode: Text.Fit\n"
                                 "anchors.top: label.bottom; anchors.bottom: parent.bottom;\n"
                                 "anchors.left: parent.left;\n"
                                 "anchors.topMargin: 5\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gameState = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gameState.setFont(font)
        self.gameState.setObjectName("gameState")
        self.verticalLayout_2.addWidget(self.gameState)
        self.clipboardButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.clipboardButton.setFont(font)
        self.clipboardButton.setObjectName("clipboardButton")
        self.verticalLayout_2.addWidget(self.clipboardButton)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(388, 233))
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.summonerLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.summonerLabel.setFont(font)
        self.summonerLabel.setStyleSheet("")
        self.summonerLabel.setScaledContents(False)
        self.summonerLabel.setObjectName("summonerLabel")
        self.horizontalLayout.addWidget(self.summonerLabel)
        self.autoAcceptToggle = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.autoAcceptToggle.setFont(font)
        self.autoAcceptToggle.setStyleSheet("")
        self.autoAcceptToggle.setObjectName("autoAcceptToggle")
        self.horizontalLayout.addWidget(self.autoAcceptToggle)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stormeous"))
        self.gameState.setText(_translate("MainWindow", "State: ?"))
        self.clipboardButton.setText(_translate("MainWindow", "Copy To Clipboard (OPGG)"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SUMMONER 1</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SUMMONER 2</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SUMMONER 3</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SUMMONER 4</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SUMMONER 5</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.summonerLabel.setText(_translate("MainWindow", "Summoner: ?"))
        self.autoAcceptToggle.setText(_translate("MainWindow", "Auto Accept"))


warnings.filterwarnings("ignore", category=DeprecationWarning)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        closed()
        event.accept()

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
    url = "https://www.op.gg/multisearch/" + "OCE" + "?summoners=" + csvname;
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


def logic():
    thread = threading.Timer(0.5, logic)
    thread.start()
    global running

    if not running:
        thread.cancel()

    cmd1 = 'pidof LeagueClientUx.exe'

    command_line = None

    cmd = 'ps -p $(pidof LeagueClientUx.exe) -o args'
    if os.system(cmd1) != 256:
        out = check_output(cmd, shell=True)
        command_line = out.decode().splitlines()[1]

    if command_line is None:
        return


    riot_token = ("riot:" + re.search('--riotclient-auth-token=(.*) --riotclient-app-port', command_line).group(
        1)).encode("ISO-8859-1")
    client_token = ("riot:" + re.search('--remoting-auth-token=(.*) --respawn-command', command_line).group(1)).encode(
        "ISO-8859-1")
    riot_token = base64.b64encode(riot_token).decode()
    client_token = base64.b64encode(client_token).decode()
    riot_port = re.search('--riotclient-app-port=(.*) --no-rads ', command_line).group(1)
    client_port = re.search('--app-port=(.*) --install-directory=', command_line).group(1)

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


running = True


def closed():
    global running
    running = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()

    win.reset_champselect()
    win.update_summoner("negro")
    win.bind_clipboard_button(copy_to_clipboard)
    win.bind_autoaccept_button(toggle_autoaccept)

    logic()
    sys.exit(app.exec_())
    sys.exit()
