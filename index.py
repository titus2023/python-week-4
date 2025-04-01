def modify_file():
    try:
        filename = input("Enter the filename to read: ")  # User provides the filename
        with open(filename, "r") as file:
            content = file.read()  # Read the file
        
        modified_content = content.upper()  # Example modification (convert to uppercase)

        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)  # Write modified content

        print(f"File successfully modified and saved as {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You do not have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
modify_file()
