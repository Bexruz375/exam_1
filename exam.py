# 1 chast

# 1.'''Oписания моделей предметной области и их взаимодействия '''
# 2.'''Статический метод ничего не знает о классе и имеет дело только с параметрами'''
# 3.''' это один из основных принципов объектно-ориентированного программирования, который подразумевает скрытие внутренней реализации объекта от внешнего мира.'''
# 4.'''Наследование в Python. Наследование позволяет объявить класс, который дублирует функциональность уже существующего класса.'''

# 2 chast
# # 1 task
# def is_even():
#     a = float(input('Enter number:'))
#     if a % 2 == 0:
#         print(True)
#     else:
#         print(False)
# is_even()
# # 2 task
# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def display_info(self):
#         return f'''
# Make: {self.make}
# Model: {self.model}
# Year: {self.year}       
#         ''' 
    
    
# car = Car('Chevrolet', 'Ford', 2022)
# print(car.display_info())

# # 3 task
# def filter_positive_numbers(numbers):
#     posive_numbers = [num for num in numbers if num >= 0]
#     return posive_numbers

# numbers = [-3, 5, -10, 7, 10]
# posive_numbers = filter_positive_numbers(numbers)
# print(posive_numbers)



# # 4 task
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

    
#     def greet(self):
#         return f'Hello, my name is {self.name} and I am {self.age} years old.'

    
    
# person = Person('Bexruz', 12)
# print(person.greet())

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def greet(self):
#         return f'Hello, my name is {self.name} and I am {self.age} years old, my student_id {self.student_id}'

# person_1 = Student('Bexruz', 22, 21343)
# print(person_1.greet())

# # 5 task
# class Student():
#     def __init__(self, name, age, student_id):
#         self.name = name
#         self.age = age
#         self.student_id = student_id

#     def greet(self):
#         return f'Hello, my name is {self.name} and I am {self.age} years old, my student_id {self.student_id}'

# person_1 = Student('Tester', 43, 4000)
# print(person_1.greet())

# 3 chast
# 1 task
# def proverka_polindrom(a):
#     return a == a[::1]
# a = 'amma'
# if proverka_polindrom(a):
#     print(f'{a} is polindrom')
# else:
#     print(f'{a} is not  polindrom')

# # 2 task
# class BankAccount:
#     def __init__(self):
#         self.balance = 0 
#         self.__balans = {} 
#     def deposit(self,__number,amount):
#         self.__balans[__number] = amount + self.balance
#         self.balance += amount
#     def withdraw(self,__number,amount):
#         self.__balans[__number] = self.balance - amount
#         self.balance -= amount
#     def get_balance(self,__number):
#         return f"Текущий Баланс : {self.__balans[__number]}"
#     def get_account_number(self,__number):
#         return f"Номер счета : {__number}"
        
# a = BankAccount()
# a.deposit(1, 33)
# a.withdraw(1, 30)
# print(a.get_account_number(1))
# print(a.get_balance(1))
# print(a.__dict__)

# # 3 task
# def stroka(string):
#     char_count = {}
#     for char in string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     return char_count

# input_string = "hello"
# result = stroka(input_string)
# print(result)






    






        
