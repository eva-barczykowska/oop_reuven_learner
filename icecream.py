class Scoop:
    def __init__(self, flavour):
        self.flavour = flavour


# if you want it with mixins:
# class Scoop:
#     def __init__(self, flavor, *mixins):  # *mixins is a tuple containing any number of mixins(walnuts, choco chips)
#         self.flavor = flavor
#         self.mixins = []


s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('cappuccino')

for flavor in [s1, s2, s3]:
    print(flavor)

# sb else's solution
icecream = ["raspberry", "blueberry", "strawberry"]
for x in icecream:
    s = Scoop(x)
    print(s.flavour)

print("---------------------------")


class Bowl:
    def __init__(self):
        self.scoops = []  # initialize our scoops attribute to an empty list


b = Bowl()
print(b.scoops)
b.scoops.append(s1)
b.scoops.append(s2)
b.scoops.append(s3)

print(b)
print(b.scoops)

for one_scoop in b.scoops:
    print(one_scoop.flavour)

print("---------------------------")


#  rewritten solution


class Bowl:
    """Bowl, a class for creating bowls of ice cream.

    This class is typically going to be used in conjunction with the Scoop class. Instances
    of Scoop will be added to an instance of Bowl using the "add_scoops" method.

    Be careful about using this class with small children or people with high cholesterol.
    """

    def __init__(self):
        """
        Initialize a new Bowl instance with an empty list of scoops.

        Parameters:
        None

        Returns:
        None
        """
        self.scoops = []

    def add_scoop(self, *args):  # all positional arguments (except self) will be put into a tuple called args
        """
        Add one or more Scoop instances to the bowl.

        Parameters:
        *args: Variable length argument list. Each argument should be an instance of Scoop.

        Returns: None
        """
        for one_scoop in args:  # go through each scoop in args
            self.scoops.append(one_scoop)  # append it to self.scoops

    def flavours(self):
        """
        This method returns a list of flavours from the scoops in the bowl.

        Parameters:
        None

        Returns:
        list: A list of strings representing the flavours of the scoops in the bowl.
        """
        # return [one_scoop.flavour for one_scoop in self.scoops]  # return a list of flavours from our scoops attribute
        output = []  # initialize an empty list
        for one_scoop in self.scoops:  # go through each scoop in our scoops attribute
            output.append(one_scoop.flavour)  # get the flavour of the scoop
        return output  # return the list of flavours


s1 = Scoop('coconut')
s2 = Scoop('cacao-bliss')
s3 = Scoop('mint')

b = Bowl()
b.add_scoop(s1, s2)
b.add_scoop(s3)
print(b.scoops)
print(len(b.scoops))

for one_scoop in b.scoops:
    print(one_scoop.flavour)

print(b.flavours())
# print(help(Bowl.flavours))
# print(Bowl.flavours.__doc__) # same as previous line!
# print(help(Bowl.add_scoop))
print(help(Bowl))
