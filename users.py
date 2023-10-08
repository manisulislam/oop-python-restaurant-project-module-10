from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name=name
        self.phone= phone
        self.email= email
        self.address= address

class Customer(User):
    def __init__(self, name, phone, email, address, money):
        self.wallet= money
        self.__order=None
        super().__init__(name, phone, email, address)
    @property
    def order(self):
        return self.__order
    @order.setter
    def order(self, order):
        self.__order=order
    def place_order(self, order):
        self.order= order
        print(f"{self.name} place an order{order.items}")

    def eat(self, order):
        print(f"{self.name} eating order {order.items}")
    def pay_for_order(self, amount):
        pass

    def tips_amount(self, amount):
        pass

    def write_review(self, stars):
        pass


class Employee(User):
    def __init__(self, name, phone, email, address, salary,starting_date, department):
        self.salary= salary
        self.due= salary
        self.department= department
        self.starting_date= starting_date
        super().__init__(name, phone, email, address)
    def receive_salary(self):
        self.due= 0


class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, cooking_item):
        self.cooking_item= cooking_item
        super().__init__(name, phone, email, address, salary, starting_date, department)

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department):
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.tips_earning= 0
    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass
    def serve_food(self, order):
        pass
    def receive_tips(self, amount):
        self.tips_earning+=amount


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department):
        super().__init__(name, phone, email, address, salary, starting_date, department)