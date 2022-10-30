#!/bin/bash

echo "Building Program";
./clean.sh;

# set up with cmake
cp -r ./build_config/ ./build/;
cmake ./build/CMakeLists.txt;

# use make
cd ./build/;
make;
cd ..;

# run program
./run.sh;
