# land_animal_speed_list.py

# List of 12 land animals and their speeds
land_animal_speed_list = [
                            "Pronghorn Antelope - 89 km/h ", "Springbok - 89 km/h", "Wildebeest - 80 km/h", "Lion - 80 km/h", 
                            "Blackbuck - 80 km/h", "American Quarter Horse - 76.5 km/h", "Brown Hare - 72 km/h", "Greyhound - 69 km/h", 
                            "Kangaroo - 71 km/h", "Coyote - 69 km/h", "African Wild Dog - 68 km/h", "Jackal - 64 km/h" 
                        ]

# Print the entire list
print("12 Animals and Their Speed List: ")
print(land_animal_speed_list)

# Access and print the 7th index
print()
print("7th Animal and Its Speed is: ")
print(land_animal_speed_list[6])

# Update the 9th index to "Cheetah - 120 km/h"
land_animal_speed_list[8] = "Cheetah - 120 km/h"
print()
print("Updated 9th Animal and Its Speed: ")
print(land_animal_speed_list)

# Delete the 10th index
del land_animal_speed_list[9]
print()
print("Updated Animals and Their Speed List After Deleting 10th: ")
print(land_animal_speed_list)

# Slice the list from index 3 to 7
print()
print("Sliced Portion from 3 to 7:")
print(land_animal_speed_list[3:8])

# Print the last index
print()
print("Last Animal and Its Speed is: ")
print(land_animal_speed_list[-1])