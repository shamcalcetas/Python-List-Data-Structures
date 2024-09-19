# currency_list.py

# List of 10 world currencies
currency_list = [
                  "South Korean Won", "Thai Baht", "Singapore Dollar", "Chinese Yuan", "Philippine Peso",
                  "United States Dollar", "Australian Dollar", "Japanese Yen", "Hong Kong Dollar", "Canadian Dollar"
                ]

# Print the entire list
print("10 World Currency List: ")
print(currency_list)

# Access and print the 4th index
print()
print("4th World Currency is: ")
print(currency_list[3])

# Update the 7th index to "Euro"
currency_list[6] = "Euro"
print()
print("Updated 7th World Currency: ")
print(currency_list)

# Delete the 9th index
del currency_list[8]
print()
print("Updated World Currency List After Deleting 9th: ")
print(currency_list)

# Print the last index
print()
print("Last World Currency is: ")
print(currency_list[-1])