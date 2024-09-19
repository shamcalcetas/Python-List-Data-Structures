# technology_inventions_list.py

# List of 15 modern technology inventions
technology_inventions_list = [
                              "Artificial Intelligence", "Personal Computer", "5G", "Advanced Robotics", "Autonomous Vehicles",
                              "Blockchain", "Internet", "Airplane", "Quantum Computing", "Edge Computing",
                              "Light Bulb", "Steam Engine", "Artificial Light", "Electricity", "Television"
                            ]

# Print the entire list
print("15 Modern Technology Invention List: ")
print(technology_inventions_list)

# Access and print the 11th index
print()
print("11th Modern Technology Invention is: ")
print(technology_inventions_list[10])

# Update the 8th index to "Smartphone"
technology_inventions_list[7] = "Smartphone"
print()
print("Updated 8th Modern Technology Invention: ")
print(technology_inventions_list)

# Delete the 14th index
del technology_inventions_list[13]
print()
print("Updated Modern Technology Invention List After Deleting 14th: ")
print(technology_inventions_list)

# Slice the list from index 5 to 10
print()
print("Sliced Portion from 5 to 10:")
print(technology_inventions_list[5:11])

# Print the last index
print()
print("Last Modern Technology Invention is: ")
print(technology_inventions_list[-1])