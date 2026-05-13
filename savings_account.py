from account import Account


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02, withdraw_limit=100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.withdraw_limit:
            print(f"Withdrawal amount exceeds the limit of ${self.withdraw_limit}.")
        else:
            super().withdraw(amount)

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} applied.")


print("--- Savings Account ---")
savings = SavingsAccount("Alice", 1000)
savings.apply_interest()

print("\n--- Testing Withdrawal Limit ---")
print(f"Current balance: ${savings.get_balance()}")
print(f"Withdrawal limit: ${savings.withdraw_limit}")

print("\nAttempt 1: Withdraw $50 (within limit)")
savings.withdraw(50)

print("\nAttempt 2: Withdraw $60 (within limit)")
savings.withdraw(60)

print("\nAttempt 3: Withdraw $150 (exceeds limit)")
savings.withdraw(150)

print(f"\nFinal balance: ${savings.get_balance()}")