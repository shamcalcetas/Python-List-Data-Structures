# space_missions_list.py

# List of 10 space missions
space_missions_list = [
                        "Project Gemini", "Mars Express", "Parker Solar Probe", "Pioneer 10", "Project Mercury",
                        "Solar Dynamics Observatory", "Cassini-Huygens", "Hubble Space Telescope", "Lunar Flashlight", "Voyager 1"
                    ]

# Print the entire list
print("10 Space Mission List: ")
print(space_missions_list)

# Access and print the 7th index
print()
print("7th Space Mission is: ")
print(space_missions_list[6])

# Update the 4th index to "Apollo 11"
space_missions_list[3] = "Apollo 11"
print()
print("Updated 4th Space Mission: ")
print(space_missions_list)

# Delete the 6th index
del space_missions_list[5]
print()
print("Updated Space Mission List After Deleting 6th: ")
print(space_missions_list)

# Print the last index
print()
print("Last Space Mission is: ")
print(space_missions_list[-1])