cmake_minimum_required(VERSION 3.5)

project(solution LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(solution Solution.cpp)

install(TARGETS solution
    DESTINATION ${SOLUTION_LIBRARY_LIB_DIRECTORY})
install(FILES Solution.h
    DESTINATION ${SOLUTION_LIBRARY_LIB_DIRECTORY})
