# student_name_list.py

# List of of 20 student names
student_name_list = [
                  "Ruel", "Ram", "Kyan", "Josh", "Ash", 
                  "Les", "Mhar", "Tine", "Chris", "Paul",
                  "Sham", "Thea", "Camy", "Carol", "Mel",
                  "Riza", "Lyn", "Cess", "Mae", "Dara"
                ]

# Print the entire list
print("20 Student List: ")
print(student_name_list)

# Access and print the 15th index
print()
print("15th Student is: ")
print(student_name_list[14])

# Update the 12th index to "John"
student_name_list[11] = "John"
print()
print("Updated 12th Student: ")
print(student_name_list)

# Delete the 10th index
del student_name_list[9]
print()
print("Updated Student List After Deleting 10th: ")
print(student_name_list)

# Slice the list from index 2 to 5 and print the sliced portion
print()
print("Sliced Portion from 2 to 5:")
print(student_name_list[2:6])

# Print the last index of the list
print()
print("Last Student is: ")
print(student_name_list[-1])