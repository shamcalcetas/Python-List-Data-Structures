# job_titles_list.py

# List of 10 job titles
job_titles_list = [
                    "Administrative Assistant", "Executive Assistant", "Marketing Manager", "Customer Service Representative", 
                    "Nurse Practitioner", "Entrepreneur", "Sales Manager", "Data Entry Clerk", "Office Assistant", "Translator"
                  ]

# Print the entire list
print("10 Job Title List: ")
print(job_titles_list)

# Access and print the 6th index
print()
print("6th Job Title is: ")
print(job_titles_list[5])

# Update the 5th index to "Software Engineer"
job_titles_list[4] = "Software Engineer"
print()
print("Updated 5th Job Title: ")
print(job_titles_list)

# Delete the 9th index
del job_titles_list[8]
print()
print("Updated Job Title List After Deleting 9th: ")
print(job_titles_list)

# Print the last index
print()
print("Last Job Title is: ")
print(job_titles_list[-1])