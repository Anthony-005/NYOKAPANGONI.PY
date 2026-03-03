
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance < amount:
            return "INSUFFICIENT BALANCE!"
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"

    def get_balance(self):
        return f"Current balance: {self.balance}"

    def customer_details(self):
        return f"Name: {self.customer_name}, Account: {self.account_number}, Opened: {self.date_of_opening}, Balance: {self.balance}"


# Example usage
my_bank = BankAccount(2219, 20000, "11-5-22", "Anthony")

print(my_bank.deposit(12000))
print(my_bank.withdraw(30000))
print(my_bank.get_balance())
print(my_bank.customer_details())
