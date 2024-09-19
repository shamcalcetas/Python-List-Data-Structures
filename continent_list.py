# continent_list.py

# List of 7 continents
continent_list = [
                    "Asia", "Europe", "North America", "South America", 
                    "Antarctica", "Africa", "Australia"
                  ]

# Print the entire list
print("7 Continent List: ")
print(continent_list)

# Access and print the 4th index
print()
print("4th Continent is: ")
print(continent_list[3])

# Update the 2nd index to "Africa"
continent_list[1] = "Africa"
print()
print("Updated 2nd Continent: ")
print(continent_list)

# Delete the 6th index
del continent_list[5]
print()
print("Updated Continent List After Deleting 6th: ")
print(continent_list)

# Print the last index
print()
print("Last Continent is: ")
print(continent_list[-1])