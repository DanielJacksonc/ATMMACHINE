from turtle import clear
from turtle import Turtle,Screen
import time

screen = Screen()



class Atm:
    def __init__(self):
        self.data = []
        self.password = []

    def greeting(self):
        t = Turtle()
        t.penup()
        t.color("Yellow")
        t.hideturtle()
        t.goto(-300, -50)
        t.write("Hi Esteemed Customer, Nno onye oma anyi,\n       ibiala? welcome to our bank    "
                "      \n            ..........", font=("courier", 22, "normal"))
        time.sleep(3)
        t.clear()

    def choose_language(self, choose):

        self.choose = screen.textinput(title="Choose language", prompt="Please choose 1 for English or 2 for Igbo").lower()
        time.sleep(1)

