# world_wonders_list.py

# List of 7 wonders of the world
world_wonders_list = [
                        "Colosseum", "Machu Picchu", "Taj Mahal", "Christ the Redeemer", 
                        "Great Wall of China", "Chichén Itzá", "Petra"
                    ]

# Print the entire list
print("7 Wonders of the World List: ")
print(world_wonders_list)

# Access and print the 4th index
print()
print("4th Wonders of the World is: ")
print(world_wonders_list[3])

# Update the 2nd index to "Great Wall of China"
world_wonders_list[1] = "Great Wall of China"
print()
print("Updated 2nd Wonders of the World: ")
print(world_wonders_list)

# Delete the 5th index
del world_wonders_list[4]
print()
print("Updated Wonders of the World List After Deleting 5th: ")
print(world_wonders_list)

# Print the last index
print()
print("Last Wonders of the World is: ")
print(world_wonders_list[-1])