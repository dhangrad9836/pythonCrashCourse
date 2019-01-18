pizzas = ['chicken', 'pepperoni', 'supreme']
for pizza in pizzas:
    print("I like " + pizza.lower() + " pizza!")
print("I really like pizza")


print("##################################################################")

#part 2 try it yourself

#count to twenty using a for loop

for value in range(1,21):
    print(value)

#make a list to populate up to one million
#count = [value for value in range(1,100000)]
#print(count) note that the output takes too long to produce

#make a list from 1 - 1000000000, then use min() and max() to make sure
#the list actually starts at one and ends at one million also use sum()
count = []
for value in range(1,10):
    count.append(value)
print(min(count))
print(max(count))
print(sum(count))

print("*****")
print("*****")
print("*****")
#print a list of even numbers from 1 -20
count = []
for value in range(1,21,2):
    count.append(value)
print(count)

#print multiples of 3 from 3 to 30
print("##############")
count = []
for value in range(3,31,3):
    count.append(value)
print(count)
print()
print("################")

cubes = [value**3 for value in range(1,11)]
print(cubes)

#########################
print("\n")
pizzas = ['chicken', 'pepperoni', 'supreme', 'peppers', 'onion', 'bacon']
print("The first three items are:")
print(pizzas[:3])

print("the items from the middle are:")
print(pizzas[2:4])

print("the last three itemss are:")
print(pizzas[-3:])

pizzas = ['chicken', 'pepperoni', 'supreme']
friend_pizza = pizzas[:]
print("friend pizza is:")
print(friend_pizza)

pizzas.append("bacon")
friend_pizza.append("pepper")

print("friend pizza is")
for pizza in friend_pizza[:1]:
    print(pizza)
print("my pizza")
for pizza in pizzas[:]:
    print(pizza)

print("#########################")
print("tuples")

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("\n")
for dimension in dimensions:
    print(dimension)

#redefine the tuple since we cannot reassign a value to a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

print("redefine")
dimensions = (400, 100)
print("\nModifiend dimensions:")
for dimension in dimensions:
    print(dimension)
