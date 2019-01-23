#Dictionaries have key:value pairs and each dictionary are seperated by a comma in a single dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#update our aliens with x and y coordinates
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("empty space\n")
#adding items to an empty dict
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("#")
#changing a value to another value in a dict
alien_0 = {'color': 'green'}
print("The color is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The color is now " + alien_0['color'] + ".")


print('#\n')
print()

