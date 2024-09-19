# animal_species_list.py

# List of 7 animal species
animal_species_list = [
                        "Wolf", "Panda", "Whale", "Horse", "Polar Bear",
                        "Turtle", "Earthworm"
                      ]

# Print the entire list
print("7 Animal Species List: ")
print(animal_species_list)

# Access and print the 2nd index
print()
print("2nd Animal Species is: ")
print(animal_species_list[1])

# Update the 5th index to "Gorilla"
animal_species_list[4] = "Gorilla"
print()
print("Updated 5th Animal Species: ")
print(animal_species_list)

# Delete the 6th index
del animal_species_list[5]
print()
print("Updated Animal Species List After Deleting 6th: ")
print(animal_species_list)

# Print the last index
print()
print("Last Animal Species is: ")
print(animal_species_list[-1])