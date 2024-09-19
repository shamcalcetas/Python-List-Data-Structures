# music_genre_list.py

# List of 15 music genres
music_genre_list = [
                      "Pop", "Rock", "Popular", "Electronic", "Rhythm and Blues",
                      "Country", "Hip Hop", "Classical", "Heavy Metal", "Folk",
                      "Dance Music", "World Music", "Alternative Rock", "Soul Music", "New-age"
                  ]

# Print the entire list
print("15 Music Genre List: ")
print(music_genre_list)

# Access and print the 10th index
print()
print("10th Music Genre is: ")
print(music_genre_list[9])

# Update the 5th index to "Jazz"
music_genre_list[4] = "Jazz"
print()
print("Updated 5th Music Genre: ")
print(music_genre_list)

# Delete the 7th index
del music_genre_list[6]
print()
print("Updated Music Genre List After Deleting 7th: ")
print(music_genre_list)

# Slice the list from index 3 to 8
print()
print("Sliced Portion from 3 to 8:")
print(music_genre_list[3:9])

# Print the last index
print()
print("Last Music Genre is: ")
print(music_genre_list[-1])