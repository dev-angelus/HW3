print('работать тут')
class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __str__(self):
        return f'Name: {self._name}\nBalance: {self._balance}'

    # @property
    # def name(self):
    #     return f'{self.__name}'
    # @name.setter
    # def name(self, n):
    #     self.__name = n
    #
    # @property
    # def balance(self):
    #     return f'{self.__balance}'
    #
    # @balance.setter
    # def balance(self, b):
    #     self.__balance = b

    def moneyX(self):
        money = int(input('Enter cash input: '))
        self._balance = int(self._balance) + money

    def __jackpot(self):
        print(f'Now your balance (* 10) is : {self._balance * 10}\n')

    def jackpot(self):
        return self.__jackpot()

    def _kill(self):
        self._balance = 0
        print(f'Annuling... Now your balance is : {self._balance}\n')

    def _copy_balance(self, copy):
        self._balance = copy._balance + self._balance
        return f'Balance taken from {copy._name}. Now your balance is: {self._balance}\n'


Client1 = Bank('Teacher', 100)
Client2 = Bank('Nazira', 100)

Client1.moneyX()
print(Client1)
Client1.jackpot()
print(Client1._copy_balance(Client2))


Client1._kill()

print(Client2)

