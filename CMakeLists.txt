cmake_minimum_required(VERSION 3.5)

project(algorithmic_questions_ground LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(algorithmic_questions_ground main.cpp)

install(TARGETS algorithmic_questions_ground
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
