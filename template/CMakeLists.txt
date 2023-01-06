cmake_minimum_required(VERSION 3.5)

project(algorithmic_questions_ground LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(SOLUTION_LIBRARY_LIB_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib)
set(SOLUTION_LIBRARY_INCLUDE_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/solution)
set(APP_BINARY_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/bin)

enable_testing()

add_subdirectory(solution)
add_subdirectory(tests)

add_executable(algorithmic_questions_ground main.cpp)

target_include_directories(algorithmic_questions_ground PRIVATE
        solution)

target_link_libraries(algorithmic_questions_ground PRIVATE solution)

install(TARGETS algorithmic_questions_ground
                DESTINATION ${APP_BINARY_DIRECTORY})
