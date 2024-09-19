# planet_list.py

# List of 8 planet names
planet_list = [
                "Mercury", "Venus", "Earth", "Mars",
                "Jupiter", "Saturn", "Uranus", "Neptune"
            ]

# Print the entire list
print("8 Planet List: ")
print(planet_list)

# Access and print the 3rd index
print()
print("3rd Planet is: ")
print(planet_list[2])

# Update the 7th index to "Pluto"
planet_list[6] = "Pluto"
print()
print("Updated 7th Planet: ")
print(planet_list)

# Delete the 4th index
del planet_list[3]
print()
print("Updated Planet List After Deleting 4th: ")
print(planet_list)

# Print the last index
print()
print("Last Planet is: ")
print(planet_list[-1])