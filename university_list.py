# university_list.py

# List of 10 universities
university_list = [
                    "Massachusetts Institute of Technology", "Stanford University", "University of Oxford", 
                    "University of California Berkeley", "University of Cambridge", "University College London",
                    "University of Washington Seattle", "Columbia University", "Yale University", "University of Toronto"
                  ]

# Print the entire list
print("10 University List: ")
print(university_list)

# Access and print the 6th index
print()
print("6th University is: ")
print(university_list[5])

# Update the 4th index to "Harvard University"
university_list[3] = "Harvard University"
print()
print("Updated 4th University: ")
print(university_list)

# Delete the 9th index
del university_list[8]
print()
print("Updated University List After Deleting 9th: ")
print(university_list)

# Print the last index
print()
print("Last University is: ")
print(university_list[-1])