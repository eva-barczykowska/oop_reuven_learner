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

    # getters / getter methods -- retrieve fields / attributes
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

print(dir(Person))  # prints all methods and attributes of the class Person:
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


person = Person("Anita", "Passanha", 41)  # need to define an instance before setting attributes
print(p.full_name())
person.set_first_name("Anita2")
person.set_last_name("Passanha2")
print(p.full_name())

# Getters / setter methods in are rarely used in Python
# No need because all attributes are accessible directly/they're all public
# Protected/Private attributes? Nothing like that!

print('---------------------------------------------------------')
print("Rewriting how it looks in modern Python")
print('---------------------------------------------------------')


class Person:
    population = 0

    def __init__(self, first_name, last_name, shoe_size):
        self.first_name = first_name
        self.last_name = last_name
        self.shoe_size = shoe_size
        Person.population += 1

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


p = Person("Beyonce", "Knowles", 7)  # need to define an instance before setting attributes
print(p.full_name())  # print the full name
print(p.first_name)  # print the first name, getting the attribute directly
print(p.last_name)
print(p.shoe_size)
p.first_name = "Beyonce2"  # change the first name, setting the attribute directly
p.last_name = "Knowles2"
print(p.full_name())


class FriendlyPerson:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def greet(self):
        return f"Hello, {self._first_name} {self._last_name}!"


citizen1 = FriendlyPerson("John", "Doe")
citizen2 = FriendlyPerson("Jane", "Doe")
print(citizen1.greet())
print(citizen2.greet())

person = FriendlyPerson("Baboon", "Hicky").greet()  # it works, but not recommended
print(person)
# print(person.greet())

#  ICPO look up path in Python
print(Person.population)  # accessing the class attribute directly
p2 = Person("Tanita", "Tikaram", 47)
print(Person.population)

print(p2.population) # we ask instance for the attribute, not the class
# if instance doesn't have the attribute, it will go to the class attribute'


class Employee(Person):
    def __init__(self, first_name, last_name, shoe_size, id):
        # Person.__init__(self, first_name, last_name, shoe_size) # comes from the superclass (Person)
        # there is a nicer way to call the superclass constructor then how we did it on the previous line
        super().__init__(first_name, last_name, shoe_size) # comes from the superclass (Person)
        self.id = id

ewa = Employee("Ewa", "Barczykowska", 41, 12345)
print(ewa.id)

# Python supports multiple inheritance but it's not recommended'
