# Text File Combiner

This Python script is designed to combine the contents of all `.txt` files within a specified folder into a single file. It is useful for aggregating text data that is distributed across multiple files into a single document for easier processing or analysis.

## How It Works

The script scans a specified folder for `.txt` files. It reads the contents of each file and appends it to a single string with a newline character separating the contents of each file. Finally, it writes the combined contents to a specified output file.

## Prerequisites

- Python 3.x
- Access to a command-line interface (CLI) or integrated development environment (IDE) where you can run Python scripts.
- Text files in `.txt` format stored in a specific folder.

## Setup

1. **Prepare Your Files:**
   Ensure that all the `.txt` files you want to combine are located within the same folder.

2. **Folder Path Configuration:**
   - Open the script with a text editor or IDE.
   - Modify the `folder_path` variable to the path of the folder containing your `.txt` files.
   Example:
   ```python
   folder_path = 'path_to_your_folder'
   ```

3. **Output File Configuration:**
   Define the name and path of the output file by modifying the `combined_file_path` variable.
   Example:
   ```python
   combined_file_path = 'desired_output_file_path'
   ```

## Usage

To use the script, follow these steps:

1. Navigate to the directory where your script is located using the command line or terminal.
2. Run the script using Python:
   ```bash
   python combine_text_files.py
   ```
3. Check the output directory for the `combined.txt` file which will contain the combined contents of all the `.txt` files from the specified folder.

## Example

Suppose you have a folder named `documents` containing `file1.txt`, `file2.txt`, and `file3.txt`. You can set `folder_path = 'documents'` and `combined_file_path = 'combined_output.txt'`. Running the script will create a `combined_output.txt` with the contents of all three files.

## Note

- The script assumes that the `.txt` files are encoded in a format readable by Python's default settings (typically UTF-8).
- If files are very large, consider modifying the script to handle file reading and writing in chunks to avoid memory issues.
