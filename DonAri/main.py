import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql.cursors
import random

loginForm = uic.loadUiType("loginMenu.ui")[0]
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
quizStartForm = uic.loadUiType("quizStart.ui")[0]
quizForm = uic.loadUiType("quizMenu.ui")[0]

class LoginWindow(QMainWindow, loginForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("로그인")

        self.loginButton.clicked.connect(self.login)

    def login(self):
        self.same = 0
        if self.nameEdit.text() != "" and self.classEdit.text() != "":
            conn = pymysql.connect(host='183.99.87.90',
                                   user='root',
                                   password='swhacademy!',
                                   db='SeanLee',
                                   charset='utf8')
            try:
                with conn.cursor() as cursor:
                    sql = "SELECT classroom FROM LadderDongAri;"
                    cursor.execute(sql)
                    conn.commit()
                    results = cursor.fetchall()
                    for result in results:
                        if result[0] == int(self.classEdit.text()):
                            self.same = 1
            finally:
                conn.close()
            if self.same == 0:
                conn = pymysql.connect(host='183.99.87.90',
                                           user='root',
                                           password='swhacademy!',
                                           db='SeanLee',
                                           charset='utf8')
                try:
                    with conn.cursor() as cursor:
                        sql = 'insert into LadderDongAri(NAME, score, quiz, clicker, catchmind, classroom) values ("%s", 0, 3, 3, 3, %s);' % (self.nameEdit.text(), self.classEdit.text())
                        cursor.execute(sql)
                        conn.commit()
                finally:
                    conn.close()
            global name
            global classroom
            name = self.nameEdit.text()
            classroom = int(self.classEdit.text())
            self.hide()
            startWindow.show()
        else:
            QMessageBox.about(self, "Error", "이름 또는 학번을\n잘못 입력하셨습니다.")

class StartWindow(QMainWindow, startForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("시작")

        self.gameButton.clicked.connect(self.game)
        self.infoButton.clicked.connect(self.info)
        self.creditButton.clicked.connect(self.credit)
        self.ladderButton.clicked.connect(self.ladder)

    def game(self):
        self.hide()
        gameWindow.show()

    def info(self):
        self.hide()
        infoWindow.show()

    def credit(self):
        QMessageBox.about(self, "TIP", "코딩\n이수형, 방현준(노력이라도 함)\n\n아이디어 참여\n기초 프로그래밍 동아리")

    def ladder(self):
        self.nameList = []
        self.scoreList = []
        conn = pymysql.connect(host='183.99.87.90',
                               user='root',
                               password='swhacademy!',
                               db='SeanLee',
                               charset='utf8')
        try:
            with conn.cursor() as cursor:
                sql = "SELECT NAME, score FROM LadderDongAri ORDER BY score DESC LIMIT 3;"
                cursor.execute(sql)
                conn.commit()
                results = cursor.fetchall()
                for result in results:
                    self.nameList.append(result[0])
                    self.scoreList.append(result[1])
        finally:
            conn.close()
        QMessageBox.about(self, "랭킹", "1위 : %s (%d점)\n2위 : %s (%d점)\n3위 : %s (%d점)" % (self.nameList[0], self.scoreList[0], self.nameList[1], self.scoreList[1], self.nameList[2], self.scoreList[2]))

class GameWindow(QMainWindow, gameForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("게임")

        self.quizButton.clicked.connect(self.quiz)
        self.backButton.clicked.connect(self.back)

    def quiz(self):
        self.hide()
        quizStartWindow.show()

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

class QuizStartWindow(QMainWindow, quizStartForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("퀴즈 시작")
        self.tries = 0

        self.quizButton.clicked.connect(self.quizStart)
        self.ruleButton.clicked.connect(self.rules)
        self.returnButton.clicked.connect(self.ret)

    def ret(self):
        self.hide()
        gameWindow.show()

    def rules(self):
        QMessageBox.about(self, "규칙", "1. 퀴즈는 정보에서 확인하실 수 있는 정보에서 문제가 출제됩니다.\n2. 개인당 최대 3회까지 참여 가능합니다.")

    def quizStart(self):
        conn = pymysql.connect(host='183.99.87.90',
                               user='root',
                               password='swhacademy!',
                               db='SeanLee',
                               charset='utf8')
        try:
            with conn.cursor() as cursor:
                sql = "SELECT quiz FROM LadderDongAri WHERE classroom = %d;" % classroom
                cursor.execute(sql)
                conn.commit()
                results = cursor.fetchall()
                self.tries = results[0][0]
        finally:
            conn.close()

        if self.tries == 0:
            QMessageBox.about(self, "WARNING", "퀴즈는 개인당 총 3회만 참여 가능합니다!")
        else:
            self.hide()
            global quizWindow
            quizWindow = QuizWindow()
            quizWindow.show()

def getQuiz():
    conn = pymysql.connect(host='183.99.87.90',
                           user='root',
                           password='swhacademy!',
                           db='SeanLee',
                           charset='utf8')

    r = 0
    ranList = []
    quizList = []
    ans1List = []
    ans2List = []
    ans3List = []
    ans4List = []
    answerList = []

    while r < 10:
        ran = random.randint(0, 29)
        while ran in ranList:
            ran = random.randint(0, 29)
        ranList.append(ran)
        r += 1

    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM donQuiz;"
            cursor.execute(sql)
            conn.commit()
            results = cursor.fetchall()
            for a in ranList:
                quizList.append(results[a][0])
                ans1List.append(results[a][1])
                ans2List.append(results[a][2])
                ans3List.append(results[a][3])
                ans4List.append(results[a][4])
                answerList.append(results[a][5])
    finally:
        conn.close()
    return (ranList, quizList, ans1List, ans2List, ans3List, ans4List, answerList)


class QuizWindow(QMainWindow, quizForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("퀴즈")
        self.prob = 0
        self.ans = 0
        self.rep = 0

        self.quizInfo = getQuiz()

        self.ranList = self.quizInfo[0]
        self.quizList = self.quizInfo[1]
        self.ans1List = self.quizInfo[2]
        self.ans2List = self.quizInfo[3]
        self.ans3List = self.quizInfo[4]
        self.ans4List = self.quizInfo[5]
        self.answerList = self.quizInfo[6]

        self.ans1.clicked.connect(self.ans1button)
        self.ans2.clicked.connect(self.ans2button)
        self.ans3.clicked.connect(self.ans3button)
        self.ans4.clicked.connect(self.ans4button)

        self.repQuiz() # self.prob - 현재 문항, self.ans = 현재 정답수

    def repQuiz(self):
        if self.prob < 10:
            self.correct.setText("정답 수 : %d" % (self.ans))
            self.quizNum.setText("문항 %d" % (self.prob+1))
            self.quiz.setText(self.quizList[self.prob])
            self.ans1.setText(self.ans1List[self.prob])
            self.ans2.setText(self.ans2List[self.prob])
            self.ans3.setText(self.ans3List[self.prob])
            self.ans4.setText(self.ans4List[self.prob])
            self.current = self.answerList[self.prob]
        else:
            conn = pymysql.connect(host='183.99.87.90',
                                   user='root',
                                   password='swhacademy!',
                                   db='SeanLee',
                                   charset='utf8')
            try:
                with conn.cursor() as cursor:
                    sql = "SELECT score FROM LadderDongAri WHERE classroom = %d;" % (classroom)
                    cursor.execute(sql)
                    conn.commit()
                    results = cursor.fetchall()
                    self.score = results[0][0]

                    sql = "SELECT quiz FROM LadderDongAri WHERE classroom = %d;" % classroom
                    cursor.execute(sql)
                    conn.commit()
                    results = cursor.fetchall()
                    self.tries = results[0][0]

            finally:
                conn.close()

            conn = pymysql.connect(host='183.99.87.90',
                                   user='root',
                                   password='swhacademy!',
                                   db='SeanLee',
                                   charset='utf8')
            try:
                with conn.cursor() as cursor:
                    sql = "update LadderDongAri set score = %d where classroom = %d;" % (self.score + (self.ans * 10), classroom, )
                    cursor.execute(sql)
                    conn.commit()

                    sql = "update LadderDongAri set quiz = %d where classroom = %d;" % (self.tries - 1, classroom)  #
                    cursor.execute(sql)
                    conn.commit()
            finally:
                conn.close()
            self.hide()
            quizStartWindow.show()

    def ans1button(self):
        if self.current == 1:
            self.ans += 1
            self.prob += 1
            self.repQuiz()
        else:
            self.prob += 1
            self.repQuiz()

    def ans2button(self):
        if self.current == 2:
            self.ans += 1
            self.prob += 1
            self.repQuiz()
        else:
            self.prob += 1
            self.repQuiz()

    def ans3button(self):
        if self.current == 3:
            self.ans += 1
            self.prob += 1
            self.repQuiz()
        else:
            self.prob += 1
            self.repQuiz()

    def ans4button(self):
        if self.current == 4:
            self.ans += 1
            self.prob += 1
            self.repQuiz()
        else:
            self.prob += 1
            self.repQuiz()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    loginWindow = LoginWindow()
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
    quizStartWindow = QuizStartWindow()

    loginWindow.show()
    sys.exit(app.exec_())