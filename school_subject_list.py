# school_subject_list.py

# List of 12 school subjects
school_subject_list = [
                        "Science", "Social Studies", "Music", "Physical Education", 
                        "Art", "Computer Science", "Geography", "Health Education", 
                        "Chemistry", "Foreign language", "History", "Algebra"
                      ]

# Print the entire list
print("12 School Subject List: ")
print(school_subject_list)

# Access and print the 6th index
print()
print("6th School Subject is: ")
print(school_subject_list[5])

# Update the 8th index to "Mathematics"
school_subject_list[7] = "Mathematics"
print()
print("Updated 8th School Subject: ")
print(school_subject_list)

# Delete the 4th index
del school_subject_list[3]
print()
print("Updated School Subject List After Deleting 4th: ")
print(school_subject_list)

# Slice the list from index 2 to 5
print()
print("Sliced Portion from 2 to 5:")
print(school_subject_list[2:6])

# Print the last index
print()
print("Last School Subject is: ")
print(school_subject_list[-1])