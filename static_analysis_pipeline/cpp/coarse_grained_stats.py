import glob
import multiprocessing
import os
import shutil
import subprocess

from xml_to_json import convert_all_xml_to_json


def cleanup(report_directory):
    shutil.rmtree(report_directory)


def generate_one_xml_report_for_all_file(source_directory, report_directory):
    # Check if source directory provided exists
    if not os.path.exists(source_directory):
        raise NotADirectoryError(f"Directory not found at: {source_directory}")

    # Create the report directory if it doesn't exist
    os.makedirs(report_directory, exist_ok=True)

    # Run cppcheck with specified options
    cppcheck_cmd = [
        "cppcheck",
        "--enable=all",
        "--suppress=missingIncludeSystem",
        "--check-level=exhaustive",
        "--quiet",
        "--xml",
        source_directory,
    ]

    if os.name == "nt":
        cppcheck_cmd.append("--platform=win64")

    error_file = os.path.join(report_directory, "error_file.xml")
    with open(error_file, "w") as error_output:
        try:
            subprocess.run(cppcheck_cmd, stderr=error_output, check=True)
            print("Cppcheck XML report generated successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error running cppcheck: {e}")

    # Generate HTML report
    htmlreport_cmd = [
        "python",
        os.path.join("scripts", "cppcheck_utils", "cppcheck-htmlreport.py"),
        "--file=" + error_file,
        "--report-dir=" + report_directory,
    ]

    try:
        subprocess.run(htmlreport_cmd, check=True)
        print("HTML report generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating HTML report: {e}")


def generate_err_xml(file_path, xml_report_directory):
    file_name = os.path.basename(file_path)
    file_name_no_ext = os.path.splitext(file_name)[0]

    error_file_path = os.path.join(xml_report_directory, f"{file_name_no_ext}_error_file.xml")

    cppcheck_command = [
        "cppcheck",
        "--enable=all",
        "--suppress=missingIncludeSystem",
        "--check-level=exhaustive",
        "--quiet",
        "--xml",
        file_path,
        error_file_path,
    ]

    if os.name == "nt":
        cppcheck_command.append("--platform=win64")

    with open(error_file_path, "w") as error_file:
        subprocess.run(cppcheck_command, stderr=error_file)


def generate_feedback_json_report(source_directory, report_directory):
    # Check if source directory provided exists
    if not os.path.exists(source_directory):
        raise NotADirectoryError(f"Directory not found at: {source_directory}")

    xml_report_directory = os.path.join(report_directory, "xml_files")
    # Create the report directory if it doesn't exist
    os.makedirs(xml_report_directory, exist_ok=True)

    def get_file_args():
        for file_path in glob.glob(os.path.join(source_directory, "*")):
            if os.path.isfile(file_path):
                yield file_path, xml_report_directory

    try:
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            pool.starmap(generate_err_xml, get_file_args())

        convert_all_xml_to_json(
            xml_report_directory, os.path.join(report_directory, "feedback.json")
        )
    finally:
        cleanup(xml_report_directory)


if __name__ == "__main__":
    # Runs before and after feedback
    # generate_one_xml_report_for_all_file("cpp_results/cpp_source", "results/cpp/one_report")
    generate_feedback_json_report(
        "cpp_results/instruct_generations/cpp/files_before_feedback", "results/cpp/before_feedback"
    )
    generate_feedback_json_report(
        "cpp_results/instruct_generations/cpp/files_after_feedback", "results/cpp/after_feedback"
    )
