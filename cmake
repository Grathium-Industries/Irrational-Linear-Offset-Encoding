# only for cmake --version >= 3.5.1
cmake_minimum_required(VERSION 3.5.1)
project(rvarago-hello-cmake)

set(EXEC hello)
set(CMAKE_CXX_STANDARD 14)

include_directories(src/includes)
file(GLOB SOURCES src/*.cpp)

add_executable(${EXEC} ${SOURCES})
