import os

# Folder path where your .txt files are stored
folder_path = 'txt_files2'  # The folder is on the same level as the script
combined_file_path = 'combined.txt'  # Output file

# Initialize an empty string to store the combined contents of all text files
combined_contents = ''

# Walk through the folder
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith('.txt'):  # Check if the file is a .txt file
            file_path = os.path.join(root, filename)
            with open(file_path, 'r') as file:  
                combined_contents += file.read() + '\n'  # Read contents and add a newline

# Write all the combined contents to one file
with open(combined_file_path, 'w') as output_file:
    output_file.write(combined_contents)

print("All text files have been combined into 'combined.txt'.")
