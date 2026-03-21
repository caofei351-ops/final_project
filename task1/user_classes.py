from base_classes import User

class Student(User):
    DISCOUNT_RATE = 0.9
    def __init__(self, phone, student_id):
        super().__init__(phone)
        self.student_id = student_id

    def get_discount(self):
        return self.DISCOUNT_RATE

    def recharge(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"✅ [{self.student_id}]be recharged successfully！Current balance：{self.get_balance():.2f}")
        else:
            print("The amount cannot be negative!")


class Teacher(User):
    DISCOUNT_RATE = 0.9
    def __init__(self, phone, teacher_id):
        super().__init__(phone)
        self.teacher_id = teacher_id 

    def get_discount(self):
        return self.DISCOUNT_RATE

    def recharge(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"✅ [{self.teacher_id}]be recharged successfully！Current balance：{self.get_balance():.2f}")
        else:
            print("The amount cannot be negative！")


class NormalUser(User):
    def get_discount(self):
        return 1.0  

    def recharge(self, amount):
        print("Non-students do not need to recharge. Just pay directly when checking out!")

