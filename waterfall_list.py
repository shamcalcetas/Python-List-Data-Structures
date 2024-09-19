# waterfall_list.py

# List of 10 famous waterfalls
waterfall_list = [
                    "Victoria Falls", "Gullfoss Falls", "Angel Falls", "Iguazu Falls", "Yosemite Falls",
                    "Jog Falls", "Ban Gioc Waterfalls", "Sutherland Falls", "Kaieteur Falls", "Tugela Falls"
                  ]

# Print the entire list
print("10 Famous Waterfalls List: ")
print(waterfall_list)

# Access and print the 8th index
print()
print("8th Famous Waterfalls is: ")
print(waterfall_list[7])

# Update the 5th index to "Niagara Falls"
waterfall_list[4] = "Niagara Falls"
print()
print("Updated 5th Famous Waterfalls: ")
print(waterfall_list)

# Delete the 9th index
del waterfall_list[8]
print()
print("Updated Famous Waterfalls List After Deleting 9th: ")
print(waterfall_list)

# Print the last index
print()
print("Last Famous Waterfalls is: ")
print(waterfall_list[-1])