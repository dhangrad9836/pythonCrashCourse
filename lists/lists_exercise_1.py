#print("hello")

people_to_invite = ['kevin heart', 'russel peters', 'Mary Smith']

print("Hello " + people_to_invite[0].title() + ", you are invited to dinner")
print("Hello " + people_to_invite[1].title() + ", you are invited to dinner")
print("Hello " + people_to_invite[2].title() + ", you are invited to dinner")
print("Sorry " + people_to_invite[1].title() + " that you can't make it to dinner")
people_to_invite.pop(1)
print(people_to_invite)
people_to_invite.insert(1, 'Donald trump')
print(people_to_invite)
print("Hello " + people_to_invite[0].title() + ", you are invited to dinner")
print("Hello " + people_to_invite[1].title() + ", you are invited to dinner")
print("Hello " + people_to_invite[2].title() + ", you are invited to dinner")

cars = ['BMmw', 'AUdi', 'toyota', 'subaru']
#cars.sort()
#print(cars)
#cars.sort(reverse=True)
#print(cars)

print("Here is the original list")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list")
print(cars)

print(len(cars))