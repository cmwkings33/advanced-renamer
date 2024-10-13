# Advanced Renamer from CSV

This Python script processes media files (images and videos) in a folder, renaming them based on a CSV file that includes information like descriptions, comments, shares, and likes. The script sanitizes post descriptions by removing URLs, generates an Excel report, and renames the files based on their popularity (i.e., the number of likes). 

## Features
- **URL Removal**: Automatically sanitizes post descriptions by removing all URLs.
- **File Renaming**: Renames the media files based on the sanitized post description, with underscores separating words.
- **Grading System**: Assigns a grade (1 to N, where N is the highest number of likes) to each file based on the number of likes.
- **Excel Report Generation**: Outputs an Excel file that tracks the old file name, new file name, description, comments, shares, and likes for easy reference and sorting.

## Requirements

The script requires the following Python packages:

- `pandas`: For handling CSV and Excel data.
- `openpyxl`: To allow Excel export functionality.
- `shutil`: For file operations like moving/renaming files.
- `re` and `os`: For regular expression operations and file system navigation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/advanced-renamer.git
   cd advanced-renamer

Install the dependencies:

bash

    pip install -r requirements.txt

## Usage

    Place all the media files (images or videos) you want to process in a folder. Also, ensure the CSV file is in the same folder. The CSV file should have the following columns:
        Filename: The exact name of the media file (e.g., image1.jpg).
        Post Description: The description you want to sanitize and use in the renaming process.
        Comments: The number of comments (this column is optional for renaming but will be included in the Excel report).
        Shares: The number of shares (optional for renaming but will be included in the Excel report).
        Likes: The number of likes, which determines the grading system for renaming.

    Run the script:

    bash

    python advanced_renamer.py

    The script will prompt you for:
        The folder path where the media files and CSV are located.
        The name of the CSV file (including the .csv extension).

    After processing, the script will:
        Rename the media files based on the sanitized post descriptions and their grade.
        Generate an Excel report (media_report.xlsx) containing the old and new filenames, the description, and the metadata (comments, shares, and likes).

## Example

CSV Example:

csv

Filename,Post Description,Comments,Shares,Likes
image1.jpg,Check out our new website at https://example.com!,10,5,100
video2.mp4,Amazing video of the sunset www.sunset.com!,15,8,150

Process Flow:

    Input: The CSV file with media files (image1.jpg, video2.mp4).
    Sanitization: The script removes URLs from the descriptions.
        "Check out our new website at https://example.com!" -> "Check out our new website!"
    Renaming: The files are renamed based on the sanitized description, with underscores replacing spaces and a grade suffix based on likes.
        image1.jpg -> Check_out_our_new_website_1.jpg
        video2.mp4 -> Amazing_video_of_the_sunset_2.mp4
    Excel Report: A report (media_report.xlsx) is generated, detailing the changes and metadata.

Logic Behind Grading System

    The file with the most likes gets the highest grade.
    The file with the least likes gets the lowest grade.
    This grading system is appended to the file name as a numerical suffix (e.g., filename_1.jpg for the file with the least likes and filename_N.jpg for the file with the most likes).

Limitations and Notes

    Ensure that the CSV contains all the required columns (Filename, Post Description, Likes).
    The script will only process files that exist in the media folder.
    URLs are removed using a regular expression that captures various URL formats.
    The filename is limited to 50 characters to avoid overly long filenames.

License

This project is licensed under the MIT License. See the LICENSE file for more details.


Full Directions on Operation Setup and Installation:

    Clone the repository:
    Clone the project repository to your local machine:

    bash

git clone https://github.com/yourusername/advanced-renamer.git

Change into the project directory:

bash

cd advanced-renamer

Install dependencies:
Install the required Python packages using:

bash

    pip install -r requirements.txt

Folder Structure:

    Place all media files and the CSV file in a folder. The CSV file should contain information such as the file names, descriptions, likes, and comments.
    Ensure the column names in your CSV match exactly as outlined in the example (Filename, Post Description, Likes, Comments, Shares).

Running the Script:

    Run the Python script:

    bash

    python advanced_renamer.py

    User Input: The script will prompt for two inputs:
        The path to the folder containing the media files and the CSV.
        The CSV file name (including the .csv extension).

    Processing: The script will:
        Remove URLs from the descriptions.
        Rename the media files using a combination of sanitized descriptions and a grade based on the number of likes.
        Generate an Excel report.

    Output:
        Media files will be renamed in the folder according to the processed rules.
        An Excel report (media_report.xlsx) will be created, detailing the old and new filenames, descriptions, and metadata like comments, shares, and likes.

How the Script Works:

    The sanitization step removes any URLs from the description using a regular expression.
    The renaming step takes the sanitized description, converts it to a valid filename by replacing spaces with underscores, and appends the grade based on likes.
    Files with the highest likes get the highest grade, while files with the least likes get the lowest.
    The generated Excel report helps track all renaming actions and provides a sortable record of your media files and their metadata.