# famous_bridge_list.py

# List of 8 famous bridges
famous_bridge_list = [
                        "Tower Bridge", "Ponte di Rialto", "Ponte Vecchio", "Sydney Harbour Bridge", 
                        "Brooklyn Bridge", "Akashi-Kaikyo Bridge", "Old Bridge Mostar", "Viaduc de Millau"
                    ]

# Print the entire list
print("8 Famous Bridge List: ")
print(famous_bridge_list)

# Access and print the 3rd index
print()
print("3rd Famous Bridge is: ")
print(famous_bridge_list[2])

# Update the 6th index to "Golden Gate Bridge"
famous_bridge_list[5] = "Golden Gate Bridge"
print()
print("Updated 6th Famous Bridge: ")
print(famous_bridge_list)

# Delete the 7th index
del famous_bridge_list[6]
print()
print("Updated Famous Bridge List After Deleting 7th: ")
print(famous_bridge_list)

# Print the last index
print()
print("Last Famous Bridge is: ")
print(famous_bridge_list[-1])