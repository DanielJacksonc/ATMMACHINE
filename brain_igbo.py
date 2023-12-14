import time
from brain import Atm
from c_information import customers_data


class ATMigbo(Atm):
    def __init__(self):
        self.money = []
        self.rate = []
        self.name_list = []
        self.password = []

        super().__init__()

    def transaction(self):
        insert_card = input("Biko Tinye aha gi m'obu akara ego gi \n").title()
        for customers in customers_data:
            name = customers["name"]
            password = customers["password"]
            amount = customers["Amount"]
            self.money.append(amount)
            self.name_list.append(name)
            self.password.append(password)
            if insert_card in self.name_list:
                self.data.append(insert_card)
                print(f"\nEzigbo mmadu {self.data}, Nnoo na DAN BANK\n")
                card_password = int(input("Biko Tinye pinu akara ego gi ebea\n"))
                if card_password == customers["password"]:
                    print("Dalu, ngwa chere nwa ntiti.......\n")
                    time.sleep(3)
                    debit_credit = input("Pia 1 maka ndoro ego, pia 2 maka itinye ego."
                                         " ma pia 3 maka imata maka akantu gi. pia 0 to ma ichoro ikagbu ya. \n ")
                    if debit_credit == "1":
                        print(f"odimma, Ego gi foduru ${amount}")
                        debit_money = float(input("Ngwa, tinye ego ole ichoro isere \n "))
                        print("chere ka anyi nyere gi aka..........\n")
                        time.sleep(3)
                        if debit_money >= amount:
                            print(f"Ego gi ezughi ezi, ego gi foduru nani: ${amount}\n\n")
                        elif debit_money <= customers["Amount"]:
                            amount -= debit_money
                            print(f"Aha!! ,were ${debit_money} gi. ego gi foduru ${amount}\n")

                    elif debit_credit == "2":
                        print(f"odimma, ihea bu ego ole foduru gi na akantu gi ${amount}\n")
                        credit_money = float(input("Biko, Tinye ego ole ichoro itinye\n"))
                        print("chere..........\n")
                        time.sleep(3)
                        amount += credit_money

                        print(f"Ahah!!, etinye goro gi ${credit_money} n'akantu gi , ego gi buzi: ${amount}\n")

                    elif debit_credit == "3":
                        print(f"{name}, ego gi foduru bu ${amount} \n")

                    elif debit_credit == "0":
                        if input(f"{name}, O ga amasi gi igwa anyi otu anyi si mee? \n").lower() == "yes":
                            rate = int(input("ngwa tinye site na 1 - 5\n"))
                            if rate == "5":
                                rate += 5
                                print(f"Imela ezigbo mmadu {name}\n")
                            else:
                                break
                        else:
                            print(f"{name},Obi di anyi mma na inonyere anyi\n")
                        break
                    else:
                        print("Ewoo!! anyi enweghi ihe ichoro.\n")
                    break

                else:
                    print("akara gi amakoghi\n")
                    break
        else:
            print("aha gi adabchaghi, nwa ozo\n")

        if input("Pia 1 oburu na ichoro ime ihe ozo\n") == "1":
            pass

        else:
            exit()
