class Pokemon:
    def __init__(self, name, power, color, evolve):
        self.name = name
        self.power = power
        self.color = color
        self.evolve = evolve  
    def who_are_you(self):
        print(f"I'm {self.name} my power is {self.power} my color is {self.color}") 

def main():

    Pikatchu = Pokemon("Pikatchu", "electricity", "yellow", "Raichu")
    Charmander = Pokemon("Charmander", "fire", "orange", "Charmeleon")


    Pikatchu.who_are_you()
    Charmander.who_are_you()           

if __name__ == "__main__":
    main()