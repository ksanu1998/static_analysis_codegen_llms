import json
import argparse
from collections import Counter


def get_error_ids(json_data, file_key):
    """
    Extracts error IDs from the provided JSON data for a specific file key.

    Args:
        json_data (dict): JSON data containing error information for different files.
        file_key (str): Key representing a specific file in the JSON data.

    Returns:
        set: A set containing error IDs extracted from the specified file key.
    """
    error_ids = set()

    if (
        file_key in json_data
        and "errors" in json_data[file_key]
        and "error" in json_data[file_key]["errors"]
    ):
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
    """
    Compares error IDs between two sets of JSON data and finds common error IDs per file key.

    Args:
        file1_data (dict): First set of JSON data containing error information for different files.
        file2_data (dict): Second set of JSON data containing error information for different files.

    Returns:
        dict: A dictionary mapping file keys to sets of common error IDs between the two sets of
        data.
    """
    common_errors = {}

    for file_key in file1_data.keys():
        file1_error_ids = get_error_ids(file1_data, file_key)
        file2_error_ids = get_error_ids(file2_data, file_key)

        common_error_ids = file1_error_ids.intersection(file2_error_ids)

        if common_error_ids:
            common_errors[file_key] = common_error_ids

    return common_errors


def count_error_frequencies(json_data, common_errors):
    """
    Count the frequencies of common error IDs within JSON data.

    This function iterates through the JSON data, identifies common error IDs present in the
    provided `common_errors` dictionary, and counts their frequencies across different files.

    Args:
        json_data (dict): JSON data containing error information in different files.
        common_errors (dict): Dictionary containing common error IDs for different files.

    Returns:
        Counter: A Counter object containing the frequencies of common error IDs.
    """
    error_frequencies = Counter()

    for file_key, error_ids in common_errors.items():
        for error_id in error_ids:
            for file_data_key, file_data in json_data.items():
                if (
                    file_data_key == file_key
                    and "errors" in file_data
                    and "error" in file_data["errors"]
                ):
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


def load_json_file(file_path):
    with open(file_path) as file:
        return json.load(file)


def analyze_error_data(file1_path, file2_path):
    """
    Analyzes error data between two JSON files.

    Loads JSON data from the provided file paths, compares error IDs between the files, and
    generates a list of common error IDs per file key. Additionally, it computes the frequency
    table for common error IDs and prints both the common error IDs per key and the error
    frequencies.

    Args:
        file1_path (str): Path to the first JSON file.
        file2_path (str): Path to the second JSON file.

    Returns:
        tuple: A tuple containing two elements:

            - A dictionary mapping file keys to sets of common error IDs between the two files.
            - A list of tuples containing error IDs and their frequencies sorted in descending
            order.
            Returns None for both elements if no common error IDs are found.
    """
    file1_data = load_json_file(file1_path)
    file2_data = load_json_file(file2_path)

    common_errors = compare_error_ids(file1_data, file2_data)
    sorted_frequencies = None

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

    return common_errors, sorted_frequencies


def main():
    parser = argparse.ArgumentParser(
        description="Compare JSON files and find common errors on a per-key basis."
    )
    parser.add_argument("file1", help="Path to the first JSON file")
    parser.add_argument("file2", help="Path to the second JSON file")
    args = parser.parse_args()

    analyze_error_data(args.file1, args.file2)


if __name__ == "__main__":
    main()
