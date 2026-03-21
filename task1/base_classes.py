from abc import ABC, abstractmethod

class Dish(ABC):
    def __init__(self, name, student_price, teacher_price, normal_price):
        self.name = name          
        self.student_price = student_price  
        self.teacher_price = teacher_price  
        self.normal_price = normal_price   

    @abstractmethod
    def get_type(self):
        pass


class User(ABC):
    def __init__(self, phone):
        self.phone = phone  
        self.balance = 0.0 

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def recharge(self, amount):
        pass

    def get_balance(self):
        return round(self.balance, 2)
