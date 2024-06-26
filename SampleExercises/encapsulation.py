# "__" double underscore represents private attribute.
# Private attributes start with "__".

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "Private GeeksforGeeks"

    def getC(self):
        return self.__c

    # Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        #print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)
print(obj1.getC()) #getter method to get the private member


#print(obj1.c)
# Uncommenting print(obj1.c) will
# raise an AttributeError

#obj2 = Derived()
# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class