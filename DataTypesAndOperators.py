print(3 + 8)
print(1 + 2 + 3 * 3)
print(3 ** 2)
print(9 % 2)

#My electricity bills for the last three months have been $23, $32 and $64. 
#What is the average monthly electricity bill over the three month period?

print((23 + 32 + 64) / 3)

#Two parts of a floor need tiling. 
#One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

# How many packages of tiles do you need to buy to tile both parts of the floor?
print(9 * 7 + 5 * 7)

#You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
print(17 * 6 - (9 * 7 + 5 * 7))

##Variables and Assignment Operators

mv_population  = 39250000
mv_population = mv_population + 1000
print(mv_population)

#
reservoir_volume = 4.445e8
rainfall = 5e6

## decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions
reservoir_volume -= 2.5e5

print(reservoir_volume)

#Changing Variable Values

carrots = 24
rabbits = 8
carrots_per_rabbit = carrots / rabbits
rabbits = 12

print(rabbits)
print(carrots_per_rabbit)

#Boolean Data Type and Logical Operators

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population / sf_area
rio_de_janeiro_pop_density = rio_population / rio_area

if san_francisco_pop_density > rio_de_janeiro_pop_density:
    print(True)
else:
    print(False)


ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'


username = "programming"
password = "fun"


#######
given_name = "Ada"
middle_name = "Augusta"
family_name = "Lovelace"

name = len(given_name + middle_name + family_name)
print(name)


print(type(666))
print(type(666.9))
print(type('kedfhkshkd'))
print(type(True))

print(0 + 8)
#print(0 + "5")
#print("8" + 12)



mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)

print(f"This week's total sales: {total_sales}")

#String methods and Attributes

text = "hello, WORLD!"
capitalized_text = text.capitalize() # The first character h is converted to uppercase. All other characters are converted to lowercase.
casefolded_text = text.casefold()   # All characters are converted to lowercase. More aggressive than lower().
centered_text = text.center(20, '-') # The original text is centered within a 2-character wide string, with - used as the fill character.
counted_text = text.lower().count("l")
encoded_text = text.encode(encoding="utf-8", errors="strict") # The text is encoded as a bytes object using UTF-8 encoding.
endswithed_text = text.endswith("!") # Returns True if the text ends with the specified suffix, otherwise False.
finded_text = text.find("el") # Returns the lowest index of the substring if found in the text. If not found, it returns -1.
print(capitalized_text)
print(casefolded_text)
print(centered_text)
print(counted_text)
print(encoded_text)
print(endswithed_text)
print(finded_text)


#formatted strings
name = "Ada Lovelace"
age = 36
formatted_string = "My name is {}. I'm {} years old".format(name, age)

print(formatted_string)

#split
csv = "name,age,occupation"
name, age, occupation = csv.split(",")  # Splits the string at each comma and unpacks the values into variables     
print(name)        # Output: "name"
print(age)         # Output: "age"     

new_str = "The cow jumped over the moon."
new_str.split()
print(new_str.split())

print(new_str.split(' ', 1))
print(new_str.split(' ', 2))
print(new_str.split(' ', 3))
print(new_str.split(' ', 4))
print(new_str.split('.'))
print(new_str.split(None, 3))

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

verse_len =len(verse)
print(verse_len)

index_of_and = verse.find("and")
print(index_of_and) 

index_of_you = verse.rfind("you")
print(index_of_you)

print(verse.count("you"))