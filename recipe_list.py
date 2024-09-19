# recipe_list.py

# List of 15 recipes
recipe_list = [
                "Tuna Casserole", "Spaghetti", "Chicken Curry", "Mac and cheese", "Beef Steak",
                "Bibimbap", "Kimbap", "Ramen", "Tteokbokki", "Bulgogi",
                "Carbonara", "Kare-kare", "Kaldereta", "Sinigang", "Adobo"
              ]

# Print the entire list
print("15 Recipe List: ")
print(recipe_list)

# Access and print the 12th index
print()
print("12th Recipe is: ")
print(recipe_list[11])

# Update the 9th index to "Lasagna"
recipe_list[8] = "Lasagna"
print()
print("Updated 9th Recipe: ")
print(recipe_list)

# Delete the 11th index
del recipe_list[10]
print()
print("Updated Recipe List After Deleting 11th: ")
print(recipe_list)

# Slice the list from index 5 to 10
print()
print("Sliced Portion from 5 to 10:")
print(recipe_list[5:11])

# Print the last index
print()
print("Last Recipe is: ")
print(recipe_list[-1])