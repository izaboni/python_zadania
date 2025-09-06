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