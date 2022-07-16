cmake_minimum_required(VERSION 3.5)

project(drvlib)

############################################################
# Create a library
############################################################

add_library(ioc
    SHARED 
        src/ioc.c
        src/ioc_sockios.c
        src/ioc_if.c
)

target_include_directories(ioc
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
    ioc
)

############################################################
# Install
############################################################

install (TARGETS ioc
    LIBRARY DESTINATION lib)
