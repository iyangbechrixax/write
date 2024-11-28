def read_and_write_file():
    import os
    
    # Prompt the user for a filename
    filename = input("Enter the name of the file to read (e.g., 'example.txt'): ").strip()
    
    try:
        # Attempt to open the specified file for reading
        with open(filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content - for this example, convert to uppercase
        modified_content = content.upper()
        
        # Create a new filename for the output
        base, ext = os.path.splitext(filename)
        new_filename = f"{base}_modified{ext}"
        
        # Write the modified content to the new file
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File '{filename}' was successfully read and modified content saved to '{new_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: Permission denied. Cannot read or write to the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_write_file()
