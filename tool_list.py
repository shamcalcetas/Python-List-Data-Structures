# tool_list.py

# List of 10 tools used in carpentry
tool_list = [
              "Chisel", "Circular Saw", "Drill", "Tape Measure", "Hand Saw",
              "Pencil", "Planes", "Level", "Sharpening tools", "Jigsaw"
            ]

# Print the entire list
print("10 Carpentry Tool List: ")
print(tool_list)

# Access and print the 4th index
print()
print("4th Carpentry Tool is: ")
print(tool_list[3])

# Update the 7th index to "Hammer"
tool_list[6] = "Hammer"
print()
print("Updated 7th Carpentry Tool: ")
print(tool_list)

# Delete the 5th index
del tool_list[4]
print()
print("Updated Carpentry Tool List After Deleting 5th: ")
print(tool_list)

# Print the last index
print()
print("Last Carpentry Tool is: ")
print(tool_list[-1])