# author_list.py

# List of 12 famous authors
author_list = [
                "Stephen King", "John Grisham", "J. K. Rowling", "Neil Gaiman", "George Saunders",
                "Anthony Horowitz", "Stan Lee", "John Green", "Kazuo Ishiguro", "Colleen Hoover",
                "Stephanie Meyer", "Dean Koontz", "James Patterson", "Emily Henry"
              ]

# Print the entire list
print("12 Author List: ")
print(author_list)

# Access and print the 6th index
print()
print("6th Author is: ")
print(author_list[5])

# Update the 4th index to "Mark Twain"
author_list[3] = "Mark Twain"
print()
print("Updated 4th Author: ")
print(author_list)

# Delete the 10th index
del author_list[9]
print()
print("Updated Author List After Deleting 10th: ")
print(author_list)

# Slice the list from index 3 to 8
print()
print("Sliced Portion from 3 to 8:")
print(author_list[3:9])

# Print the last index
print()
print("Last Author is: ")
print(author_list[-1])