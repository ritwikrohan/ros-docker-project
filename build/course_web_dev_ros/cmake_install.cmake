# Install script for directory: /home/user/simulation_ws/src/course_web_dev_ros

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/user/simulation_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/course_web_dev_ros/action" TYPE FILE FILES
    "/home/user/simulation_ws/src/course_web_dev_ros/action/ExampleAction.action"
    "/home/user/simulation_ws/src/course_web_dev_ros/action/WaypointAction.action"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/course_web_dev_ros/msg" TYPE FILE FILES
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/ExampleActionAction.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/ExampleActionActionGoal.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/ExampleActionActionResult.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/ExampleActionActionFeedback.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/ExampleActionGoal.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/ExampleActionResult.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/ExampleActionFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/course_web_dev_ros/msg" TYPE FILE FILES
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/WaypointActionAction.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/WaypointActionActionGoal.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/WaypointActionActionResult.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/WaypointActionActionFeedback.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/WaypointActionGoal.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/WaypointActionResult.msg"
    "/home/user/simulation_ws/devel/share/course_web_dev_ros/msg/WaypointActionFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/course_web_dev_ros/cmake" TYPE FILE FILES "/home/user/simulation_ws/build/course_web_dev_ros/catkin_generated/installspace/course_web_dev_ros-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/user/simulation_ws/devel/include/course_web_dev_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/user/simulation_ws/devel/share/roseus/ros/course_web_dev_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/user/simulation_ws/devel/share/common-lisp/ros/course_web_dev_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/user/simulation_ws/devel/share/gennodejs/ros/course_web_dev_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/user/simulation_ws/devel/lib/python3/dist-packages/course_web_dev_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/user/simulation_ws/devel/lib/python3/dist-packages/course_web_dev_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/user/simulation_ws/build/course_web_dev_ros/catkin_generated/installspace/course_web_dev_ros.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/course_web_dev_ros/cmake" TYPE FILE FILES "/home/user/simulation_ws/build/course_web_dev_ros/catkin_generated/installspace/course_web_dev_ros-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/course_web_dev_ros/cmake" TYPE FILE FILES
    "/home/user/simulation_ws/build/course_web_dev_ros/catkin_generated/installspace/course_web_dev_rosConfig.cmake"
    "/home/user/simulation_ws/build/course_web_dev_ros/catkin_generated/installspace/course_web_dev_rosConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/course_web_dev_ros" TYPE FILE FILES "/home/user/simulation_ws/src/course_web_dev_ros/package.xml")
endif()

