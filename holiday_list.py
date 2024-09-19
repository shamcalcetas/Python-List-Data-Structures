# holiday_list.py

# List of 12 holidays
holiday_list = [
                  "New Year", "Araw ng Kagitingan", "Eid'l Fitr", "Labor Day",
                  "Independence", "National Heroes", "Bonifacio Day", "Rizal Day",
                  "All Saints' Day", "Ninoy Aquino Day", "Black Saturday", "All Souls' Day"
                ]

# Print the entire list
print("12 Holiday List: ")
print(holiday_list)

# Access and print the 9th index
print()
print("9th Holiday is: ")
print(holiday_list[8])

# Update the 3rd index to "Christmas"
holiday_list[2] = "Christmas"
print()
print("Updated 3rd Holiday: ")
print(holiday_list)

# Delete the 11th index
del holiday_list[10]
print()
print("Updated Holiday List After Deleting 11th: ")
print(holiday_list)

# Slice the list from index 2 to 7
print()
print("Sliced Portion from 2 to 7:")
print(holiday_list[2:8])

# Print the last index
print()
print("Last Holiday is: ")
print(holiday_list[-1])