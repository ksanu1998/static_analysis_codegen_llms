#!/bin/bash

# Check if the source and report directories are provided as arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <source_directory> <report_directory>"
    exit 1
fi

# Extract source and report directories from command line arguments
source_directory="$1"
report_directory="$2"

# Check if the source directory exists
if [ ! -d "$source_directory" ]; then
    echo "Source directory does not exist: $source_directory"
    exit 1
fi

# Create the report directory if it doesn't exist
if [ ! -d "$report_directory" ]; then
    mkdir -p "$report_directory"
fi

flake8 --statistics "$source_directory" --q --output-file="$report_directory/flake8_report.txt"