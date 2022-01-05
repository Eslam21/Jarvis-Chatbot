#Jarvis Bot Team:
#Ziad Ahmed ElKady 202001598
#Eslam Ahmed Mohamed 202000039
#Anas Ahmed Hassan Sayed 202000005
#Youssef Hisham Abd elwahab 202000543

import time
from covid import Covid
import datetime
import random
import wolframalpha
import wikipedia
import pyttsx3
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import sys

#PyQt5 GUI
class MyWindow(QWidget):
    userInput = ""
    greeting = ""

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        greeting = "Good Morning !"

    elif hour >= 12 and hour < 18:
        greeting = "Good Afternoon !"
    else:
        greeting = "Good Evening !"

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(600,150,620,600)
        self.setWindowTitle("Jarvis Chat Bot")
        self.setWindowIcon(QtGui.QIcon("jarvislogo.png"))
        self.initUI()

    def initUI(self): #We put all Qt Variables here

        font="Bahnschrift"

        #Label For Sitting Background Color or Image
        self.bglabel = QtWidgets.QLabel(self)
        self.bglabel.setGeometry(0,0,1920,1080)
        self.bglabel.setStyleSheet("background-color:black")

        #Runs Gif
        self.giflabel = QtWidgets.QLabel(self)
        self.giflabel.setGeometry(-100,0,970,660)
        self.movie = QMovie("Motion exploration for AI system.gif")
        self.giflabel.setMovie(self.movie)
        self.movie.start()

        #Label For Jarvis Header
        self.jarvislabel = QtWidgets.QLabel(self)
        self.jarvislabel.setText("Jarvis")
        self.jarvislabel.setFont(QFont(font, 24))
        self.jarvislabel.setAlignment(Qt.AlignCenter)
        self.jarvislabel.setStyleSheet("color:white; background-color:turquoise")

        #Label That Contains Jarvis Answer
        self.label = QtWidgets.QLabel(self)
        self.label.setText(self.greeting+"\n\n"
            "Im Jarvis, a chatbot that can do alot of things.\n\n"
            "I can search and provide you with information about almost anything you ask me.\n\n"
            "I can recommend you a movie.\n\n"
            "I can also provide you information about covid-19 in any country in the world.\n\n"
            "And much more....")
        self.label.setFont(QFont(font, 12))
        self.label.setAlignment(Qt.AlignTop)
        self.label.setStyleSheet("border:2px solid white; color:white")
        self.label.setWordWrap(True)

        #Line Box That Takes UserInput
        self.line = QtWidgets.QLineEdit(self)
        self.line.setStyleSheet("border:2px solid white; color:white; background-color:black")
        self.line.setFont(QFont(font, 12))
        self.line.returnPressed.connect(self.send)

        #Window Layout
        layout = QVBoxLayout()
        layout.addWidget(self.jarvislabel)
        self.jarvislabel.setMaximumSize(1920,50)
        layout.addWidget(self.label)
        layout.addWidget(self.line)
        self.setLayout(layout)

    def JarvisDoSearch(self):
        self.changeLabel(self.greeting+"\n\n"
            "Im Jarvis, a chatbot that can do alot of things.\n\n"
            "I can search and provide you with information about almost anything you ask me.\n\n"
            "I can recommend you a movie.\n\n"
            "I can also provide you information about covid-19 in any country in the world.\n\n"
            "And much more....")
        input_list = self.userInput.upper().split()
        counter=0
        for i in input_list:
            self.changeLabel(i)
            if i == "RECOMMEND" or i == "MOVIE":
                self.Movie_recommendation()
                break
            elif i == "ENCRYPT" or i == "ENCODE":
                self.ceaser_encrypt()
                break
            elif i == "DECRYPT" or i == "DECODE":
                self.ceaser_decrypt()
                break
            elif i == "COVID" or i == "COVID-19" or i == "CORONA" or i == "VIRUS" or i == "COVID19" or i == "COVID 19":
                self.covido_bot()
                break
            elif i == "HELP" or i == "JARVIS" or i == "COMMANDS":
                self.help()
                break
            else:
                counter=counter+1

        if counter==len(input_list) and counter != 0:
            self.search_anything()

    def send(self):
        self.say(self.line.text())
        self.userInput=self.line.text()
        self.line.clear()
        self.JarvisDoSearch()

    def changeLabel(self,strr):
        # strrList=strr.split(".")
        # if type(strrList)==list:
        #     strr=""
        #     for i in strrList:
        #         strr=strr+"\n"+strrList[i]

        self.label.setText(strr)
        #self.label.adjustSize()

    def say(self,x):

        self.changeLabel(x)
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')

        engine.setProperty('rate', 190)
        voices = engine.getProperty('voices')  # getting details of current voice

        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        engine.say(x)
        engine.runAndWait()



    def startJarvis(self):

        self.say(self.greeting+"\n"
            "Im Jarvis, a chatbot that can do alot of things.\n"
            "I can search and provide you with information about almost anything you ask me.\n"
            "I can recommend you a movie.\n"
            "I can also provide you information about covid-19 in any country in the world.\n"
            "And much more....")

        self.JarvisDoSearch()

    def search_anything(self):
        x=self.userInput

        try:
            question = x
            if question == "":
                self.say("Please input something")
            else:
                # App id to let me access the data
                app_id = 'KUXWL9-5PXYG64KWH'

                # Instance of wolframalpha client class
                client = wolframalpha.Client(app_id)

                # Stores the response from wolframalpha
                res = client.query(question)

                # Includes only text from the response
                answer = next(res.results).text
                for i in answer:
                    x = answer.replace("Wolfram|Alpha.", "jarvis")  # to replace chatbot name
                self.say(x)
        except:
            # wiki part
            questiona = question
            try:
                print(wikipedia.summary(questiona))
                self.say(wikipedia.summary(questiona))
            except:
                try:
                    print("\n")
                    search_suggestion = wikipedia.search(questiona)
                    for number, letter in enumerate(search_suggestion):  # loop to put the suggestion and number
                        print(number + 1, "-", letter)
                        time.sleep(0.2)
                    suggestion_num = int("1")
                    if suggestion_num <= len(search_suggestion):
                        print(wikipedia.summary(search_suggestion[suggestion_num - 1]))
                        self.say(wikipedia.summary(search_suggestion[suggestion_num - 1]))  # index the suggestion number and search for it
                    else:
                        self.say("Sorry, I can't understand that :(")
                except:
                    return

    def ceaser_encrypt(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.changeLabel("Enter the message that you want to encrypt  :")
        msg = self.userInput
        msg = msg.lower()
        msg = msg.replace("encrypt","")
        msg = msg.replace("encode","")
        self.changeLabel("enter your key:")
        key = int("3")
        L = len(msg)

        encoded_msg = ""
        for i in range(L):
            char = msg[i]
            if char.islower():
                positon = alphabet.find(char)
                new_positon = (positon + key) % 26
                encoded_msg += alphabet[new_positon]
            else:
                encoded_msg += char

        self.say("Encrypted message: "+encoded_msg)

    def ceaser_decrypt(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        encrypted_msg = self.userInput
        encrypted_msg = encrypted_msg.lower()
        encrypted_msg = encrypted_msg.replace("decrypt","")
        encrypted_msg = encrypted_msg.replace("decode","")
        key = int("3")
        L = len(encrypted_msg)
        encrypted_msg = encrypted_msg.lower()
        decoded_msg = ""
        for i in range(L):
            char = encrypted_msg[i]
            if char.islower():
                positon = alphabet.find(char)
                new_positon = (positon - key) % 26
                decoded_msg += alphabet[new_positon]
            else:
                decoded_msg += char

        self.say("Decrypted message: "+decoded_msg)

    def Movie_recommendation(self):

        HORROR = ["The Grudge", "The Nun", "Us", "IT", "The Purge", "A Quiet Place", "Jigsaw", "Knock Knock",
                  "The Predator", "Alien: Covenant", "The Babysitter", "Insidious: The Last Key", "The Turning"]
        SCIENCEFICTION = ["Bloodshot", "Gemini Man", "Assassins Creed", "War for the Planet of the Apes", "Underwater",
                          "Extinction", "Terminator: Dark Fate", "Rampage", "Godzilla: King of the Monsters",
                          "Geostorm", "Jurassic World: Fallen Kingdom", "Spider-Man: Far From Home", "Justice League",
                          "The Martian"]
        COMEDY = ["The Hitman's Bodyguard", "The Mask", "The Secret Life of Walter Mitty", "Game Night",
                  "Jumanji: The Next Level", "Baywatch", "Let's Be Cops", " School of Rock "]
        ACTION = ["The Matrix", "Assassins", "John Wick", "Harley Quinn: Birds of Prey", "Gods of Egypt", "Baby Driver",
                  "Rambo: Last Blood", "The Meg"]
        DRAMA = ["Braveheart", "Joker", "Life Of Pi", "The Man Who Knew Infinity", "The Way Back", "The King",
                 "A Star is Born", "Wonder", "The Revenant", "The Founder"]
        ROMANCE = ["Forrest Gump", "Titanic", "The Bodyguard", "Chemical Hearts", "After We Collided", "Let It Snow",
                   "The Fault in Our Stars", "Zero", "La La Land", "Marriage Story", "The Shape Of Water"]

        ALL_Genres=HORROR+SCIENCEFICTION+COMEDY+ACTION+DRAMA+ROMANCE

        self.say("I recommend you to watch: " + random.choice(ALL_Genres))

    def covido_bot(self):
        try:
            self.covid_data(self.userInput)
        except:
            self.say("Error 201! Something wrong happened :(")
            return

    def covid_data(self, x):
        # to get data from worldometers.info
        x = x.lower()
        x = x.replace("corona virus", "")
        x = x.replace("corona","")
        x = x.replace("covid-19", "")
        x = x.replace("covid", "")
        x = x.replace("19", "")
        x = x.replace("cases", "")
        x = x.replace(" ", "")

        covid = Covid(source="worldometers")
        c = covid.get_status_by_country_name(x)

        x=""
        for key, value in c.items():  # to print it line by line
            x = x+'\n'+str(key)+' : '+str(value)
        self.changeLabel(x)

    def help(self):
        self.changeLabel(self.say("Try asking me the following:\n"
                                  "-Recommend a movie\n"
                                  "-Corona virus cases in *country*\n"
                                  "-Encrypt *message*\n"
                                  "-Decrypt *message*\n"
                                  "-Ask me to solve math equations\n"
                                  "-Ask me about the definition of any English word"))
        self.changeLabel("Try asking me the following:\n"
                         "-Recommend a movie\n"
                         "-Corona virus cases in *country*\n"
                         "-Encrypt *message*\n"
                         "-Decrypt *message*\n"
                         "-Ask me to solve math equations\n"
                         "-Ask me about the defination of any English word")


def window(): #Responsible for showing the GUI window
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    win.startJarvis() #Jarvis Welcome
    sys.exit(app.exec())


window() #Function called for showing the window






