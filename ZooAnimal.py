from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes
    isAlive = True
    canEat = []

    #Constructors
    def __init__(self):
        self.value = "Animal"

    #Methods
    @abstractmethod
    def reproduce(self):
        pass

    @abstractmethod
    def breathe(self):
        pass

    @abstractmethod
    def movement(self):
        pass

    def eat(self, other):
        for i in range(len(self.canEat)):
            if other == self.canEat[i]:
                return True
            else:
                return False

    def sleep(self):
        return("I am sleeping")

    def die(self):
        self.isAlive = False
        return

    def type(self):
        return(self.value)

class Plant(ABC):
    #Attributes
    isAlive = True
    canEat = []
    #Constructors
    def __init__(self):
        self.value = "Plant"

    #Methods
    def eat(self, other):
        for i in range(len(self.canEat)):
            if other == self.canEat[i]:
                return True
            else:
                return False

    def type(self):
        return(self.value)

class Mammal(Animal):
    #Attributes

    #Constructors
    def __init__(self):
        self.value = "Mammal"

    #Methods

    def movement(self):
        return("I walk on land")

    def breathe(self):
        return("I breathe in air")

    def reproduce(self):
        return("I give birth")

    def type(self):
        return(self.value)

class Bird(Animal):
    #Attributes

    #Constructors
    def __init__(self):
        self.value = "Bird"

    #Methods

    @abstractmethod
    def movement(self):
        pass

    def breathe(self):
        return("I breathe in air")

    def reproduce(self):
        return("I lay eggs")

    def type(self):
        return(self.value)

class Fish(Animal):
    #Attributes

    #Constructors
    def __init__(self):
        self.value = "Fish"

    #Methods

    def movement(self):
        return("I swim in water")

    def breathe(self):
        return("I breathe underwater")

    def reproduce(self):
        return("I lay eggs")

    def type(self):
        return(self.value)

class Grass(Plant):
    #Attributes

    #Constructors
    def __init__(self):
        self.value = "Grass"

    #Methods
    def type(self):
        return(self.value)

class Leaves(Plant):
    #Attributes

    #Constructors
    def __init__(self):
        self.value = "Leaves"

    #Methods
    def type(self):
        return(self.value)

class Antelope(Mammal):
    #Attributes
    canEat = ["Grass"]

    #Constructors
    def __init__(self):
        self.value = "Antelope"

    #Methods
    def type(self):
        return(self.value)


class BigFish(Fish):
    #Attributes
    canEat = ["LittleFish"]

    #Constructors
    def __init__(self):
        self.value = "Bigfish"

    #Methods
    def type(self):
        return(self.value)
        

class LittleFish(Fish):
    #Attributes

    #Constructors
    def __init__(self):
        self.value = "LittleFish"

    #Methods
    def type(self):
        return(self.value)



class Bug(Animal):
    #Attributes
    canEat = ["Leaves"]

    #Constructors
    def __init__(self):
        self.value = "Bug"

    #Methods
    def movement(self):
        return("I can fly")

    def breathe(self):
        return("I breathe in air")

    def reproduce(self):
        return("I lay eggs")

    def type(self):
        return(self.value)

class Bear(Mammal):
    #Attributes
    canEat = ["BigFish","Bug","Chicken","Cow","Leaves","Sheep"]

    #Constructors
    def __init__(self):
        self.value = "Bear"
    
    #Methods
    def type(self):
        return(self.value)

class Chicken(Bird):
    #Attributes
    canEat = ["Bug"]

    #Constructors
    def __init__(self):
        self.value = "Chicken"

    #Methods
    def type(self):
        return(self.value)

    def movement(self):
        return("I can fly short distances") 


class Cow(Mammal):
    #Attributes
    canEat = ["Grass"]

    #Constructors
    def __init__(self):
        self.value = "Cow"

    #Methods
    def type(self):
        return(self.value)


class Fox(Mammal):
    #Attributes
    canEat = ["Chicken","Sheep"]

    #Constructors
    def __init__(self):
        self.value = "Fox"

    #Methods
    def type(self):
        return(self.value)


class Giraffe(Mammal):
    #Attributes
    canEat = ["Leaves"]

    #Constructors
    def __init__(self):
        self.value = "Giraffe"

    #Methods
    def type(self):
        return(self.value)


class Lion(Mammal):
    #Attributes
    canEat = ["Antelope","Cow"]

    #Constructors
    def __init__(self):
        self.value = "Lion"

    #Methods
    def type(self):
        return(self.value)


class Panda(Mammal):
    #Attributes
    canEat = ["Leaves"]

    #Constructors
    def __init__(self):
        self.value = "Panda"

    #Methods
    def type(self):
        return(self.value)


class Sheep(Mammal):
    #Attributes
    canEat = ["Grass"]

    #Constructors
    def __init__(self):
        self.value = "Sheep"

    #Methods
    def type(self):
        return(self.value)
