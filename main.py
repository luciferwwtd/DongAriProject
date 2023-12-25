import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

startForm = uic.loadUiType("StartMenu.ui")[0]
gameForm = uic.loadUiType("GameMenu.ui")[0]
infoForm = uic.loadUiType("infoMenu.ui")[0]
plasticForm = uic.loadUiType("plasticMenu.ui")[0]
vinylForm = uic.loadUiType("vinylMenu.ui")[0]
paperForm = uic.loadUiType("paperMenu.ui")[0]
paperBagForm = uic.loadUiType("paperBagMenu.ui")[0]
canForm = uic.loadUiType("canMenu.ui")[0]
glassForm = uic.loadUiType("glassMenu.ui")[0]
elecForm = uic.loadUiType("elecMenu.ui")[0]
etcForm = uic.loadUiType("etcMenu.ui")[0]


class StartWindow(QMainWindow, startForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("시작")

        self.gameButton.clicked.connect(self.game)
        self.infoButton.clicked.connect(self.info)

    def game(self):
        self.hide()
        gameWindow.show()

    def info(self):
        self.hide()
        infoWindow.show()

class GameWindow(QMainWindow, gameForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("게임")

        self.quizButton.clicked.connect(self.quiz)
        self.clickerButton.clicked.connect(self.clicker)
        self.catchmindButton.clicked.connect(self.catchmind)
        self.backButton.clicked.connect(self.back)

    def quiz(self):
        print("quiz")

    def clicker(self):
        print("clicker")

    def catchmind(self):
        print("catchmind")

    def back(self):
        self.hide()
        startWindow.show()

class InfoWindow(QMainWindow, infoForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("정보")

        self.envButton.clicked.connect(self.env)
        self.ecyceButton.clicked.connect(self.ecyce)
        self.backButton.clicked.connect(self.back)

    def env(self):
        print("env")

    def ecyce(self):
        self.hide()
        plasticWindow.show()

    def back(self):
        self.hide()
        startWindow.show()

class PlasticWindow(QMainWindow, plasticForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("플라스틱류")

        self.canButton.clicked.connect(self.can)
        self.elecButton.clicked.connect(self.elec)
        self.etcButton.clicked.connect(self.etc)
        self.glassButton.clicked.connect(self.glass)
        self.paperBagButton.clicked.connect(self.paperBag)
        self.paperButton.clicked.connect(self.paper)
        self.plasticButton.clicked.connect(self.plastic)
        self.vinylButton.clicked.connect(self.vinyl)
        self.backButton.clicked.connect(self.back)

    def can(self):
        self.hide()
        canWindow.show()

    def elec(self):
        self.hide()
        elecWindow.show()

    def etc(self):
        self.hide()
        etcWindow.show()

    def glass(self):
        self.hide()
        glassWindow.show()

    def paperBag(self):
        self.hide()
        paperBagWindow.show()

    def paper(self):
        self.hide()
        paperWindow.show()

    def plastic(self):
        self.hide()
        plasticWindow.show()

    def vinyl(self):
        self.hide()
        vinylWindow.show()

    def back(self):
        self.hide()
        infoWindow.show()

class VinylWindow(QMainWindow, vinylForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("비닐류")

        self.canButton.clicked.connect(self.can)
        self.elecButton.clicked.connect(self.elec)
        self.etcButton.clicked.connect(self.etc)
        self.glassButton.clicked.connect(self.glass)
        self.paperBagButton.clicked.connect(self.paperBag)
        self.paperButton.clicked.connect(self.paper)
        self.plasticButton.clicked.connect(self.plastic)
        self.vinylButton.clicked.connect(self.vinyl)
        self.backButton.clicked.connect(self.back)

    def can(self):
        self.hide()
        canWindow.show()

    def elec(self):
        self.hide()
        elecWindow.show()

    def etc(self):
        self.hide()
        etcWindow.show()

    def glass(self):
        self.hide()
        glassWindow.show()

    def paperBag(self):
        self.hide()
        paperBagWindow.show()

    def paper(self):
        self.hide()
        paperWindow.show()

    def plastic(self):
        self.hide()
        plasticWindow.show()

    def vinyl(self):
        self.hide()
        vinylWindow.show()

    def back(self):
        self.hide()
        infoWindow.show()

class PaperWindow(QMainWindow, paperForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("종이류")

        self.canButton.clicked.connect(self.can)
        self.elecButton.clicked.connect(self.elec)
        self.etcButton.clicked.connect(self.etc)
        self.glassButton.clicked.connect(self.glass)
        self.paperBagButton.clicked.connect(self.paperBag)
        self.paperButton.clicked.connect(self.paper)
        self.plasticButton.clicked.connect(self.plastic)
        self.vinylButton.clicked.connect(self.vinyl)
        self.backButton.clicked.connect(self.back)

    def can(self):
        self.hide()
        canWindow.show()

    def elec(self):
        self.hide()
        elecWindow.show()

    def etc(self):
        self.hide()
        etcWindow.show()

    def glass(self):
        self.hide()
        glassWindow.show()

    def paperBag(self):
        self.hide()
        paperBagWindow.show()

    def paper(self):
        self.hide()
        paperWindow.show()

    def plastic(self):
        self.hide()
        plasticWindow.show()

    def vinyl(self):
        self.hide()
        vinylWindow.show()

    def back(self):
        self.hide()
        infoWindow.show()

class PaperBagWindow(QMainWindow, paperBagForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("종이팩류")

        self.canButton.clicked.connect(self.can)
        self.elecButton.clicked.connect(self.elec)
        self.etcButton.clicked.connect(self.etc)
        self.glassButton.clicked.connect(self.glass)
        self.paperBagButton.clicked.connect(self.paperBag)
        self.paperButton.clicked.connect(self.paper)
        self.plasticButton.clicked.connect(self.plastic)
        self.vinylButton.clicked.connect(self.vinyl)
        self.backButton.clicked.connect(self.back)

    def can(self):
        self.hide()
        canWindow.show()

    def elec(self):
        self.hide()
        elecWindow.show()

    def etc(self):
        self.hide()
        etcWindow.show()

    def glass(self):
        self.hide()
        glassWindow.show()

    def paperBag(self):
        self.hide()
        paperBagWindow.show()

    def paper(self):
        self.hide()
        paperWindow.show()

    def plastic(self):
        self.hide()
        plasticWindow.show()

    def vinyl(self):
        self.hide()
        vinylWindow.show()

    def back(self):
        self.hide()
        infoWindow.show()

class CanWindow(QMainWindow, canForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("캔류")

        self.canButton.clicked.connect(self.can)
        self.elecButton.clicked.connect(self.elec)
        self.etcButton.clicked.connect(self.etc)
        self.glassButton.clicked.connect(self.glass)
        self.paperBagButton.clicked.connect(self.paperBag)
        self.paperButton.clicked.connect(self.paper)
        self.plasticButton.clicked.connect(self.plastic)
        self.vinylButton.clicked.connect(self.vinyl)
        self.backButton.clicked.connect(self.back)

    def can(self):
        self.hide()
        canWindow.show()

    def elec(self):
        self.hide()
        elecWindow.show()

    def etc(self):
        self.hide()
        etcWindow.show()

    def glass(self):
        self.hide()
        glassWindow.show()

    def paperBag(self):
        self.hide()
        paperBagWindow.show()

    def paper(self):
        self.hide()
        paperWindow.show()

    def plastic(self):
        self.hide()
        plasticWindow.show()

    def vinyl(self):
        self.hide()
        vinylWindow.show()

    def back(self):
        self.hide()
        infoWindow.show()

class GlassWindow(QMainWindow, glassForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("유리병류")

        self.canButton.clicked.connect(self.can)
        self.elecButton.clicked.connect(self.elec)
        self.etcButton.clicked.connect(self.etc)
        self.glassButton.clicked.connect(self.glass)
        self.paperBagButton.clicked.connect(self.paperBag)
        self.paperButton.clicked.connect(self.paper)
        self.plasticButton.clicked.connect(self.plastic)
        self.vinylButton.clicked.connect(self.vinyl)
        self.backButton.clicked.connect(self.back)

    def can(self):
        self.hide()
        canWindow.show()

    def elec(self):
        self.hide()
        elecWindow.show()

    def etc(self):
        self.hide()
        etcWindow.show()

    def glass(self):
        self.hide()
        glassWindow.show()

    def paperBag(self):
        self.hide()
        paperBagWindow.show()

    def paper(self):
        self.hide()
        paperWindow.show()

    def plastic(self):
        self.hide()
        plasticWindow.show()

    def vinyl(self):
        self.hide()
        vinylWindow.show()

    def back(self):
        self.hide()
        infoWindow.show()

class ElecWindow(QMainWindow, elecForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("폐전자제품")

        self.canButton.clicked.connect(self.can)
        self.elecButton.clicked.connect(self.elec)
        self.etcButton.clicked.connect(self.etc)
        self.glassButton.clicked.connect(self.glass)
        self.paperBagButton.clicked.connect(self.paperBag)
        self.paperButton.clicked.connect(self.paper)
        self.plasticButton.clicked.connect(self.plastic)
        self.vinylButton.clicked.connect(self.vinyl)
        self.backButton.clicked.connect(self.back)
        self.tipButton.clicked.connect(self.tip)

    def can(self):
        self.hide()
        canWindow.show()

    def elec(self):
        self.hide()
        elecWindow.show()

    def etc(self):
        self.hide()
        etcWindow.show()

    def glass(self):
        self.hide()
        glassWindow.show()

    def paperBag(self):
        self.hide()
        paperBagWindow.show()

    def paper(self):
        self.hide()
        paperWindow.show()

    def plastic(self):
        self.hide()
        plasticWindow.show()

    def vinyl(self):
        self.hide()
        vinylWindow.show()

    def back(self):
        self.hide()
        infoWindow.show()

    def tip(self):
        QMessageBox.about(self, "TIP", "대형폐가전 무상방문수거 서비스\n콜센터 : 1599-0903\n인터넷 : http://www.15990903.or.kr")

class EtcWindow(QMainWindow, etcForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("기타")

        self.canButton.clicked.connect(self.can)
        self.elecButton.clicked.connect(self.elec)
        self.etcButton.clicked.connect(self.etc)
        self.glassButton.clicked.connect(self.glass)
        self.paperBagButton.clicked.connect(self.paperBag)
        self.paperButton.clicked.connect(self.paper)
        self.plasticButton.clicked.connect(self.plastic)
        self.vinylButton.clicked.connect(self.vinyl)
        self.backButton.clicked.connect(self.back)

    def can(self):
        self.hide()
        canWindow.show()

    def elec(self):
        self.hide()
        elecWindow.show()

    def etc(self):
        self.hide()
        etcWindow.show()

    def glass(self):
        self.hide()
        glassWindow.show()

    def paperBag(self):
        self.hide()
        paperBagWindow.show()

    def paper(self):
        self.hide()
        paperWindow.show()

    def plastic(self):
        self.hide()
        plasticWindow.show()

    def vinyl(self):
        self.hide()
        vinylWindow.show()

    def back(self):
        self.hide()
        infoWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    startWindow = StartWindow()
    gameWindow = GameWindow()
    infoWindow = InfoWindow()
    plasticWindow = PlasticWindow()
    vinylWindow = VinylWindow()
    paperWindow = PaperWindow()
    paperBagWindow = PaperBagWindow()
    canWindow = CanWindow()
    glassWindow = GlassWindow()
    elecWindow = ElecWindow()
    etcWindow = EtcWindow()

    startWindow.show()
    sys.exit(app.exec_())