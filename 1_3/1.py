class BankAccount:

    __id = 0

    def __init__(self, first_name, last_name, start_balance):

        self.first_name = first_name
        self.last_name = last_name
        self.balance = start_balance
        self.id_inc()

    def add(self, count):
        if count <= 0:
            raise ValueError("Нельзя вводить отрицательные числа!")
        self.balance += count
        return self.balance

    @property
    def balance(self):
        return self.__balance

    @property
    def get_id(self):
        return self.__id

    @balance.setter
    def balance(self, start_balance):
        if start_balance <= 0:
            raise ValueError("Нельзя вводить отрицательные числа!")
        else:
            self.__balance = start_balance

    @classmethod
    def id_inc(cls):
        cls.__id += 1


a = BankAccount('123', 'xasd', 1000)

print(a.balance)
print(a.add(100))
print(a.get_id)

b = BankAccount('121233', 'xa123123sd', 200)

print(b.balance)
print(b.add(100))
print(b.get_id)