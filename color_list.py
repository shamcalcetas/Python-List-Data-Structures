# color_list.py

# List of 15 colors
color_list = [
                "Blue", "Green", "Brown", "Gray", "Red", 
                "White", "Pink", "Yellow", "Black", "Beige",
                "Navy Blue", "Maroon", "Magenta", "Orange", "Aqua",
            ]

# Print the entire list
print("15 Color List: ")
print(color_list)

# Access and print the 10th index
print()
print("10th Color is: ")
print(color_list[9])

# Update the 4th index to "Purple"
color_list[3] = "Purple"
print()
print("Updated 4th Color: ")
print(color_list)

# Delete the 5th index
del color_list[4]
print()
print("Updated Color List After Deleting 5th: ")
print(color_list)

# Slice the list from index 2 to 8
print()
print("Sliced Portion from 2 to 8:")
print(color_list[2:9])

# Print the last index
print()
print("Last Color is: ")
print(color_list[-1])