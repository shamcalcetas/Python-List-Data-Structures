# social_media_list.py

# List of 10 social media platforms
social_media_list = [
                      "Facebook", "Youtube", "Weibo", "Pinterest", "QQ",
                      "Messenger", "Telegram", "WhatsApp", "LinkedIn", "Snapchat"
                    ]

# Print the entire list
print("10 Social Media List: ")
print(social_media_list)

# Access and print the 5th index
print()
print("5th Social Media is: ")
print(social_media_list[4])

# Update the 3rd index to "Instagram"
social_media_list[2] = "Instagram"
print()
print("Updated 3rd Social Media: ")
print(social_media_list)

# Delete the 8th index
del social_media_list[7]
print()
print("Updated Social Media List After Deleting 8th: ")
print(social_media_list)

# Print the last index
print()
print("Last Social Media is: ")
print(social_media_list[-1])