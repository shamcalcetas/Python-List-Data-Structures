# natural_landmark_list.py

# List of 10 natural landmarks
natural_landmark_list = [
                          "Uyuni Salt Flat", "Cliffs of Moher", "Rocky Mountains", "Fox Glacier", "Cave of the Crystals",
                          "Chocolate Hills", "Sundarbans", "Blyde River Canyon", "Pulpit Rock", "Batad Rice Terraces"
                        ]

# Print the entire list
print("10 Natural Landmark List: ")
print(natural_landmark_list)

# Access and print the 8th index
print()
print("8th Natural Landmark is: ")
print(natural_landmark_list[7])

# Update the 5th index to "Grand Canyon"
natural_landmark_list[4] = "Grand Canyon"
print()
print("Updated 5th Natural Landmark: ")
print(natural_landmark_list)

# Delete the 9th index
del natural_landmark_list[8]
print()
print("Updated Natural Landmark List After Deleting 9th: ")
print(natural_landmark_list)

# Print the last index
print()
print("Last Natural Landmark is: ")
print(natural_landmark_list[-1])