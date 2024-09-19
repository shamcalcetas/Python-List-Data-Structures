# bird_species_list.py

# List of 12 bird species
bird_species_list = [
                      "Raven", "Clark's Nutcracker", "White-throated Sparrow", "Ancient Murrelet",
                      "Calliope Hummingbird", "Wild Turkey", "Wood Duck", "Hoatzin", 
                      "Trumpeter Swan", "Sandhill Crane", "Loon", "Arctic Tern"
                    ]

# Print the entire list
print("12 Bird Species List: ")
print(bird_species_list)

# Access and print the 9th index
print()
print("9th Bird Species is: ")
print(bird_species_list[8])

# Update the 6th index to "Eagle"
bird_species_list[5] = "Eagle"
print()
print("Updated 6th Bird Species: ")
print(bird_species_list)

# Delete the 8th index
del bird_species_list[7]
print()
print("Updated Bird Species List After Deleting 8th: ")
print(bird_species_list)

# Slice the list from index 3 to 7
print()
print("Sliced Portion from 3 to 7:")
print(bird_species_list[3:8])

# Print the last index
print()
print("Last Bird Species is: ")
print(bird_species_list[-1])