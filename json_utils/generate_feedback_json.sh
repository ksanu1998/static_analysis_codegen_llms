#!/bin/bash

# Set the fixed report_directory
report_directory="xml_files"

# Check if the source directory is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <source_directory>"
    exit 1
fi

# Extract source directory from command line arguments
source_directory="$1"

# Check if the source directory exists
if [ ! -d "$source_directory" ]; then
    echo "Source directory does not exist: $source_directory"
    exit 1
fi

# Create the report directory if it doesn't exist
if [ ! -d "$report_directory" ]; then
    mkdir -p "$report_directory"
fi

# Iterate over each file in the source directory
for file in "$source_directory"/*; do
    # Check if the item is a file
    if [ -f "$file" ]; then
        # Extract the filename without extension
        filename=$(basename -- "$file")
        filename_no_ext="${filename%.*}"

        # Run cppcheck for the current file
        cppcheck/build/bin/cppcheck --enable=all --suppress=missingIncludeSystem --check-level=exhaustive --xml "$file" 2> "$report_directory/${filename_no_ext}_error_file.xml"
    fi
done

# Run xml_to_json.py
python3 "$(dirname "$0")/xml_to_json.py" "$report_directory" "feedback.json"

# Remove $report_directory
rm -r "$report_directory"