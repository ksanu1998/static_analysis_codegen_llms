import os
import shutil
import subprocess


def generate_flake8_report(source_directory, report_directory):
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise NotADirectoryError(f"Source directory does not exist: {source_directory}")

    # Create the report directory if it doesn't exist
    if not os.path.exists(report_directory):
        os.makedirs(report_directory)

    stats_file = os.path.join(report_directory, "coarse_grained_stats.txt")
    if os.path.exists(stats_file):
        shutil.rmtree(stats_file)

    # Run flake8 command to generate the statistics and output file
    flake8_command = [
        "flake8",
        "--statistics",
        source_directory,
        "--q",
        "--output-file",
        stats_file,
    ]

    try:
        subprocess.run(flake8_command, check=True)
        print("Flake8 report generated successfully.")
    except subprocess.CalledProcessError:
        # print(f"Error generating Flake8 report: {e}")
        pass


if __name__ == "__main__":
    generate_flake8_report(os.path.join("py_results", "py_source"), os.path.join("results", "py"))
    ...
