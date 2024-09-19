# ocean_list.py

# List of 5 oceans
ocean_list = [
                "Arctic Ocean", "Southern Ocean", "Atlantic Ocean", "Pacific Ocean", "Indian Ocean"
            ]

# Print the entire list
print("5 Ocean List: ")
print(ocean_list)

# Access and print the 3rd index
print()
print("3rd Ocean is: ")
print(ocean_list[2])

# Update the 2nd index to "Pacific Ocean"
ocean_list[1] = "Pacific Ocean"
print()
print("Updated 2nd Ocean: ")
print(ocean_list)

# Delete the 4th index
del ocean_list[3]
print()
print("Updated Ocean List After Deleting 4th: ")
print(ocean_list)

# Print the last index
print()
print("Last Ocean is: ")
print(ocean_list[-1])