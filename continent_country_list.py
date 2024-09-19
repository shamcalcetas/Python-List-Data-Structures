# continent_country_list.py

# List of 15 countries and the continents they belong to
continent_country_list = [
                            "Africa : Nigeria", "Africa : Kenya", "Asia: Philippines", "Asia: Japan", "Asia : Korea",
                            "Europe : Finland", "Europe : Italy", "Europe : France", "North America : Mexico", "North America : Jamaica",
                            "South America : Brazil", "South America : Argentina", "Oceania : Fiji", "Oceania : New Zealand", "Oceania : Palau", 
                        ]

# Print the entire list
print("15 Continents and Their Countries List: ")
print(continent_country_list)

# Access and print the 9th index
print()
print("9th Continent and Its Country is: ")
print(continent_country_list[8])

# Update the 10th index to "Australia"
continent_country_list[9] = "Australia"
print()
print("Updated 10th Continent and Its Country: ")
print(continent_country_list)

# Delete the 12th index
del continent_country_list[11]
print()
print("Updated Continents and Their Countries List After Deleting 12th: ")
print(continent_country_list)

# Slice the list from index 5 to 10
print()
print("Sliced Portion from 4 to 8:")
print(continent_country_list[4:9])

# Print the last index
print()
print("Last Continent and Its Country is: ")
print(continent_country_list[-1])