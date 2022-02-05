# Import the module os that provides tools to work with the operating system of your computer.
import os

# Ask a user for the input file name.
file_name = input("Please write the name of the file to work with:\n")

# If the path that a user has entered exists, do the following steps:
if os.path.exists(file_name):
    with open(file_name) as file:
        # Open the file in the reading mode, read its content.
        content = file.read()
    # Apply the previously defined function process() to the text taken from the file.
    new_content = process(content)

    # Open for writing a new file with a slightly changed name, write the processed text there.
    with open(f'{file_name}_processed.txt', 'w') as new_file:
        new_file.write(new_content)

    # Print that everything is done.
    print("All done!")

else:
    # If the path entered by a user doesn't exist, print the corresponding message.
    print("The file you entered does not exist!")