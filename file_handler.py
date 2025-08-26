import os

def file_processor():
    """
    Asks for a filename, reads it, adds line numbers, and writes to a new file.
    Includes robust error handling for common file-related issues.
    """
    print("--File read, modify and write program")

    # Ask the user for a file name
    input_file_name = input("Enter the name of the file to read (e.g., 'input.txt'): ").strip()

    # File processing and error handling
    try:
        # Perform all the operations within this 'try' block
        with open(input_file_name, 'r') as file_input:
            print(f"\nReading content from '{input_file_name}'...")
            # .readlines reads the entire file and returns a list of strings
            lines = file_input.readlines()

        # check if the file is empty 
        if not lines:
            print(f"Warning! The file '{input_file_name}' is empty")

        # Write modified version to a new file
        # Create new filename for the output to avoid overwriting the original
        name, ext = os.path.splitext(input_file_name)
        output_file_name = f"{name}_modified{ext}"

        with open(output_file_name, 'w') as file_output:
            # enumerate returns an index(line number) and the value of the list
            # from 1 to make human-readable line numbers
            for line_number, line in enumerate(lines, start=1):
                # Modify the line by prepending the line number.
                # The line already contains a newline character at the end.
                modified_line = f"{line_number}: {line}"
                file_output.write(modified_line) 

        # --Success message
        print("\n Success printing new line complete")
        print(f"Modified content has been written to {output_file_name}")

    except FileNotFoundError:
        # --Specific file error when file does not exist
        print(f"\n❌ ERROR: The file '{input_file_name}' was not found.")
        print("Please check the spelling and make sure the file is in the same directory as the script.")

    except PermissionError:
        # --Specific file error when file is not readable
        print(f"\n❌ ERROR: You do not have permission to read the file '{input_file_name}'.")
        print("Please check the file permissions and try again.")

    except Exception as e:
        # --General error handling
        print(f"\n❌ ERROR: An unexpected error occurred: {e}")
        print("Please check the file name and try again.")


# This line ensures that the function runs only when the script is executed directly
if __name__ == "__main__":
    file_processor()


