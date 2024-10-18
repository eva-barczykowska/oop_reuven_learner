# without OOP
person = ("Ewa", "Barczykowska", 41)
print(person[0])
print(person[1])
print(person[2])

def full_name(person):
    return f"{person[0]} {person[1]}"

print(full_name(person))

print('---------------------------------------------------------')

# with OOP
class Person:
    def __init__(self, first_name, last_name, shoe_size):
        self.first_name = first_name
        self.last_name = last_name
        self.shoe_size = shoe_size
#getters / getter methods -- retrieve fields / attributes
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def first_name(self):
        return f"{self.first_name}"

    def last_name(self):
        return f"{self.last_name}"

p = Person("Ewa", "Barczykowska", 41)
print(p)
print(p.full_name())
print(type(p))
print(type(Person))

print(dir(Person)) # prints all methods and attributes of the class Person:
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# 'full_name']

print('setters / setter methods are used to modify the state of an object')
# setters / setter methods

class Person:
    def __init__(self, first_name, last_name, shoe_size):
        self.first_name = first_name
        self.last_name = last_name
        self.shoe_size = shoe_size

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def first_name(self):
        return f"{self.first_name}"

    def last_name(self):
        return f"{self.last_name}"
# setters / setter methods
    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def set_shoe_size(self, new_shoe_size):
        self.shoe_size = new_shoe_size

p = Person("Anita", "Passanha", 41) # need to define an instance before setting attributes
print(p.full_name())
p.set_first_name("Anita2")
p.set_last_name("Passanha2")
print(p.full_name())

# Getters / setter methods in are rarely used in Python
# No need because all atrributes are accessible directly/they're all public
# Protected/Private attributes? Nothing like that!

# Rewriting how it looks in modern Python

print('---------------------------------------------------------')

class Person:
    def __init__(self, first_name, last_name, shoe_size):
        self.first_name = first_name
        self.last_name = last_name
        self.shoe_size = shoe_size

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


p = Person("Beyonce", "Knowles", 7) # need to define an instance before setting attributes
print(p.full_name())
print(p.first_name)
print(p.last_name)
print(p.shoe_size)
p.first_name = "Beyonce2"
p.last_name = "Knowles2"
print(p.full_name())

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def greet(self):
        return f"Hello, {self._first_name} {self._last_name}!"

citizen1 = Person("John", "Doe")
citizen2 = Person("Jane", "Doe")
print(citizen1.greet())
print(citizen2.greet())

person = Person("Baboon", "Hicky").greet() # it works, but not recommended
print(person)