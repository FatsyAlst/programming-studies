# ===================================
# CLASSES, OBJECTS & INHERITANCE
# ===================================
# Comprehensive guide to Object-Oriented Programming (OOP) in Python

# ===================================
# 1. CLASSES AND OBJECTS - BASICS
# ===================================

# A class is a blueprint for creating objects
# An object is an instance of a class

# Basic class definition
class Dog:
    pass  # Empty class

# Creating objects (instances)
dog1 = Dog()
dog2 = Dog()
print(dog1)  # <__main__.Dog object at 0x...>
print(dog2)  # <__main__.Dog object at 0x...> (different memory address)


# ===================================
# 2. THE __init__ METHOD (Constructor)
# ===================================

# __init__ is called automatically when creating an object
# It initializes the object's attributes

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# Creating instances with initial values
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name)  # Alice
print(person2.age)   # 30
print(person1.introduce())  # Hi, I'm Alice and I'm 25 years old


# ===================================
# 3. INSTANCE ATTRIBUTES VS CLASS ATTRIBUTES
# ===================================

class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    
    def __init__(self, brand, model):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand)   # Toyota (instance attribute)
print(car2.brand)   # Honda (instance attribute)
print(car1.wheels)  # 4 (class attribute)
print(car2.wheels)  # 4 (class attribute)

# Changing class attribute affects all instances
Car.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6


# ===================================
# 4. INSTANCE METHODS
# ===================================

# Methods are functions defined inside a class
# First parameter is always 'self' (refers to the instance)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def get_balance(self):
        return f"{self.owner}'s balance: ${self.balance}"

account = BankAccount("John", 1000)
print(account.deposit(500))    # Deposited $500. New balance: $1500
print(account.withdraw(200))   # Withdrew $200. New balance: $1300
print(account.get_balance())   # John's balance: $1300


# ===================================
# 5. THE self PARAMETER
# ===================================

# 'self' represents the instance calling the method
# It's automatically passed when calling methods

class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1  # Accessing instance attribute via self
    
    def get_count(self):
        return self.count

counter1 = Counter()
counter2 = Counter()

counter1.increment()
counter1.increment()
counter2.increment()

print(counter1.get_count())  # 2
print(counter2.get_count())  # 1


# ===================================
# 6. INHERITANCE - BASICS
# ===================================

# Inheritance allows a class to inherit attributes and methods from another class
# Parent class (superclass/base class)
# Child class (subclass/derived class)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# Child class inherits from Animal
class Cat(Animal):
    def speak(self):  # Method overriding
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self):  # Method overriding
        return f"{self.name} says Woof!"

# Creating instances
cat = Cat("Whiskers")
dog = Dog("Buddy")

print(cat.speak())  # Whiskers says Meow!
print(dog.speak())  # Buddy says Woof!


# ===================================
# 7. EXTENDING PARENT CLASS WITH super()
# ===================================

# super() calls methods from the parent class
# Useful when you want to extend (not replace) parent functionality

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call parent's __init__
        self.battery_capacity = battery_capacity
    
    def info(self):
        parent_info = super().info()  # Call parent's info()
        return f"{parent_info} - Battery: {self.battery_capacity}kWh"

tesla = ElectricCar("Tesla", "Model 3", 75)
print(tesla.info())  # Tesla Model 3 - Battery: 75kWh


# ===================================
# 8. MULTIPLE INHERITANCE
# ===================================

# A class can inherit from multiple parent classes

class Flyer:
    def fly(self):
        return "Flying in the sky"

class Swimmer:
    def swim(self):
        return "Swimming in water"

class Duck(Flyer, Swimmer, Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

duck = Duck("Donald")
print(duck.name)   # Donald (from Animal)
print(duck.fly())  # Flying in the sky (from Flyer)
print(duck.swim()) # Swimming in water (from Swimmer)


# ===================================
# 9. METHOD RESOLUTION ORDER (MRO)
# ===================================

# Python uses MRO to determine which method to call in multiple inheritance
# Use .mro() or __mro__ to see the order

print(Duck.mro())
# [<class '__main__.Duck'>, <class '__main__.Flyer'>, 
#  <class '__main__.Swimmer'>, <class '__main__.Animal'>, <class 'object'>]


# ===================================
# 10. ENCAPSULATION (Private Attributes)
# ===================================

# Python doesn't have true private attributes, but uses naming conventions
# Single underscore _ : "internal use" (convention, not enforced)
# Double underscore __ : Name mangling (harder to access from outside)

class SecureAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # "Private" attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = SecureAccount("Alice", 1000)
print(account.owner)           # Alice (public)
# print(account.__balance)     # AttributeError
print(account.get_balance())   # 1000 (accessed through method)


# ===================================
# 11. PROPERTY DECORATORS (@property)
# ===================================

# @property allows you to access methods like attributes
# Provides controlled access to private attributes

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)     # 25 (called like attribute, but it's a method)
print(temp.fahrenheit)  # 77.0
temp.celsius = 30       # Using setter
print(temp.celsius)     # 30


# ===================================
# 12. CLASS METHODS (@classmethod)
# ===================================

# Class methods receive the class (cls) instead of instance (self)
# Used for alternative constructors or operations on the class itself

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        # Alternative constructor
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        # Another alternative constructor
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

date1 = Date(2025, 12, 4)
date2 = Date.from_string("2025-12-25")
date3 = Date.today()

print(date1)  # 2025-12-04
print(date2)  # 2025-12-25


