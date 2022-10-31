cmake_minimum_required(VERSION 3.13)
project(ILOE)

set(CMAKE_CXX_STANDARD 14)
set(SOURCE_FILES ../src/main.cpp)
set(CMAKE_CXX_FLAGS "-lgmp")

add_executable(ILOE ${SOURCE_FILES})
