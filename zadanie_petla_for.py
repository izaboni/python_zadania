##Dodawanie trzech liczb dodatnich parzystych

wynik = 0
i = 0
while i < 3:
    x = int(input("podaj liczbę: "))
    if (x > 0 and x % 2 == 0):
        wynik += x
        i += 1
    else:
        print("Podano nieodpowiednią liczbę")
        continue    
print("Wynik to: ", wynik)

