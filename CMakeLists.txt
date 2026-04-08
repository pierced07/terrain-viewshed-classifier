cmake_minimum_required(VERSION 3.15)
project(terrain_perception LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(pybind11 REQUIRED)

pybind11_add_module(perception_core
    cpp_src/viewshed.cpp
    cpp_src/classifier.cpp
    cpp_src/bindings.cpp
)

target_compile_options(perception_core PRIVATE -O3 -march=native)