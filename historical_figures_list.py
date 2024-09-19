# historical_figures_list.py

# List of 10 historical figures
historical_figures_list = [
                            "Martin Luther King Jr.", "George Washington", "William Shakespeare", 
                            "Julius Caesar", "Alexander the Great", "Charles Darwin", 
                            "Isaac Newton", "Leonardo da Vinci", "Adolf Hitler", "Abraham Lincoln"
                          ]

# Print the entire list
print("10 Historial Figure List: ")
print(historical_figures_list)

# Access and print the 8th index
print()
print("8th Historial Figure is: ")
print(historical_figures_list[7])

# Update the 4th index to "Nelson Mandela"
historical_figures_list[3] = "Nelson Mandela"
print()
print("Updated 4th Historial Figure: ")
print(historical_figures_list)

# Delete the 7th index
del historical_figures_list[6]
print()
print("Updated Historial Figure List After Deleting 7th: ")
print(historical_figures_list)

# Print the last index
print()
print("Last Historial Figure is: ")
print(historical_figures_list[-1])