from datetime import datetime


class Account:

    __all_id = 0
    __history_operation = {}

    def __init__(self, first_name, last_name, start_balance):

        self._first_name = first_name
        self._last_name = last_name
        self.balance = start_balance
        self._id = self.id_inc()
        self.init_person_to_history(self._id, self._first_name,
                                    self._last_name, self.balance)

    def add(self, count):
        if count <= 0:
            raise ValueError("Нельзя вводить отрицательные числа!")
        self.balance += count
        self.person_add_count(count)
        return self.balance

    def remove(self, count):
        if count <= 0:
            raise ValueError("Нельзя снять отрицательные числа и 0!")

        if self._balance - count < 0:
            raise ValueError("На счете не хвататет средств для совершения операции!")
        self._balance = self.balance - count
        self.person_remove_count(count)
        return self.balance

    @property
    def balance(self):
        return self._balance

    @property
    def get_id(self):
        return self._id

    @property
    def get_history(self):
        return self.__history_operation[self._id]

    @balance.setter
    def balance(self, start_balance):
        if start_balance <= 0:
            raise ValueError("Нельзя вводить отрицательные числа и 0!")
        else:
            self._balance = start_balance

    @classmethod
    def id_inc(cls):
        cls.__all_id += 1
        return cls.__all_id

    @classmethod
    def init_person_to_history(cls, id, first_name, last_name, balance):
        cls.__history_operation[id] = [f'''{datetime.now()} Пользователь {first_name} {last_name} '''
                                       f'''Создал счет с суммой {balance} ед.''']

    def person_add_count(self, count):
        self.__history_operation.get(self._id).append(f'''{datetime.now()}: '''
                                                      f'''Пользователь {self._first_name} {self._last_name}'''
                                                      f'''добавил к счету {count} ед.'''
                                                      f'''Общий баланс - {self._balance}''')

    def person_remove_count(self, count):
        self.__history_operation.get(self._id).append(f'''{datetime.now()}: '''
                                                      f'''Пользователь {self._first_name} {self._last_name}'''
                                                      f'''снял со счета {count} ед.'''
                                                      f'''Общий баланс - {self._balance}''')


a = Account('Andrew', 'Kod', 1000)

print(a.get_id)
print(a.balance)
print(a.add(100))
print(a.remove(200))

[print(i) for i in a.get_history]


b = Account('Daniel', 'Xud', 2000)

print(b.get_id)
print(b.balance)
print(b.add(1000))
print(b.add(1000))
print(b.remove(4100))
[print(i) for i in b.get_history]