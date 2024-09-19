# river_list.py

# List of 10 famous rivers
river_list = [
                "Yamuna River", "Hudson River", "River Thames", "River Tiber", "Seine",
                "Yangtze River", "Saint Lawrence River", "Ganges", "Spree", "Moskva River"
            ]

# Print the entire list
print("10 Famous River List: ")
print(river_list)

# Access and print the 6th index
print()
print("6th Famous River is: ")
print(river_list[5])

# Update the 8th index to "Nile River"
river_list[7] = "Nile River"
print()
print("Updated 8th Famous River: ")
print(river_list)

# Delete the 9th index
del river_list[8]
print()
print("Updated Famous River List After Deleting 9th: ")
print(river_list)

# Print the last index
print()
print("Last Famous River is: ")
print(river_list[-1])