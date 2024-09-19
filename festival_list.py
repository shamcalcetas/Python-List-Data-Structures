# festival_list.py

# List of 15 festivals around the world
festival_list = [
                  "Day of the Dead", "Holi", "Songkran", "La Tomatina", "Mardi Gras in New Orleans",
                  "Oktoberfest", "Rio Carnival", "Burning Man", "St. Patrick's Day", "Venice Carnival",
                  "Holy Week", "Glastonbury Festival", "Boryeong Mud Festival", "Hermanus Whale Festival", "Yi Peng"
                ]

# Print the entire list
print("15 Festival List: ")
print(festival_list)

# Access and print the 7th index
print()
print("7th Festival is: ")
print(festival_list[6])

# Update the 11th index to "Diwali"
festival_list[10] = "Diwali"
print()
print("Updated 11th Festival: ")
print(festival_list)

# Delete the 9th index
del festival_list[8]
print()
print("Updated Festival List After Deleting 9th: ")
print(festival_list)

# Slice the list from index 5 to 12
print()
print("Sliced Portion from 5 to 12:")
print(festival_list[5:13])

# Print the last index
print()
print("Last Festival is: ")
print(festival_list[-1])