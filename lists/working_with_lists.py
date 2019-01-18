print("hello")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + " .\n")

print("Thank you, everyone. That was a great magic show!")


print("##################################################################")

#using range function to print a range of numbers
#note that this is an off by one value...only prints 1 -5 not up to 6
for value in range(1,6):
    print(value)

#USE range() to make a list of numbers by wrapping the list() function around thr range function
#this will print a range of numbers inside of a list
numbers = list(range(1,6))
print(numbers)

#using range() inside of list() and to only display even numbers
#note that you start with 2 then 11 which is an off by one to equal 10 and end with 2 designating evens
even_numbers = list(range(2,11,2))
print(even_numbers)

#putting squared numbers inside a list
#1 create an empty list
squares = []
#2 create the range
for value in range(1,11):
    #3 square the value and store inside the square variable
    square = value ** 2
    #4 append the  square value inside the squares list
    squares.append(square)
#print the squares
print(squares)

#shorter version of the code above without the temporary variable square
#we just appended the value **2 directly to squares list
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))


#LIST COMPREHENSION
#1 define the squares list
#2 define the expression value **2
#3 write the for loop....here it's with the range function
squares = [value **2 for value in range(1,11)]
print(squares)

print()
print()
print()
print("############## Slicing a list########################")

players = ['charles', 'matina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:]) #note that -1 is eli, -2 is florence, -3 is michael

#Looping through a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())



#######################foods.py##################################
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My fav foods are:")
print(my_foods)

print("\n")
print("\nMy friends fav foods are:")
print(friend_foods)

print("\n")
print("Tuples try it yourself exercises")

foods = ("chicken", "potatoes", "turkey", "carrots", "corn")
for food in foods:
    print(food)


print("Changed Menu")
foods = ("chicken", "soup", "peas", "carrots", "corn")
for food in foods:
    print(food)












