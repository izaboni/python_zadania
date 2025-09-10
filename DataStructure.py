#list

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(months[0])    
print(months[3])
print(months[-1])
#print(months[100]) #IndexError: list index out of range

q1 = months[0:3]
print(q1)

q2 = months[3:6]
print(q2)

q3 = months[6:9]
print(q3)

q4 = months[9:12]
print(q4)

first_half = months[0:6]
print(first_half)

second_half = months[6:12]
print(second_half)

print(len(months))

greeting = "HELLO THERE!"
print(len(greeting))

list_of_random_things = [3.14, "Hello", 42, True, None]
print(list_of_random_things)
print(list_of_random_things[1])
print(list_of_random_things[-2])

#list_of_random_things[len(list_of_random_things)] 
#print(list_of_random_things)

list_of_random_things[len(list_of_random_things) - 1] 
print(list_of_random_things)


list_of_random_things[-1]  
print(list_of_random_things)

#Slice and Dice with Lists

list_of_random_things = [3.14, "Hello", 42, True, None]
print(list_of_random_things[1:4])
print(list_of_random_things[1:2])
print(list_of_random_things[1:1])
print(list_of_random_things[0:0])
print(list_of_random_things[1:3])
print(list_of_random_things[0:3])
print(list_of_random_things[:2])
print(list_of_random_things[2:])

# Are you in or out?
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("January" in months)
print("lol" in months)
print("lol" not in months)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(3 in numbers)
print(7 in numbers)
print(100 not in numbers)

#mutability of Lists

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers[0] = 10
numbers[5] = 42
numbers[8] = 'seven'
numbers[-1] = '$%'
print(numbers)

greeting = "Hello, world!"
#greeting[0] = 'J'  # This will raise a TypeError
#print(greeting)

month = 8
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(days_in_month[month - 1])

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

print(eclipse_dates[-3:])

#Useful List Methods

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers)) 
print(sorted(numbers))
numbers.append(7)
print(numbers)

new_str = "\n".join(["Hello", "world!"])
print(new_str)

new_str = "\r".join(["@@@"])
print(new_str)

letter_list = ['a', 'b', 'c', 'd', 'e']
letter_list.append('f')
print(letter_list)

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)])) #długość najdłuższej listy
print(min([len(a), len(b), len(c)])) #długość najkrótszej listy


print([len(a), len(b), len(c)])

names = ["Mary", "Isla", "Sam"]
print(" & ".join(sorted(names)))
print(sorted(names))

#Tuples

my_tuple = 1, 'a', 3.14 

x, y, z = my_tuple
print(x)

#example of tuple unpacking
my_second_tuple = (2, 'b', 6.28)
print(my_second_tuple)

#empty tuple
empty_tuple = ()
print(empty_tuple)

#single element tuple
single_element_tuple = (42,)
print(single_element_tuple)

location = (32.7767, -96.7970)  # Tuple representing (latitude, longitude)

print("Latitude:", location[0])
print("Longitude:", location[1])