# ===================================
# 13. STATIC METHODS (@staticmethod)
# ===================================

# Static methods don't receive self or cls
# Used for utility functions related to the class

class Math:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def is_even(num):
        return num % 2 == 0

# Can be called without creating an instance
print(Math.add(5, 3))        # 8
print(Math.multiply(4, 7))   # 28
print(Math.is_even(10))      # True


# ===================================
# 14. MAGIC METHODS (DUNDER METHODS)
# ===================================

# Special methods with double underscores
# Allow custom behavior for built-in operations

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        # Called by str() and print()
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        # Called by repr() - should be unambiguous
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        # Called by len()
        return self.pages
    
    def __eq__(self, other):
        # Called by ==
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        # Called by <
        return self.pages < other.pages

book1 = Book("1984", "George Orwell", 328)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("Animal Farm", "George Orwell", 112)

print(book1)           # '1984' by George Orwell (__str__)
print(repr(book1))     # Book('1984', 'George Orwell', 328) (__repr__)
print(len(book1))      # 328 (__len__)
print(book1 == book2)  # True (__eq__)
print(book3 < book1)   # True (__lt__)


# ===================================
# 15. INHERITANCE WITH isinstance() AND issubclass()
# ===================================

class Shape:
    pass

class Circle(Shape):
    pass

circle = Circle()

# isinstance() checks if object is instance of class
print(isinstance(circle, Circle))  # True
print(isinstance(circle, Shape))   # True (Circle inherits from Shape)
print(isinstance(circle, str))     # False

# issubclass() checks if class is subclass of another
print(issubclass(Circle, Shape))   # True
print(issubclass(Shape, Circle))   # False


# ===================================
# 16. COMPOSITION VS INHERITANCE
# ===================================

# Composition: "has-a" relationship (more flexible than inheritance)
# Inheritance: "is-a" relationship

# Composition example
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started"

class CarWithComposition:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Car HAS-A engine
    
    def start_car(self):
        return f"{self.brand}: {self.engine.start()}"

engine = Engine(200)
car = CarWithComposition("Toyota", engine)
print(car.start_car())  # Toyota: Engine started


# ===================================
# COMMON USE CASES
# ===================================

# 1. Game characters with inheritance
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self):
        return f"{self.name} attacks!"

class Warrior(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon
    
    def attack(self):
        return f"{self.name} attacks with {self.weapon}!"

class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana
    
    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} casts a spell!"
        return "Not enough mana"

warrior = Warrior("Conan", 100, "Sword")
mage = Mage("Gandalf", 80, 50)

print(warrior.attack())    # Conan attacks with Sword!
print(mage.cast_spell())   # Gandalf casts a spell!


# 2. Employee management system
class Employee:
    employee_count = 0  # Class attribute
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def annual_salary(self):
        return self.salary * 12
    
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def annual_salary(self):
        bonus = self.salary * 2  # Bonus: 2 months salary
        return (self.salary * 12) + bonus

emp1 = Employee("John", 5000)
emp2 = Manager("Alice", 8000, "IT")

print(emp1.annual_salary())           # 60000
print(emp2.annual_salary())           # 112000 (includes bonus)
print(Employee.get_employee_count())  # 2


# ===================================
# BEST PRACTICES
# ===================================

# 1. Use clear, descriptive class names (PascalCase)
# 2. Keep classes focused (Single Responsibility Principle)
# 3. Use inheritance for "is-a" relationships
# 4. Use composition for "has-a" relationships
# 5. Don't overuse inheritance - prefer composition when possible
# 6. Use @property for computed attributes or controlled access
# 7. Implement __str__ and __repr__ for better debugging
# 8. Use isinstance() instead of type() for type checking
# 9. Follow naming conventions:
#    - _single_underscore for internal use
#    - __double_underscore for name mangling
# 10. Document your classes with docstrings


# ===================================
# COMMON MISTAKES
# ===================================

# 1. Forgetting self parameter
# class Wrong:
#     def method():  # ❌ Missing self
#         pass

# 2. Not calling super().__init__() in child class
# class Child(Parent):
#     def __init__(self, x):
#         self.x = x  # ❌ Parent's __init__ not called

# 3. Modifying mutable class attributes
# class Wrong:
#     items = []  # ❌ Shared by all instances
#     
#     def add_item(self, item):
#         self.items.append(item)  # Changes for ALL instances!

# 4. Using class name instead of self
# class Wrong:
#     def __init__(self):
#         Wrong.value = 10  # ❌ Should be self.value

# 5. Not returning self in chaining methods
# class Wrong:
#     def method(self):
#         # Do something
#         pass  # ❌ Should return self for chaining


# ===================================
# PRACTICE EXERCISES
# ===================================

# Exercise 1: Create a Rectangle class
# - __init__(width, height)
# - area() method
# - perimeter() method
# - __str__() method

# Exercise 2: Create a Student class with inheritance
# - Person class with name and age
# - Student inherits from Person, adds student_id and grades list
# - calculate_average() method
# - is_passing() method (average >= 60)

# Exercise 3: Create a BankAccount class with encapsulation
# - Private __balance attribute
# - deposit() and withdraw() methods
# - @property for balance (read-only)
# - transaction_history list

# Exercise 4: Create a Shape hierarchy
# - Shape base class with area() method
# - Circle, Rectangle, Triangle child classes
# - Each implements area() differently
# - Use isinstance() to identify shapes
