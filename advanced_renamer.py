import os
import re
import csv
import shutil
import pandas as pd

# Function to sanitize the post description by removing URLs
def sanitize_description(description):
    # Improved regular expression pattern to match various URL formats
    url_pattern = r'(https?://\S+|www\.\S+|\S+\.\S+\.\S+)'
    sanitized_description = re.sub(url_pattern, '', description)
    return sanitized_description.strip()

# Function to convert description to a file-friendly name
def description_to_filename(description):
    # Keep only alphanumeric characters and underscores, truncate to 50 characters
    filename = re.sub(r'\W+', '_', description)
    return filename[:50]

# Function to rank the files based on likes
def create_grading_system(data):
    # Check if the 'Likes' column exists
    if 'Likes' not in data[0]:
        raise KeyError("The CSV file is missing the 'Likes' column. Please check the column name.")

    data_sorted = sorted(data, key=lambda x: int(x['Likes']), reverse=True)
    for index, row in enumerate(data_sorted, start=1):
        row['Grade'] = len(data_sorted) - index + 1
    return data_sorted

# Function to generate the Excel report
def generate_excel_report(output_data, output_file):
    df = pd.DataFrame(output_data)
    df.to_excel(output_file, index=False)
    print(f"Excel report saved to {output_file}")

# Main function to process the media files and rename them
def rename_media_files(media_folder, csv_file, output_excel):
    # Read the CSV file
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        media_data = list(reader)

    # Check for required columns
    required_columns = ['Filename', 'Post Description', 'Likes']
    missing_columns = [col for col in required_columns if col not in media_data[0]]

    if missing_columns:
        raise KeyError(f"The following required columns are missing in the CSV: {', '.join(missing_columns)}")

    # Sanitize descriptions and create grading system
    for row in media_data:
        row['Sanitized Description'] = sanitize_description(row['Post Description'])
    graded_data = create_grading_system(media_data)

    # Prepare output data for Excel report
    output_data = []

    # Process each file
    for row in graded_data:
        original_filename = row['Filename']
        sanitized_description = row['Sanitized Description']
        grade = row['Grade']

        # Create a new file name using the sanitized description and grade
        new_filename_base = description_to_filename(sanitized_description)
        file_extension = os.path.splitext(original_filename)[1]
        new_filename = f"{new_filename_base}_{grade}{file_extension}"

        # Check if the file exists in the media folder
        original_filepath = os.path.join(media_folder, original_filename)
        new_filepath = os.path.join(media_folder, new_filename)

        # Rename the file
        if os.path.exists(original_filepath):
            shutil.move(original_filepath, new_filepath)
            print(f"Renamed: {original_filename} -> {new_filename}")

            # Append to output data for Excel report
            output_data.append({
                'Old Filename': original_filename,
                'New Filename': new_filename,
                'Description': row['Post Description'],
                'Comments': row['Comments'],
                'Shares': row['Shares'],
                'Likes': row['Likes']
            })
        else:
            print(f"File not found: {original_filename}")

    # Generate Excel report
    generate_excel_report(output_data, output_excel)

if __name__ == "__main__":
    # Ask the user for the folder containing the media files and CSV
    media_folder = input("Please enter the path to the folder containing the media files: ").strip()
    csv_file_name = input("Please enter the CSV file name (including .csv extension): ").strip()

    # Define the paths based on user input
    csv_file = os.path.join(media_folder, csv_file_name)  # Path to the user-specified CSV file
    output_excel = os.path.join(media_folder, 'media_report.xlsx')  # Output Excel file

    # Check if the folder and CSV file exist
    if not os.path.isdir(media_folder):
        print(f"Error: The folder '{media_folder}' does not exist.")
    elif not os.path.isfile(csv_file):
        print(f"Error: The CSV file '{csv_file_name}' was not found in '{media_folder}'.")
    else:
        # Proceed with renaming media files and generating the Excel report
        rename_media_files(media_folder, csv_file, output_excel)
