import datetime


class BankingApp:
    with open("account_ledger.txt", "w") as account_ledger:
        init_deposit = input("Please make an initial deposit: ")
        account_start = datetime.datetime.now()
        ledger = account_ledger.write(
            f"starting balance as of {account_start.strftime('%c')} \n {init_deposit} ")
    print(f"Current Balance: {init_deposit}")

    def write_changes(self, change, new_balance):
        ledger = open("account_ledger.txt", "a")
        ledger.write(change)
        new_balance_str = "\n {0:.2f} \n".format(
            new_balance)
        print("\nCurrent Balance: ", new_balance_str)
        ledger.write(new_balance_str)
        ledger.close()

    def select(self):
        pick = input(
            "Would you like to \n(W): Withdraw from your account \n(D): Deposit to your account \n(V): View your account or \n(Q): Quit?")
        return pick

    def withdrawal(self):
        deduct = input("How much would you like to withdraw?")

        with open("account_ledger.txt", "r") as f:
            current_bal = f.readlines()[-1]

        change = f"\n-{deduct}"
        new_balance = float(current_bal) - float(deduct)

        self.write_changes(change, new_balance)

    def deposit(self):
        add = input("How much would you like to deposit?")

        with open("account_ledger.txt", "r") as f:
            current_bal = f.readlines()[-1]

        change = f"\n+{add}"
        new_balance = float(current_bal) + float(add)

        self.write_changes(change, new_balance)

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
    elif atm_action == 'q':
        break
    else:
        print("Please select the letter next to the action you wish to take \nW: Withdraw \nD: Deposit \nV: View account \nQ: Quit")
