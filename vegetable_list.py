# vegetable_list.py

# List of 7 vegetables
vegetable_list = [
                    "Onion", "Potato", "Cabbage", "Carrot",
                    "Broccoli", "Mushroom", "Garlic"
                  ]

# Print the entire list
print("7 Vegetable List: ")
print(vegetable_list)

# Access and print the 5th index
print()
print("5th Vegetable is: ")
print(vegetable_list[4])

# Update the 3rd index to "Spinach"
vegetable_list[2] = "Spinach"
print()
print("Updated 3rd Vegetable: ")
print(vegetable_list)

# Delete the 6th index
del vegetable_list[5]
print()
print("Updated Vegetable List After Deleting 6th: ")
print(vegetable_list)

# Print the last index
print()
print("Last Vegetable is: ")
print(vegetable_list[-1])