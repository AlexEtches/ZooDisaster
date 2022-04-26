from ZooAnimal import *

inputString = "Fox,Bug,Chicken,Grass,Sheep"
#extra test cases, all working
#inputString = "BigFish,LittleFish,Fox,Chicken,Cow,Grass"
#inputString = "Bear,Sheep,Chicken,Bug,Leaves,Giraffe,Grass,Antelope"
#inputString = "Cow,Grass,Antelope,Lion,Leaves,Panda"
inputList=inputString.split(",")
animalList = []
outputList = []
remaining = ""

def foodChain(Animals):

    length = len(Animals)

    for i in range(len(Animals)):
        if len(Animals) == 1:
            break

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
    #if no animals were removed from the list, return false
    if len(Animals) == length:
        return False
        

def toString(animalList):
    if len(animalList) == 1:
        return animalList[0].value    
    else:
        string = []
        for animal in animalList:
            string.append(animal.value)
        return string

outputList.append(inputString)

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

while foodChain(animalList) != False:
    foodChain(animalList)
    
animalOutput = toString(animalList)

if type(animalOutput) == str:
    outputList.append(animalOutput)
else:
    for item in animalOutput:
        remaining += str(item + ",")
        #removes trailing comma if there is one
        if remaining[-1]==',':
            result = remaining[:-1] 
        else:
            remaining
    outputList.append(result)
    
print(outputList)