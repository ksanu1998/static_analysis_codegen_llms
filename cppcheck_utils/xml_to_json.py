import os
import sys
import xml.etree.ElementTree as ET
import json

def xml_to_dict(element):
    result = {}
    result['tag'] = element.tag
    result['attributes'] = element.attrib
    result['text'] = element.text

    for child in element:
        if child.tag in result:
            if type(result[child.tag]) is list:
                result[child.tag].append(xml_to_dict(child))
            else:
                result[child.tag] = [result[child.tag], xml_to_dict(child)]
        else:
            result[child.tag] = xml_to_dict(child)

    return result

def convert_all_xml_to_json(xml_directory, output_json_path):
    json_data_dict = {}

    # Iterate over each file in the specified directory
    for filename in os.listdir(xml_directory):
        if filename.endswith("_error_file.xml"):
            # Extract the base filename without the extension
            base_filename = os.path.splitext(filename)[0]
            source_filename = base_filename.replace("_error_file", "") + ".cpp"

            file_path = os.path.join(xml_directory, filename)

            # Read XML from file
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Convert XML to JSON
            json_data = xml_to_dict(root)

            # Add to the dictionary with the source filename as the key
            json_data_dict[source_filename] = json_data

    # Write the dictionary to a JSON file
    with open(output_json_path, 'w') as json_file:
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
