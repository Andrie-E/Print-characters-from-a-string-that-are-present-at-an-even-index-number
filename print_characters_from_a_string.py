# Write a program to accept a string from the user and display characters that are present at an even index number.

# Pseudocode
# Create an input code for the users to add a word
Users_input = input("Please write your word here:")
# Display the users word
print ("Original String is,", Users_input)
print("Printing only even index chars")
# Display characters at even index numbers
for i in range(0, len(Users_input), 2):

# Print the result
    print(Users_input[i])