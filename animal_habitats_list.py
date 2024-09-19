# animal_habitats_list.py

# List of 8 animal habitats
animal_habitats_list = [
                         "Forest", "Grassland", "Desert", "Polar Regions", "Wetlands",
                         "Cave", "Freshwater", "Ocean"
                      ]

# Print the entire list
print("8 Animal Habitat List: ")
print(animal_habitats_list)

# Access and print the 5th index
print()
print("5th Animal Habitat is: ")
print(animal_habitats_list[4])

# Update the 3rd index to "Savannah"
animal_habitats_list[2] = "Savannah"
print()
print("Updated 3rd Animal Habitat: ")
print(animal_habitats_list)

# Delete the 6th index
del animal_habitats_list[5]
print()
print("Updated Animal Habitat List After Deleting 6th: ")
print(animal_habitats_list)

# Print the last index
print()
print("Last Animal Habitat is: ")
print(animal_habitats_list[-1])