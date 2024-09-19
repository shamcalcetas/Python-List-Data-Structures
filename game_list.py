# game_list.py

# List of 15 video game titles
game_list = [
                "Elden Ring", "Hades", "Disco Elysium", "God of War", "Fortnite",
                "Stardew Valley", "Persona", "Overwatch", "Undertale", "Bloodborne",
                "The Last of Us", "Dota", "	Borderlands", "Portal", "Dark Souls",
            ]

# Print the entire list
print("15 Video Game List: ")
print(game_list)

# Access and print the 7th index
print()
print("7th Video Game is: ")
print(game_list[6])

# Update the 4th index to "Minecraft"
game_list[3] = "Minecraft"
print()
print("Updated 4th Video Game: ")
print(game_list)

# Delete the 9th index
del game_list[8]
print()
print("Updated Video Game List After Deleting 9th: ")
print(game_list)

# Slice the list from index 5 to 10
print()
print("Sliced Portion from 5 to 10:")
print(game_list[5:11])

# Print the last index
print()
print("Last Video Game is: ")
print(game_list[-1])