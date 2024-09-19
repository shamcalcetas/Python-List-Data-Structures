# drink_list.py

# List of 8 popular drinks
drink_list = [
                "Water", "Soft drinks", "Beer", "Wine", 
                "Coconut Water", "Tea", "Soju", "Smoothies"
              ]

# Print the entire list
print("8 Popular Drinks List: ")
print(drink_list)

# Access and print the 4th index
print()
print("4th Popular Drinks is: ")
print(drink_list[3])

# Update the 3rd index to "Coffee"
drink_list[2] = "Coffee"
print()
print("Updated 3rd Popular Drinks: ")
print(drink_list)

# Delete the 7th index
del drink_list[6]
print()
print("Updated Popular Drinks List After Deleting 7th: ")
print(drink_list)

# Print the last index
print()
print("Last Popular Drinks is: ")
print(drink_list[-1])