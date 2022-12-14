class Dog():
    __name : str #Private attribute in the class
    
    #Method init is the constructor initializes the object with the attributes. Self is like this in java, indicates the self object.
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        self.chip = False #Default value for attribute
    #Getters and setters
    def get_name (self):
        return self.__name
    def get_age(self):
        return self.age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.age = age
    #The others methods of the class
    def sit(self):
        print(self.__name.title() + " is now sitting.")
    def roll_over(self):
        print(self.__name.title() + " rolled over!")

nemo = Dog('nemo','2')
nemo.sit()
nemo.set_name(True) #IMPORTANT: We can modify the data type of attribute in runTime
print(nemo.get_name())

