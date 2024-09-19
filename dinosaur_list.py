# dinosaur_list.py

# List of 8 dinosaur names
dinosaur_list = [
                  "Triceratops", "Pterodactyl", "Brontosaurus", "Diplodocus", 
                  "Stegosaurus", "Ankylosaurus", "Spinosaurus", "Velociraptor"
                ]

# Print the entire list
print("8 Dinosaur List: ")
print(dinosaur_list)

# Access and print the 4th index
print()
print("4th Dinosaur is: ")
print(dinosaur_list[3])

# Update the 6th index to "Tyrannosaurus Rex"
dinosaur_list[5] = "Tyrannosaurus Rex"
print()
print("Updated 6th Dinosaur: ")
print(dinosaur_list)

# Delete the 7th index
del dinosaur_list[6]
print()
print("Updated Dinosaur List After Deleting 7th: ")
print(dinosaur_list)

# Print the last index
print()
print("Last Dinosaur is: ")
print(dinosaur_list[-1])