# language_spoken_list.py

# List of 20 languages spoken around the world
language_spoken_list = [
                          "Korean", "Filipino", "Japanese", "Chinese", "Turkish",
                          "English", "German", "Vietnamese", "Arabic", "French",
                          "Taiwanese", "Russian", "Bengali", "Urdu", "Hindi",
                          "Tamil", "Telugu", "Marathi", "Indonesian", "Portuguese"
                      ]

# Print the entire list
print("20 Language Spoken List: ")
print(language_spoken_list)

# Access and print the 13th index
print()
print("13th Language Spoken is: ")
print(language_spoken_list[12])

# Update the 10th index to "Spanish"
language_spoken_list[9] = "Spanish"
print()
print("Updated 10th Language Spoken: ")
print(language_spoken_list)

# Delete the 16th index
del language_spoken_list[15]
print()
print("Updated Language Spoken List After Deleting 16th: ")
print(language_spoken_list)

# Slice the list from index 6 to 11
print()
print("Sliced Portion from 6 to 11:")
print(language_spoken_list[6:12])

# Print the last index
print()
print("Last Language Spoken is: ")
print(language_spoken_list[-1])