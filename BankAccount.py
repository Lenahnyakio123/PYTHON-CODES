class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    # i. deposit method should return the amount deposited
    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        self.balance += amount
        return f"Amount deposited: {amount}"

    # ii. withdraw method
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Amount withdrawn: {amount}"

    # iii. check_balance method should print current balance
    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    # iv. customer_details method
    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

# Example to test
if __name__ == "__main__":
    acc1 = BankAccount(223334455, "Lynn Wangari", "01-07-2020", 10000)
    
    print(acc1.deposit(5000))
    print(acc1.withdraw(2000))
    print(acc1.withdraw(20000))
    
    acc1.check_balance()
    acc1.customer_details()
