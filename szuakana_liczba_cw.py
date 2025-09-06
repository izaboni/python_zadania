## x - szukana liczba

wantedNumber = 40
givenNumber = 0
countOfTry = 3
i = 0

##wersja podstawowa
##print("Program do zgadywania liczby")
##
##while i < countOfTry:
##      givenNumber = int(input("Podaj liczbę: "))
##      if (wantedNumber == givenNumber):
##          print("Brawo! szukana liczba to:", wantedNumber, "Wygrywasz zupełnie nic")
##          break
##      else:
##          i += 1
##          print("To nie jest szukana liczba! Pozostało prób: ", countOfTry - i)
##                     
##print("Koniec tego fantastycznego programu")
##

##wersja hard z licznikiem prób

##print("Program do zgadywania liczby")
##
##while i < countOfTry:
##      givenNumber = int(input("Podaj liczbę: "))
##      if (wantedNumber == givenNumber):
##          print("Brawo! szukana liczba to:", wantedNumber)
##          break
##      elif(wantedNumber > givenNumber):
##          i += 1
##          print("Ta liczba jest mniejsza od pożądanej. Pozostała liczba prób:", countOfTry - i)
##      elif(wantedNumber < givenNumber):
##          i += 1
##          print("Ta liczba jest większa od pożądanej. Pozostała liczba prób:", countOfTry - i)
##
##print("Koniec tego fantastycznego programu")
##

##wersja bez licznika prób
print("Program do zgadywania liczby")

while wantedNumber != givenNumber:
      givenNumber = int(input("Podaj liczbę: "))
      if (wantedNumber == givenNumber):
          print("Brawo! szukana liczba to:", wantedNumber)
          break
      elif(wantedNumber > givenNumber):
          print("Ta liczba jest mniejsza od pożądanej")
      elif(wantedNumber < givenNumber):
          print("Ta liczba jest większa od pożądanej")

print("Koniec tego fantastycznego programu")
