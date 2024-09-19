# language_list.py

# List of 14 programming languages
language_list = [
                  "C", "C++", "C#", "Go", "HTML",
                  "Java", "JavaScript", "PHP", "Scala", "R",
                  "Ruby", "Rust", "SQL", "Swift"
                ]

# Print the entire list
print("14 Programming Language List: ")
print(language_list)

# Access and print the 11th index
print()
print("11th Programming Language is: ")
print(language_list[10])

# Update the 9th index to "Python"
language_list[8] = "Python"
print()
print("Updated 9th Programming Language: ")
print(language_list)

# Delete the 13th index
del language_list[12]
print()
print("Updated Programming Language List After Deleting 13th: ")
print(language_list)

# Slice the list from index 5 to 12
print()
print("Sliced Portion from 5 to 12:")
print(language_list[5:13])

# Print the last index
print()
print("Last Programming Language is: ")
print(language_list[-1])