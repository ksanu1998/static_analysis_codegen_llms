import glob
import json
import os
import sys
import xml.etree.ElementTree as ET
from multiprocessing import Pool


def xml_to_dict(element):
    result = {}
    result["tag"] = element.tag
    result["attributes"] = element.attrib
    result["text"] = element.text

    for child in element:
        if child.tag in result:
            if type(result[child.tag]) is list:
                result[child.tag].append(xml_to_dict(child))
            else:
                result[child.tag] = [result[child.tag], xml_to_dict(child)]
        else:
            result[child.tag] = xml_to_dict(child)

    return result


@staticmethod
def process_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    json_data = xml_to_dict(root)
    base_filename = (
        os.path.splitext(os.path.basename(file_path))[0]
        .replace("_error_file", "")
        .replace(".xml", ".cpp")
    )
    return base_filename, json_data


def convert_all_xml_to_json(xml_directory, output_json_path):
    json_data_dict = {}
    xml_files = glob.glob(os.path.join(xml_directory, "*_error_file.xml"))

    with Pool(processes=os.cpu_count()) as pool:
        results = pool.map(process_xml_file, xml_files)

    for base_filename, json_data in results:
        json_data_dict[base_filename] = json_data

    # Write the dictionary to a JSON file
    with open(output_json_path, "w") as json_file:
        json.dump(json_data_dict, json_file, indent=2)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_directory> <output_json_file>")
        sys.exit(1)

    # Extract input and output paths from command-line arguments
    input_directory = sys.argv[1]
    output_json_path = sys.argv[2]

    # Convert all XML files to JSON and store in a single JSON file
    convert_all_xml_to_json(input_directory, output_json_path)
