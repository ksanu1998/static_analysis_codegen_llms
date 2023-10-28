# NLP_Group37

## `cppcheck` installation
* Assuming that you have enabled SSH key based login to GitHub
* $ `git clone <this-branch>`
* $ `cd cppcheck_utils`
* $ `chmod +X install_cppcheck.sh`
* $ `./install_cppcheck.sh`

## Running `cppcheck` and getting a HTML report
* Assuming there is a directory named `source` containing `.cpp` files to be checked
* `cppcheck/build/bin/cppcheck --enable=all --check-level=exhaustive --xml </path/to/source> 2> error_file.xml`
* `cppcheck/htmlreport/cppcheck-htmlreport --file=error_file.xml --report-dir=report`
* Go to `report` and open `index.html`
