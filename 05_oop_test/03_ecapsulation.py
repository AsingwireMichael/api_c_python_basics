class BankAccount:
    def __init__(self, acc_num, balance):
        self.__acc_num = acc_num
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def setBalance(self, amount):
        self.__balance = self.__balance + amount
        # self.__balance += amount # same as code above

# creating an instance/object for the class
acc = BankAccount(1452, 10000)
# print(acc.__acc_num) 
print(acc.getBalance())
print(acc.setBalance(25000))
print(acc.getBalance())
