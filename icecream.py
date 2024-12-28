class Scoop:
    def __init__(self, flavour):
        self.flavour = flavour

    def __repr__(self):
        return f"{self.flavour}"


# if you want it with mixins:
# class Scoop:
#     def __init__(self, flavor, *mixins):  # *mixins is a tuple containing any number of mixins(walnuts, choco chips)
#         self.flavor = flavor
#         self.mixins = []


s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('cappuccino')


# for flavor in [s1, s2, s3]:
#     print(flavor)
#
# # sb else's solution
# icecream = ["raspberry", "blueberry", "strawberry"]
# for x in icecream:
#     s = Scoop(x)
#     print(s.flavour)
#
# print("---------------------------")


# b = Bowl()
# print(b.scoops)
# b.scoops.append(s1)
# b.scoops.append(s2)
# b.scoops.append(s3)
#
# print(b)
# print(b.scoops)
#
# for one_scoop in b.scoops:
#     print(one_scoop.flavour)
#
# print("---------------------------")


#  rewritten solution


class Bowl:
    """Bowl, a class for creating bowls of ice cream.

    This class is typically going to be used in conjunction with the Scoop class. Instances
    of Scoop will be added to an instance of Bowl using the "add_scoops" method.

    Be careful about using this class with small children or people with high cholesterol.
    """
    MAX_SCOOPS = 3

    def __init__(self):
        """
        Initialize a new Bowl instance with an empty list of scoops.

        Parameters:
        None

        Returns:
        None
        """
        self.scoops = []

    def __repr__(self):
        # return f"Bowl with {len(self.scoops)} scoops"
        # return f"Bowl has {(self.scoops)}"

        # OPTION 1, traditional loop
        # output = ''
        # for index, one_scoop in enumerate(self.scoops):
        #     output += f" {index + 1}: {one_scoop}\n"
        # return output

        # OPTION 2, using list comprehension
        # join each scoop with a newline character and return the result
        return '\n'.join([f'{index + 1}: {scoop}' for index, scoop in enumerate(self.scoops)])

    def add_scoop(self, *args):  # all positional arguments (except self) will be put into a tuple called args
        """
        Add one or more Scoop instances to the bowl.

        Parameters:
        *args: Variable length argument list. Each argument should be an instance of Scoop.

        Returns: None
        """

        for one_scoop in args:  # go through each scoop in args
            if len(self.scoops) >= self.MAX_SCOOPS:
                print(f"Bowl is full. Cannot add more than {self.MAX_SCOOPS} scoops.")
                break
            self.scoops.append(one_scoop)  # add the scoop to our scoops attribute

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

    def has_flavours(self):
        return [one_scoop.flavour for one_scoop in self.flavours()]

    def has_flavour(self, flavour):
        return flavour in self.flavours()


# s1 = Scoop('coconut')
# s2 = Scoop('cacao-bliss')
# s3 = Scoop('mint')
# print(s1)

# bowl_with_3_scoops = Bowl()
# bowl_with_3_scoops.add_scoop(s1, s2)
# bowl_with_3_scoops.add_scoop(s3)
# bowl_with_3_scoops.add_scoop(s1) # tryig to add a 4th scoop when the bowl is already full


# print(b)
# print(b.scoops)
# print(len(b.scoops))
# print(b.has_flavour('persimon'))
# print(b.has_flavour('vanilla'))

# for one_scoop in b.scoops:
#     print(one_scoop.flavour)

# print(b.flavours())
# print(help(Bowl.flavours))
# print(Bowl.flavours.__doc__) # same as previous line!
# # print(help(Bowl.add_scoop))
# print(help(Bowl))

# print(s1)
#
# print(s2.__class__)
# print(s2.__class__.__name__) # one way to get the name of the class

class BigBowl(Bowl):
    MAX_SCOOPS = 5

    # look at that, only 1 line but it will all work!

    # we don't need to redefine __init__ here, because it's already defined in the superclass
    # and it's the same as Bowl.__init__
    # if we had other attributes, we would need to use super().__init__() to call the superclass's __init__ method'

    # def __init__(self):
    #     # super().__init__()
    #     self.scoops = []
    # this below method can be moved to the superclass, so that it's not repeated in each subclass
    # what we do is we prepend MAX_SCOOPS with self in the parent class
    # so it will always work for all subclasses

    # def add_scoop(self, *args):  # all positional arguments (except self) will be put into a tuple called args
    #     """
    #     Add one or more Scoop instances to the bowl.
    #
    #     Parameters:
    #     *args: Variable length argument list. Each argument should be an instance of Scoop.
    #
    #     Returns: None
    #     """
    #
    #     for one_scoop in args:  # go through each scoop in args
    #         if len(self.scoops) >= self.MAX_SCOOPS:
    #             print(f"Bowl is full. Cannot add more than {self.MAX_SCOOPS} scoops.")
    #             break
    #         self.scoops.append(one_scoop)  # add the scoop to our scoops attribute


bigger_bowl_with_5_scoops = BigBowl()
bigger_bowl_with_5_scoops.add_scoop(s1, s2, s3, s1, s1, s2)
print(bigger_bowl_with_5_scoops.flavours())  # prints only 5, because the MAX_SCOOPS is 5


class SuperBigBowl(Bowl):
    MAX_SCOOPS = 10


giant_bowl_with_10_scoops = SuperBigBowl()
giant_bowl_with_10_scoops.add_scoop(s1, s2, s3, s1, s1, s2, s3, s1, s1, s2)
giant_bowl_with_10_scoops.add_scoop(s1)  # this will add the scoop because the MAX_SCOOPS is 10
print(giant_bowl_with_10_scoops.flavours())  # prints all 10, because the MAX_SCOOPS is 10

# and we can continue like this, making new classes that inherit

# look up pattern
# ICPO

print('---------------------------------------')
for var in vars(Bowl):
    print(var)
