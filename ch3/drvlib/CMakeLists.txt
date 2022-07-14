cmake_minimum_required(VERSION 3.5)

project(ioc_query)

############################################################
# Create a library
############################################################

add_library(iocq
    SHARED 
        src/ioc_query.c
)

target_include_directories(iocq
    PUBLIC
        include
)

############################################################
# Create an executable
############################################################

add_executable(test
    src/main.c
)

target_include_directories(test
    PUBLIC
        include
)

target_link_libraries( test
    iocq
)

############################################################
# Install
############################################################

install (TARGETS iocq
    LIBRARY DESTINATION lib)
