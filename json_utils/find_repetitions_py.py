"""
Finds repitions in error codes in JSON files contained in source and target directories
on a per file basis and counted across files
"""

import json
import os
import argparse
from collections import Counter


def load_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def compare_errors(source_errors, target_errors):
    # Extract error codes from each file
    source_codes = [entry["code"] for entry in source_errors]
    target_codes = [entry["code"] for entry in target_errors]

    # Find common error codes
    common_codes = set(source_codes).intersection(target_codes)

    return common_codes


def compare_files(source_path, target_path):
    source_data = load_json(source_path)
    target_data = load_json(target_path)

    # Extract filename (key) from the source path and replace ".json" with ".py"
    source_filename = os.path.splitext(os.path.basename(source_path))[0] + ".py"

    source_errors = source_data.get("./files/" + source_filename, [])
    target_errors = target_data.get("./files_with_feedback/" + source_filename, [])

    common_codes = compare_errors(source_errors, target_errors)

    return common_codes


def main():
    parser = argparse.ArgumentParser(
        description="Compare error codes in JSON files for a specific file."
    )
    parser.add_argument("source_directory", help="Path to the source directory")
    parser.add_argument("target_directory", help="Path to the target directory")
    args = parser.parse_args()

    source_directory = args.source_directory
    target_directory = args.target_directory

    all_common_codes = []

    for filename in os.listdir(source_directory):
        if filename.endswith(".json"):
            source_path = os.path.join(source_directory, filename)
            target_path = os.path.join(target_directory, filename)

            if os.path.exists(target_path):
                common_codes = compare_files(source_path, target_path)
                all_common_codes.extend(common_codes)

    # Include codes with frequency 0 for those that have not repeated
    all_codes = [
        entry["code"]
        for filename in os.listdir(source_directory)
        if filename.endswith(".json")
        for entry in load_json(os.path.join(source_directory, filename)).get(
            "./files/" + os.path.splitext(filename)[0] + ".py", []
        )
    ]

    for code in set(all_codes):
        if code not in all_common_codes:
            all_common_codes.append(code)

    # Table of frequencies for all error codes
    error_frequencies = Counter(all_common_codes)
    # Sort items by frequency in descending order
    error_frequencies = sorted(error_frequencies.items(), key=lambda x: x[1], reverse=True)

    print("\nTable of Frequencies:")
    print("{:<10} {:<10}".format("Error Code", "Frequency"))
    print("-" * 20)
    for code, frequency in error_frequencies:
        print("{:<10} {:<10}".format(code, frequency))


if __name__ == "__main__":
    main()
