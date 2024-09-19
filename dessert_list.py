# dessert_list.py

# List of 10 desserts
dessert_list = [
                  "Ice cream", "Mochi", "Gelatin", "Pudding", "Pie",
                  "Brownies", "S'mores", "Candies", "Custards", "Muffins"
                  ]

# Print the entire list
print("10 Dessert List: ")
print(dessert_list)

# Access and print the 4th index
print()
print("4th Dessert is: ")
print(dessert_list[3])

# Update the 6th index to "Chocolate Cake"
dessert_list[5] = "Chocolate Cake"
print()
print("Updated 6th Dessert: ")
print(dessert_list)

# Delete the 3rd index
del dessert_list[2]
print()
print("Updated Dessert List After Deleting 3rd: ")
print(dessert_list)

# Print the last index
print()
print("Last Dessert is: ")
print(dessert_list[-1])