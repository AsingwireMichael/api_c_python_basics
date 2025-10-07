class BankAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

# creating an instance/object for the class
acc = BankAccount(1452, 10000)
print(acc.acc_num)
print(acc.balance)

# acc1 = BankAccount()
