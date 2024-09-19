# volcano_list.py

# List of 7 famous volcanoes
volcano_list = [
                  "Krakatoa", "Mount Etna", "Cotopaxi", "Eyjafjallajökull", 
                  "Mount Pinatubo", "Mauna Loa", "Mount Pelée"
              ]

# Print the entire list
print("7 Famous Volcano List: ")
print(volcano_list)

# Access and print the 4th index
print()
print("4th Famous Volcano is: ")
print(volcano_list[3])

# Update the 3rd index to "Mount Vesuvius"
volcano_list[2] = "Mount Vesuvius"
print()
print("Updated 3rd Famous Volcano: ")
print(volcano_list)

# Delete the 5th index
del volcano_list[4]
print()
print("Updated Famous Volcano List After Deleting 5th: ")
print(volcano_list)

# Print the last index
print()
print("Last Famous Volcano is: ")
print(volcano_list[-1])