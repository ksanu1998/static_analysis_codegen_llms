import json
import argparse
from collections import Counter

def get_error_ids(json_data, file_key):
    error_ids = set()

    if file_key in json_data and "errors" in json_data[file_key] and "error" in json_data[file_key]["errors"]:
        errors = json_data[file_key]["errors"]["error"]

        # Handle the case where "error" is a list of errors
        if isinstance(errors, list):
            for error in errors:
                error_id = error["attributes"]["id"]
                error_ids.add(error_id)
        else:
            # Handle the case where "error" is a single error
            error_id = errors["attributes"]["id"]
            error_ids.add(error_id)

    return error_ids

def compare_error_ids(file1_data, file2_data):
    common_errors = {}

    for file_key in file1_data.keys():
        file1_error_ids = get_error_ids(file1_data, file_key)
        file2_error_ids = get_error_ids(file2_data, file_key)

        common_error_ids = file1_error_ids.intersection(file2_error_ids)

        if common_error_ids:
            common_errors[file_key] = common_error_ids

    return common_errors

def count_error_frequencies(json_data, common_errors):
    error_frequencies = Counter()

    for file_key, error_ids in common_errors.items():
        for error_id in error_ids:
            for file_data_key, file_data in json_data.items():
                if file_data_key == file_key and "errors" in file_data and "error" in file_data["errors"]:
                    errors = file_data["errors"]["error"]

                    # Handle the case where "error" is a list of errors
                    if isinstance(errors, list):
                        for error in errors:
                            if error["attributes"]["id"] == error_id:
                                error_frequencies[error_id] += 1
                                break
                    else:
                        # Handle the case where "error" is a single error
                        if errors["attributes"]["id"] == error_id:
                            error_frequencies[error_id] += 1

    return error_frequencies

def main():
    parser = argparse.ArgumentParser(description='Compare JSON files and find common errors on a per-key basis.')
    parser.add_argument('file1', help='Path to the first JSON file')
    parser.add_argument('file2', help='Path to the second JSON file')

    args = parser.parse_args()

    with open(args.file1) as file1:
        file1_data = json.load(file1)

    with open(args.file2) as file2:
        file2_data = json.load(file2)

    common_errors = compare_error_ids(file1_data, file2_data)

    if common_errors:
        # Print the list of common error IDs on a per-key basis
        print("File Key\tCommon Error IDs")
        for file_key, error_ids in common_errors.items():
            print(f"{file_key}\t{', '.join(error_ids)}")

        # Generate and print the frequency table
        error_frequencies = count_error_frequencies(file1_data, common_errors)

        # Sort frequencies in descending order
        sorted_frequencies = sorted(error_frequencies.items(), key=lambda x: x[1], reverse=True)

        # Print the frequency table
        print("\nError ID\tFrequency")
        for error_id, frequency in sorted_frequencies:
            print(f"{error_id}\t{frequency}")
    else:
        print("No common error IDs found.")

if __name__ == "__main__":
    main()
