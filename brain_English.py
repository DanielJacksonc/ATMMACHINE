from brain import Atm
from c_information import customers_data
from turtle import Turtle, Screen
import time


t = Turtle()
t.penup()
t.color("Yellow")
t.hideturtle()
t.goto(-200, 50)
class AtmEnglish(Atm):
    def __init__(self):
        self.money = []
        self.rate = []
        self.name_list = []
        self.password = []

        super().__init__()
        # self.screen = Screen()
    def transaction(self):

        screen = Screen()
        insert_card = screen.textinput(title="Your Card", prompt="Please insert your card or your name on card").title()
        for customers in customers_data:
            name = customers["name"]
            password = customers["password"]
            amount = float(customers["Amount"])
            self.money.append(amount)
            self.name_list.append(name)
            self.password.append(password)
            if insert_card in self.name_list:
                self.data.append(insert_card)

                t.write(f"\nHello {self.data}, \nwelcome to DAN BANK", font=("courier", 22, "normal"))
                card_password = screen.textinput(title="password", prompt="Please put your password digit here")
                if card_password == customers["password"]:
                    t.write("You are all set....", font=("courier", 22, "normal"))
                    time.sleep(2)
                    debit_credit = screen.textinput(title="Choose transaction", prompt="Press 1 for Debit transaction"
                                                                                       " and 2 for Credit transaction."
                                         " or 3 for account information. press 0 to cancel").title()
                    if debit_credit == "1":
                        print(f"ok, this is your account balance ${amount}")
                        debit_money = float(screen.textinput(title="Debit", prompt="Please input amount to collect"))
                        print("processing transaction..........\n")
                        time.sleep(3)
                        if debit_money >= amount:
                            print(f"Insufficient fund, you current amount is: ${amount}\n\n")
                        elif debit_money <= customers["Amount"]:
                            self.money -= debit_money
                            print(f"Successful,take your ${debit_money}. your current balance is ${amount}\n")

                    elif debit_credit == "2":
                        print(f"ok, this is your account balance ${amount}")
                        credit_money = float(screen.textinput(title="Credit", prompt="Please input amount to Credit"))
                        print("processing transaction..........\n")
                        time.sleep(3)
                        self.money += credit_money

                        print(f"Successful, credited with {credit_money}, current balance: ${self.money}\n")

                    elif debit_credit == "3":
                        print("processing transaction..........\n")
                        time.sleep(3)
                        print(f"{name}, your current balance is ${amount} \n")

                    elif debit_credit == "0":
                        if screen.textinput(title=f"Rate Us {name}", prompt="Would you want to take a survey?").lower() == "yes":
                            rate = int(input("Please rate us here from 1 - 5"))
                            if rate == "5":
                                rate += 5
                                print(f"Thank you {name}")
                            else:
                                break
                        else:
                            print(f"{name},Thanks for banking with us")
                        break
                    else:
                        print("Not a provided option.\n")
                    break

                else:
                    print("This is a wrong pin")
                    break
        else:
            print("incorrect name")
        if screen.textinput(title="Perform more Transaction? ", prompt="Press 1 if you want to perform another transaction") == "1":
            pass

        else:
            exit()

