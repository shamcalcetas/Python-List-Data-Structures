# actor_list.py

# List of 10 famous actors
actor_list = [
               "Robert Downey Jr.", "Brad Pitt", "Tom Cruise", "Will Smith", "Tom Hanks",
                "Dwayne Johnson", "Bruce Willis", "Keanu Reeves", "Nicolas Cage", "Jackie Chan"
              ]

# Print the entire list
print("10 Famous Actor List: ")
print(actor_list)

# Access and print the 7th index
print()
print("7th Famous Actor is: ")
print(actor_list[6])

# Update the 3rd index to "Leonardo DiCaprio"
actor_list[2] = "Leonardo DiCaprio"
print()
print("Updated 3rd Famous Actor: ")
print(actor_list)

# Delete the 8th index
del actor_list[7]
print()
print("Updated Famous Actor List After Deleting 8th: ")
print(actor_list)

# Print the last index
print()
print("Last Famous Actor is: ")
print(actor_list[-1])