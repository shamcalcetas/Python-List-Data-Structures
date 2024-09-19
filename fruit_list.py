# fruit_list.py

# List of 12 fruits
fruit_list = [
                "Apple", "Orange", "Grapes", "Banana",
                "Pineapple", "Mango", "Watermelon", "Lime",
                "Strawberry", "Rambutan", "Cherry", "Peach"
            ]

# Print the entire list
print("12 Fruit List: ")
print(fruit_list)

# Access and print the 9th index
print()
print("9th Fruit is: ")
print(fruit_list[8])

# Update the 2nd index to "Mango"
fruit_list[1] = "Mango"
print()
print("Updated 2nd Fruit: ")
print(fruit_list)

# Delete the 10th index
del fruit_list[9]
print()
print("Updated Fruit List After Deleting 10th: ")
print(fruit_list)

# Slice the list from index 4 to 7
print()
print("Sliced Portion from 4 to 7:")
print(fruit_list[4:8])

# Print the last index
print()
print("Last Fruit is: ")
print(fruit_list[-1])