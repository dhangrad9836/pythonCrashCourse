#print("Hello")


#lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[-1].title())

personal_lists = ['Darren', 'Dhanpat', 'bmw', 'suv']
message = 'My name is ' + personal_lists[0].title() + " " + personal_lists[1].title() + ' I would' \
    ' like to own a ' + personal_lists[2].upper() + ' or an ' + personal_lists[3].upper()
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#popped_motorcycles = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycles)

last_owned = motorcycles.pop(0)
print("The last motorcycle I owned was a " + last_owned.title() + ".")
