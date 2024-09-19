# flower_list.py

# List of 10 flower names
flower_list = [
                "Dahlia", "Hyacinth", "Daisy", "Sunflower", "Marigold",
                "Carnation", "Lily", "Cornflower", "Chrysanthemum", "Orchid",
              ]

# Print the entire list
print("10 Flower List: ")
print(flower_list)

# Access and print the 5th index
print()
print("5th Flower is: ")
print(flower_list[4])

# Update the 8th index to "Rose"
flower_list[7] = "Rose"
print()
print("Updated 8th Flower: ")
print(flower_list)

# Delete the 2ndh index
del flower_list[1]
print()
print("Updated Flower List After Deleting 2nd: ")
print(flower_list)

# Print the last index
print()
print("Last Flower is: ")
print(flower_list[-1])