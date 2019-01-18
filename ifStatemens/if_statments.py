cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("\n")
print("\n")
print("\n")
print("Pizzeria")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

print("\n")
print("\n")
print("\n")
print("\n")
print("Chcking a list if empty")

requested_toppings = []
#this checks if the list above is empty
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("Finished making your pizza!")
else:
    print("are you sure you want a plain pizza")

print("\n")
print("\n")
print("\n")
print("\n")
print("Using multiple lists")
available_toppints = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppints:
        print("Adding " + requested_topping + ".")
    else:
        print("sorry we don't have " + requested_topping + ".")
print("Finished making you pizza")