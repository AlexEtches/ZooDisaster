from ZooAnimal import *


def foodChain(Animals):

    for i in range(len(Animals)):
        if Animals[i].eat(Animals[i+1]) == True:
            print(Animals[i].value + "eats " + Animals[i+1].value)
            Animals.remove(Animals[i+1])
            print(toString(Animals))

def toString(animalList):
    string = []
    for animal in animalList:
        string.append(animal.value)

inputString = "Fox,Bug,Chicken,Grass,Sheep"
inputList=inputString.split(",")
animalList = []

for animal in inputList:
    if animal == "Fox":
        obj = Fox()
    elif animal == "Bug":
        obj = Bug()
    elif animal == "Chicken":
        obj = Chicken()
    elif animal == "Grass":
        obj = Grass()
    elif animal == "Sheep":
        obj = Sheep()
    elif animal == "Leaves":
        obj = Leaves()
    elif animal == "Antelope":
        obj = Antelope()
    elif animal == "BigFish":
        obj = BigFish()
    elif animal == "LittleFish":
        obj = LittleFish()
    elif animal == "Bear":
        obj = Bear()
    elif animal == "Cow":
        obj = Cow()
    elif animal == "Giraffe":
        obj = Giraffe()
    elif animal == "Lion":
        obj = Lion()
    elif animal == "Panda":
        obj = Panda()
    else:
        print(animal + " is not contained in the zoo")

    animalList.append(obj)

foodChain(animalList)