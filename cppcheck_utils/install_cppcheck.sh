#!/bin/bash

# Clone the cppcheck repository from GitHub
git clone https://github.com/danmar/cppcheck.git

# Create a 'build' directory and navigate to it
mkdir build
cd build

# Run CMake to configure the build
cmake ..

# Build the project using CMake
cmake --build .
