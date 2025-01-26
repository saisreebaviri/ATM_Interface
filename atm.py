class User:
    def _init_(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient_account.user_id}")
            recipient_account.balance += amount
            recipient_account.transaction_history.append(f"Received ${amount} from {self.user_id}")

class ATM:
    def _init_(self):
        self.users = {
            "123456": User("123456", "1234")
            # Add more users here if needed
        }

    def start(self):
        print("Welcome to the ATM")
        user_id = input("Enter user ID: ")
        pin = input("Enter PIN: ")

        if user_id in self.users and self.users[user_id].pin == pin:
            self.perform_transactions(self.users[user_id])
        else:
            print("Invalid user ID or PIN")
            self.start()

    def perform_transactions(self, user):
        while True:
            print("\nChoose an option:")
            print("1. View Transaction History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Transaction History:")
                for transaction in user.transaction_history:
                    print(transaction)

            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                user.withdraw(amount)

            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                user.deposit(amount)

            elif choice == "4":
                recipient_id = input("Enter recipient's user ID: ")
                amount = float(input("Enter amount to transfer: "))
                if recipient_id in self.users:
                    user.transfer(amount, self.users[recipient_id])
                else:
                    print("Recipient not found. Please try again.")

            elif choice == "5":
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.start()