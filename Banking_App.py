# TODO: USE:
# WHILE TRUE
# INPUT X
# CLASSES X
# METHOD X
# PROPERTIES x
# OPEN() x

import math
import datetime
# TODO: CLASS BASED BANKING APP


class BankingApp:
    with open("account_ledger.txt", "w") as account_ledger:
        init_deposit = input("Please make an initial deposit: ")
        account_bal = float(init_deposit)
        account_start = datetime.datetime.now()
        ledger = account_ledger.write(
            f"\n {init_deposit} starting balance {account_start.strftime('%c')}")
    print(account_bal)  # initial account balance established

    # TODO: WITHDRAWAL

    def select(self):
        pick = input(
            "Would you like to \n(W): Withdraw from your account \n(D): Deposit to your account or \n(V): View your account?")
        return pick

    def withdrawal(self):
        deduct = input("How much would you like to withdraw?")
        new_balance = self.account_bal - float(deduct)
        print(new_balance)
        # change = str(0 - float(deduct))
        # TODO: WRITE METHOD RESULT TO A PYTHON LEDGER FILE
        ledger = open("account_ledger.txt", "a")
        ledger.write(f"\n-{deduct}")
        new_balance_f = new_balance.format('%c')
        ledger.write(f"\n {str(new_balance_f)} balance")
        ledger.close()

    # TODO: DEPOSIT METHODS
    def deposit(self):
        add = input("How much would you like to deposit?")
        new_balance = self.account_bal + float(add)
        print(new_balance)
        ledger = open("account_ledger.txt", "a")
        ledger.write(f"\n+{add}")
        new_balance_f = str(new_balance)
        bal = (f"\n {new_balance_f:.2f} balance")
        ledger.write(bal.format(bal))
        ledger.close()

    def view(self):
        with open("account_ledger.txt", "r") as account:
            account_view = account.read()
        print(account_view)


atm = BankingApp()

while True:
    atm_action = atm.select()

    if atm_action == 'w':
        atm.withdrawal()
    elif atm_action == 'd':
        atm.deposit()
    elif atm_action == 'v':
        atm.view()
    else:
        print("Please select the letter next to the action you wish to take \nW: Withdraw \nD: Deposit \nV: View account")
