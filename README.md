# NLP_Group37

## Install `cppcheck`
Assuming that you have enabled SSH key based login to GitHub
* $ `git clone https://github.com/ksanu1998/NLP_Group37.git`
* $ `git checkout anuroop`
* $ `cd cppcheck_utils`
* $ `chmod +x install_cppcheck.sh`
* $ `./install_cppcheck.sh`

## Run `cppcheck` and generate an HTML report
Assuming there is a directory named `source_directory` containing `.cpp` files to be checked and another one named `report_directory` to store the generated reports
* $ `chmod +x run_cppcheck.sh`
* $ `./run_cppcheck.sh <source_directory> <report_directory>`
* Go to `<report_directory>` and open `index.html`


## Install `flake8`
Assuming that you have enabled SSH key based login to GitHub
* $ `git clone https://github.com/ksanu1998/NLP_Group37.git`
* $ `git checkout anuroop`
* $ `cd flake8_utils`
* $ `chmod +x install_flake8.sh`
* $ `./install_flake8.sh`

## Run `flake8` and generate an TXT report
Assuming there is a directory named `source_directory` containing `.py` files to be checked and another one named `report_directory` to store the generated reports
* $ `chmod +x run_flake8.sh`
* $ `./run_flake8.sh <source_directory> <report_directory>`
* Go to `<report_directory>` and open `flake8_report.txt`
