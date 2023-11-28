import argparse
import glob
import json
import multiprocessing
import os
from collections import Counter
from multiprocessing import Pool


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
    """
    Compare error codes between two files and find common error codes.

    Loads JSON data from the source and target paths, extracts error codes from both files,
    and finds common error codes between the source and target.

    Args:
        source_path (str): Path to the source JSON file.
        target_path (str): Path to the target JSON file.

    Returns:
        list: A list of common error codes found between the source and target files.
    """
    source_data = load_json(source_path)
    target_data = load_json(target_path)

    # Extract filename (key) from the source path and replace ".json" with ".py"
    source_filename = os.path.splitext(os.path.basename(source_path))[0] + ".py"

    source_errors = source_data.get("./files/" + source_filename, [])
    target_errors = target_data.get("./files_with_feedback/" + source_filename, [])

    common_codes = compare_errors(source_errors, target_errors)

    return common_codes


@staticmethod
def get_common_codes(file_pair):
    source_path, target_path = file_pair
    if os.path.exists(target_path):
        return compare_files(source_path, target_path)
    return []


def analyze_feedback(source_directory, target_directory):
    """
    Analyze feedback between source and target directories for common error codes.

    Compares error codes between files in the source and target directories, finding
    common error codes and generating a table of frequencies for all error codes.

    Args:
        source_directory (str): Path to the source directory containing JSON files.
        target_directory (str): Path to the target directory containing JSON files.

    Prints:
        Table of Frequencies: Prints a table displaying error codes and their frequencies.
    """
    all_common_codes = []
    file_pairs = []

    for filename in os.listdir(source_directory):
        if filename.endswith(".json"):
            source_path = os.path.join(source_directory, filename)
            target_path = os.path.join(target_directory, filename)
            file_pairs.append((source_path, target_path))

    with Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(get_common_codes, file_pairs)
        for common_codes in results:
            all_common_codes.extend(common_codes)

    # Retrieve all files ending with '.json' in the source_directory
    json_files = glob.glob(os.path.join(source_directory, "*.json"))

    # Include codes with frequency 0 for those that have not repeated
    all_codes = [
        entry["code"]
        for json_file in json_files
        for entry in load_json(json_file).get(
            "./files/" + os.path.splitext(json_file)[0] + ".py", []
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


def main():
    """
    Finds repitions in error codes in JSON files contained in source and target directories
    on a per file basis and counted across files
    """
    parser = argparse.ArgumentParser(
        description="Compare error codes in JSON files for a specific file."
    )
    parser.add_argument("source_directory", help="Path to the source directory")
    parser.add_argument("target_directory", help="Path to the target directory")
    args = parser.parse_args()

    source_directory = args.source_directory
    target_directory = args.target_directory

    analyze_feedback(source_directory, target_directory)


if __name__ == "__main__":
    main()
