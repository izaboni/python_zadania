##Program, który pozwoli użytkownikowi
## 1. Dodawać nowe definicje 
## 2. Szukać istniejących definicji
## 3. Usuwać wybrane definicje

paramName = "name"
paramPower = "power"
paramOwner = "owner"

pokedict = {}


while(True):
    print("")
    print("1: Add new definition: ")
    print("2: Find definition: ")
    print("3: Show dictonary")
    print("4: Remove value from dictonary")
    print("5: Finish it!")
    print("")

    choose = int(input("What do you want to do?: "))

    if (choose == 1):
            pokeName = input("\nWrite name of Pokemon: ")
            pokedict[paramName] = pokeName
            pokePower = input("\nWhat power have pokemon?: ")
            pokedict[paramPower] = pokePower
            pokeOwner = input("\nWho is the owner of this Pokemon?: ")
            pokedict[paramOwner] = pokeOwner
            print(pokedict)
    elif (choose == 2):
        print("2: Find definition: ")
        value = input("\nWhat are you looking for?: ")
        if value in pokedict:
                print(pokedict[value])    
    elif(choose == 3):
        print(pokedict) 
    elif(choose == 4):    
        value = input("\nWhat do you want remove?: ")
        if value in pokedict:
            del pokedict[value]
        print(pokedict)
    elif(choose == 5):
            break        
print(pokedict)
print("")