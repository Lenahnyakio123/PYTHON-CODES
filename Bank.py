class Account:
    # i. Parent class
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # ii. displayAccount() method
    def displayAccount(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: KSh {self.balance}")

class SavingsAccount(Account):
    # iii. Child class inheriting from Account
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        # iv. Interest rate attribute
        self.interest_rate = interest_rate

    # v. calculateInterest() method
    def calculateInterest(self):
        interest = self.balance * self.interest_rate / 100
        return interest

    def displaySavingsAccount(self):
        super().displayAccount()
        print(f"Interest Rate: {self.interest_rate}%")
        print(f"Calculated Interest: KSh {self.calculateInterest()}")

# vi. Create SavingsAccount object and display
if __name__ == "__main__":
    savings1 = SavingsAccount("ACC5689", 20000, 8)
    
    savings1.displayAccount()
    print(f"Interest Rate: {savings1.interest_rate}%")
    print(f"Interest Earned: KSh {savings1.calculateInterest()}")
    
    print("\n--- Or using combined display ---")
    savings1.displaySavingsAccount()
