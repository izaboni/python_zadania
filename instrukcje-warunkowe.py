
wybor = input("* mnożenie, / dzielenie, + dodawanie, - odejmowanie, warość bezwględna ||: ")

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

if (wybor == "*"):
    print(a * b)
elif (wybor == "/"):
    if (b == 0):
        print("nie dzieli się przez 0!")
    else:
            print(a / b)
elif (wybor == "+"):
    print(a + b)
elif (wybor == "-"):
    print(a - b)
elif (wybor == "||"):
    print(abs(a))
    print(abs(b))
else:
    print("wybrano zły znak!")
    
  

