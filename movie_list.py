# movie_list.py

# List of 20 movie titles
movie_list = [
                "Pilot", "Roundup", "Platform", "Exit", "Parasyte",
                "V.I.P", "Rampage", "Escape", "Cube", "Maze",
                "Psychokinesis", "Blind", "Chasing", "Parasite", "Believer",
                "Forgotten", "Ashfall", "Hitman", "Start Up", "The Witch"
            ]

# Print the entire list
print("20 Movie List: ")
print(movie_list)

# Access and print the 12th index
print()
print("12th Movie is: ")
print(movie_list[11])

# Update the 15th index to "Inception"
movie_list[14] = "Inception"
print()
print("Updated 15th Movie: ")
print(movie_list)

# Delete the 18th index
del movie_list[17]
print()
print("Updated Movie List After Deleting 18th: ")
print(movie_list)

# Slice the list from index 8 to 13
print()
print("Sliced Portion from 8 to 13:")
print(movie_list[8:14])

# Print the last index
print()
print("Last Movie is: ")
print(movie_list[-1])