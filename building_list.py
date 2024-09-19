# building_list.py

# List of 8 famous buildings
building_list = [
                  "Taj Mahal", "Colosseum", "Tower of Pisa", "Empire State Building",
                  "Lotus Temple", "Big Ben", "The Gateway Arch", "Burj Khalifa"
                ]

# Print the entire list
print("8 Famous Building List: ")
print(building_list)

# Access and print the 5th index
print()
print("5th Famous Building is: ")
print(building_list[4])

# Update the 2nd index to "Eiffel Tower"
building_list[1] = "Eiffel Tower"
print()
print("Updated 2nd Famous Building: ")
print(building_list)

# Delete the 6th index
del building_list[5]
print()
print("Updated Famous Building List After Deleting 6th: ")
print(building_list)

# Print the last index
print()
print("Last Famous Building is: ")
print(building_list[-1])