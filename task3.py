# copyfile.py

def main():
    # Prompt the user for input and output file names
    input_file_name = input("Enter the name of the input text file: ")
    output_file_name = input("Enter the name of the output text file: ")

    try:
        # Open the input file for reading
        with open(input_file_name, 'r') as input_file:
            # Read the contents of the input file
            file_contents = input_file.read()

        # Open the output file for writing
        with open(output_file_name, 'w') as output_file:
            # Write the contents to the output file
            output_file.write(file_contents)

        print(f"Contents copied from '{input_file_name}' to '{output_file_name}' successfully.")

    except FileNotFoundError:
        print("Error: One or both of the files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
