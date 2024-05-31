class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
        print("Thank you for using the ATM!")


    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} successfully. New balance: ${self.balance}")
        print("Thank you for using the ATM!")


        

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn ${amount} successfully. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")
            print("Thank you for using the ATM!")



def display_menu():
    print("Welcome to VN BANK")
    print("      ATM         ")
    print("A. Check Balance")
    print("B. Deposit")
    print("C. Withdraw")
    print("D. Exit")


def main():
    atm = ATM()
    while True:
        display_menu()
        choice = input("Please enter your choice (A-D): ")
        
        if choice == 'A':
            atm.check_balance()
            break
        elif choice == 'B':
            amount = float(input("Enter the amount to deposit: $"))
            atm.deposit(amount)
            break
        elif choice == 'C':
            amount = float(input("Enter the amount to withdraw: $"))
            atm.withdraw(amount)
            break
        elif choice == 'D':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
