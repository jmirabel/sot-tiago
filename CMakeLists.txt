# Copyright 2016, Thomas Moulard, Olivier Stasse, JRL, CNRS/AIST

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

SET(PROJECT_NAMESPACE stack-of-tasks)
SET(PROJECT_NAME sot-tiago)
SET(PROJECT_DESCRIPTION "dynamic-graph package for Tiago robot")
SET(PROJECT_URL "http://github.com/${PROJECT_NAMESPACE}/${PROJECT_NAME}")

OPTION(SUFFIX_SO_VERSION
  "Suffix shared library name by a string depending on git status of project"
  ON)

INCLUDE(cmake/base.cmake)
INCLUDE(cmake/boost.cmake)
INCLUDE(cmake/eigen.cmake)
INCLUDE(cmake/lapack.cmake)
INCLUDE(cmake/ros.cmake)
INCLUDE(cmake/python.cmake)

SET(CUSTOM_HEADER_DIR "${PROJECT_NAME}")

SET(CXX_DISABLE_WERROR True)

SET(PKG_CONFIG_ADDITIONAL_VARIABLES
  ${PKG_CONFIG_ADDITIONAL_VARIABLES}
  plugindirname
  plugindir
  )

CMAKE_POLICY(SET CMP0048 OLD)
PROJECT(${PROJECT_NAME} CXX)

# Search for dependencies.

ADD_REQUIRED_DEPENDENCY("pinocchio")

ADD_REQUIRED_DEPENDENCY("dynamic-graph >= 3.0.0")
ADD_REQUIRED_DEPENDENCY("sot-core >= 3.0.0")
ADD_REQUIRED_DEPENDENCY("sot-dynamic-pinocchio >= 3.1")
ADD_REQUIRED_DEPENDENCY("dynamic-graph-python >= 3.0.0")

ADD_REQUIRED_DEPENDENCY("dynamic_graph_bridge_msgs")
ADD_REQUIRED_DEPENDENCY("dynamic_graph_bridge >= 3.0")

ADD_OPTIONAL_DEPENDENCY("tiago_data")
# Search for dependencies.
# Boost
SET(BOOST_COMPONENTS filesystem system thread)
SEARCH_FOR_BOOST()
SEARCH_FOR_EIGEN()

FINDPYTHON()
INCLUDE_DIRECTORIES(SYSTEM ${PYTHON_INCLUDE_PATH})

# Handle rpath necessary to handle ROS multiplace packages
# libraries inclusion
SET(CMAKE_INSTALL_LIBDIR lib)
SET(CMAKE_SKIP_BUILD_RPATH  FALSE)
SET(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
SET(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}")
SET(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

# Add subdirectories.
ADD_SUBDIRECTORY(src)

IF(TIAGO_DATA_FOUND)
  INSTALL(FILES
    ${PROJECT_SOURCE_DIR}/tests/test.py
    ${PROJECT_SOURCE_DIR}/tests/appli.py
    ${PROJECT_SOURCE_DIR}/tests/stop-controllers.py
    DESTINATION
    ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/tests
    )

ENDIF(TIAGO_DATA_FOUND)
