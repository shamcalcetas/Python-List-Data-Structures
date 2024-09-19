# furniture_list.py

# List of 12 furniture items
furniture_list = [
                    "Table", "Chair", "Bed", "Cabinet",
                    "Desk", "Ottoman", "TV Stand", "Wardrobe",
                    "Stool", "Bench", "Cupboard", "Bookcase"
                  ]

# Print the entire list
print("12 Furniture List: ")
print(furniture_list)

# Access and print the 8th index
print()
print("8th Furniture is: ")
print(furniture_list[7])

# Update the 5th index to "Sofa"
furniture_list[4] = "Sofa"
print()
print("Updated 2nd Furniture: ")
print(furniture_list)

# Delete the 10th index
del furniture_list[9]
print()
print("Updated Furniture List After Deleting 10th: ")
print(furniture_list)

# Print the last index
print()
print("Last Furniture is: ")
print(furniture_list[-1])