# festival_celebration_list.py

# List of 10 festival celebrations
festival_celebration_list = [
                              "Christmas", "Chinese New Year", "Diwali", "Eid al-Fitr", "Easter",
                              "Halloween", "Hanukkah", "New Year's Eve", "Carnival", "Independence Day"
                            ]

# Print the entire list
print("10 Festival Celebration List: ")
print(festival_celebration_list)

# Access and print the 5th index
print()
print("5th Festival Celebration is: ")
print(festival_celebration_list[4])

# Update the 3rd index to "Thanksgiving"
festival_celebration_list[2] = "Thanksgiving"
print()
print("Updated 3rd Festival Celebration: ")
print(festival_celebration_list)

# Delete the 7th index
del festival_celebration_list[6]
print()
print("Updated Festival Celebration List After Deleting 7th: ")
print(festival_celebration_list)

# Print the last index
print()
print("Last Festival Celebration is: ")
print(festival_celebration_list[-1])