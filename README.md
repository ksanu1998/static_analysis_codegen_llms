# NLP_Group37

## `cppcheck` installation
* Assuming that you have enabled SSH key based login to GitHub
* $ `git clone <this-branch>`
* $ `cd cppcheck_utils`
* $ `chmod +X install_cppcheck.sh`
* $ `./install_cppcheck.sh`

## Running `cppcheck` and getting a HTML report
* Assuming there is a directory named `source_directory` containing `.cpp` files to be checked and another one named `report_directory` to store the generated reports
* `chmod +X run_cppcheck.sh`
* `./run_cppcheck.sh <source_directory> <report_directory>`
* Go to `<report_directory>` and open `index.html`
