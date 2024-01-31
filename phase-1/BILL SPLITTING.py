class Billsplitter:

    def __init__(self):
        self.expenses = {}

    def add_user(self, name):
        self.expenses[name] = 0

    def add_expense(self, payer, amt, participants):
        total_members = len(participants)
        if total_members == 0:
            print("Error: At least one participant is required.")
            return

        individual_share = amt / total_members
        self.expenses[payer] += amt

        for participant in participants:
            self.expenses[participant] -= individual_share

        self.expenses.setdefault(payer, 0)
        self.expenses[payer] += amt

        for participant in participants:
            self.expenses.setdefault(participant, 0)
            self.expenses[participant] -= individual_share

    def print_balances(self):
        print("Current Balances:")
        for user, balance in self.expenses.items():
            print(f"{user}: {balance}")

    def settle_expenses(self):
        for user, balance in self.expenses.items():
            if balance < 0:
                for other_user, other_balance in self.expenses.items():
                    if other_balance > 0:
                        amt_to_settle = min(-balance, other_balance)
                        print(f"{user} owes {other_user}: {amt_to_settle}")
                        self.expenses[user] += amt_to_settle
                        self.expenses[other_user] -= amt_to_settle
                        balance += amt_to_settle
                        other_balance -= amt_to_settle
                        if balance == 0:
                            break

    def run(self):
        while True:
            print("Options:")
            print("1. Add user")
            print("2. Add expense")
            print("3. Print balances")
            print("4. Settle expenses")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter user name: ")
                self.add_user(name)

            elif choice == '2':
                payer = input("Enter payer's name: ")
                amt = float(input("Enter the expense amt: "))
                participants_str = input("Enter participants names separated by commas: ")
                participants = [p.strip() for p in participants_str.split(",")]
                self.add_expense(payer, amt, participants)

            elif choice == '3':
                self.print_balances()

            elif choice == '4':
                self.settle_expenses()

            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    bill_splitter = Billsplitter()
    bill_splitter.run()
