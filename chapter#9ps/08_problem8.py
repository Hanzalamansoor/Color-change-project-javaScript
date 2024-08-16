#Write a program to find out the line number where python is present from ques 6.


# Open the file and read lines
with open("log.txt", "r") as file:
    lines = file.readlines()

# Initialize line number counter
line_number = 1

# Iterate through each line
for line in lines:
    if "python" in line.lower():  # Check if "python" is in the line (case-insensitive)
        print(f"Python word is found in line number: {line_number}")
        break
    line_number += 1
else:
    print("Python word is not found in the text")

