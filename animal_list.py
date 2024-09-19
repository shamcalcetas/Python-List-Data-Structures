# animal_list.py

# List of 10 animal names
animal_list = [
                "Alligator", "Bear", "Cat", "Dog", "Flamingo",
                "Giraffe", "Lion", "Pig", "Sheep", "Tiger"
              ]

# Print the entire list
print("10 Animal List: ")
print(animal_list)

# Access and print the 3rd index
print()
print("3rd Animal is: ")
print(animal_list[2])

# Update the 6th index to "Elephant"
animal_list[5] = "Elephant"
print()
print("Updated 6th Animal: ")
print(animal_list)

# Delete the 8th index
del animal_list[7]
print()
print("Updated Animal List After Deleting 8th: ")
print(animal_list)

# Print the last index
print()
print("Last Animal is: ")
print(animal_list[-1])