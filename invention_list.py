# invention_list.py

# List of 8 famous inventions
invention_list = [
                    "Penicillin", "Internet", "Telephone", "Battery", 
                    "Television", "Steam Engine", "Printing Press", "Compass"
                  ]

# Print the entire list
print("8 Invention List: ")
print(invention_list)

# Access and print the 6th index
print()
print("6th Invention is: ")
print(invention_list[5])

# Update the 2nd index to "Lightbulb"
invention_list[1] = "Lightbulb"
print()
print("Updated 2nd Invention: ")
print(invention_list)

# Delete the 5th index
del invention_list[4]
print()
print("Updated Invention List After Deleting 5th: ")
print(invention_list)

# Print the last index
print()
print("Last Invention is: ")
print(invention_list[-1])