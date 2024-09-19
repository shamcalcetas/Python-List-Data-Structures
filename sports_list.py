# sports_list.py

# List of 10 popular sports
sports_list = [
                "Soccer", "Cricket", "Tennis", "Golf", "Baseball",
                "Snooker", "Volleyball", "Hockey", "Rugby", "Football"
              ]

# Print the entire list
print("10 Popular Sport List: ")
print(sports_list)

# Access and print the 6th index
print()
print("6th Popular Sport is: ")
print(sports_list[5])

# Update the 4th index to "Basketball"
sports_list[3] = "Basketball"
print()
print("Updated 4th Popular Sport: ")
print(sports_list)

# Delete the 9th index
del sports_list[8]
print()
print("Updated Popular Sport List After Deleting 8th: ")
print(sports_list)

# Print the last index
print()
print("Last Popular Sport is: ")
print(sports_list[-1])