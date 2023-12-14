from turtle import Turtle, Screen
from brain import Atm
from brain_igbo import ATMigbo
from brain_English import AtmEnglish

screen = Screen()
screen.setup(height=800, width=1000)
screen.bgpic("J.gif")
greet = Atm()
greet.greeting()
greet.choose_language("question")
transaction_in_process = True
while transaction_in_process:

    if greet.choose == "1":
        customer_transaction = AtmEnglish()
        customer_transaction.transaction()
    elif greet.choose == "2":
        customer_transaction = ATMigbo()
        customer_transaction.transaction()

    else:
        print("We don't have that option")
