# mountain_list.py

# List of 8 mountain names
mountain_list = [
                  "Sierra", "Carmel", "Aneto", "Mount Blanc",
                  "Apo", "Denali", "Ben Nevis", "Aconcagua"
                ]

# Print the entire list
print("8 Mountain List: ")
print(mountain_list)

# Access and print the 5th index
print()
print("5th Mountain is: ")
print(mountain_list[4])

# Update the 3rd index to "Everest"
mountain_list[2] = "Everest"
print()
print("Updated 3rd Mountain: ")
print(mountain_list)

# Delete the 6th index
del mountain_list[5]
print()
print("Updated Mountain List After Deleting 6th: ")
print(mountain_list)

# Print the last index
print()
print("Last Mountain is: ")
print(mountain_list[-1])