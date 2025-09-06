##Zadanie 1. Stacja meteorologiczna

weeklyTemp = [1.5, 3, 2, 0, -1 , 1.9, 0.1]
print(weeklyTemp)

avgTemp = sum(weeklyTemp)/len(weeklyTemp)
reverseList = list(reversed(weeklyTemp))


print("Maksymalna temperatura w tygodniu to:", max(weeklyTemp), "\n"
      "Minimalna temperatura w tygodniu to:", min(weeklyTemp), "\n"
      "Średnia temperatura to: ", avgTemp,  "\n"
      "Posortowana lista: ", sorted(weeklyTemp), "\n"
      "Odwrócona lista: ", reverseList)

