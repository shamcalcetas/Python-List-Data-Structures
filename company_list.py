# company_list.py

# List of 10 company names
company_list = [
                  "Amazon", "Nike", "Starbucks", "Sony", "BMW",
                  "Adidas", "Coca-Cola", "Microsoft", "Google", "Mercedes-Benz"
                ]

# Print the entire list
print("10 Company List: ")
print(company_list)

# Access and print the 7th index
print()
print("7th Company is: ")
print(company_list[6])

# Update the 5th index to "Apple"
company_list[4] = "Apple"
print()
print("Updated 5th Company: ")
print(company_list)

# Delete the 8th index
del company_list[7]
print()
print("Updated Company List After Deleting 8th: ")
print(company_list)

# Print the last index
print()
print("Last Company is: ")
print(company_list[-1])