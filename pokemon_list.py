# pokemon_list.py

# List of 15 Pokémon names
pokemon_list = [
                  "Bulbasaur", "Charmander", "Squirtle", "Wasp", "Pangolin",
                  "Foxfire", "Sprout", "Vamp", "Pinky Rat", "Water Lizard",
                  "Curlypuff", "Snakey", "Woodpecker", "Sonic", "Sleepbulb"
                ]

# Print the entire list
print("15 Pokemon List: ")
print(pokemon_list)

# Access and print the 9th index
print()
print("9th Pokemon is: ")
print(pokemon_list[8])

# Update the 12th index to "Pikachu"
pokemon_list[11] = "Pikachu"
print()
print("Updated 12th Pokemon: ")
print(pokemon_list)

# Delete the 10th index
del pokemon_list[9]
print()
print("Updated Pokemon List After Deleting 10th: ")
print(pokemon_list)

# Slice the list from index 4 to 7
print()
print("Sliced Portion from 4 to 7:")
print(pokemon_list[4:8])

# Print the last index
print()
print("Last Pokemon is: ")
print(pokemon_list[-1])