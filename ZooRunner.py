from ZooAnimal import *

inputString = "Fox,Bug,Chicken,Grass,Sheep"
inputList=inputString.split(",")
animalList = []
outputList = []

def foodChain(Animals):

    for i in range(len(Animals)):
        if i == 0:
            Animals[i].eat(Animals[i+1].value)
            if Animals[i].canEat == True:
                outputList.append(Animals[i].value + " eats " + Animals[i+1].value)
                Animals.remove(Animals[i+1])
                break

        elif i == (len(Animals)-1):
            Animals[i].eat(Animals[i-1].value)
            if Animals[i].canEat == True:
                outputList.append(Animals[i].value + " eats " + Animals[i-1].value)
                Animals.remove(Animals[i-1])
                break

        elif i > 0 and i < (len(Animals)-1):
            Animals[i].eat(Animals[i+1].value)
            if Animals[i].canEat== True:
                outputList.append(Animals[i].value + " eats " + Animals[i+1].value)
                Animals.remove(Animals[i+1])
                break

            Animals[i].eat(Animals[i-1].value)
            if Animals[i].canEat== True:
                outputList.append(Animals[i].value + " eats " + Animals[i-1].value)
                Animals.remove(Animals[i-1])
                break
        else:
            exit
        

def toString(animalList):
    if len(animalList) == 1:
        return animalList[0].value    
    else:
        string = []
        for animal in animalList:
            string.append(animal.value)
        return string

for item in inputList:
        outputList.append(item)

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

while len(animalList) > 1:
    foodChain(animalList)
    
outputList.append(toString(animalList))
print(outputList)