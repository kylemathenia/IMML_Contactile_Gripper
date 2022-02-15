# Install script for directory: /home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/papillarray_ros_v2/msg" TYPE FILE FILES
    "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg"
    "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/papillarray_ros_v2/srv" TYPE FILE FILES
    "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv"
    "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv"
    "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/papillarray_ros_v2/cmake" TYPE FILE FILES "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/build/papillarray_ros_v2/catkin_generated/installspace/papillarray_ros_v2-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/devel/include/papillarray_ros_v2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/devel/share/roseus/ros/papillarray_ros_v2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/devel/share/common-lisp/ros/papillarray_ros_v2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/devel/share/gennodejs/ros/papillarray_ros_v2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/devel/lib/python2.7/dist-packages/papillarray_ros_v2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/devel/lib/python2.7/dist-packages/papillarray_ros_v2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/build/papillarray_ros_v2/catkin_generated/installspace/papillarray_ros_v2.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/papillarray_ros_v2/cmake" TYPE FILE FILES "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/build/papillarray_ros_v2/catkin_generated/installspace/papillarray_ros_v2-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/papillarray_ros_v2/cmake" TYPE FILE FILES
    "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/build/papillarray_ros_v2/catkin_generated/installspace/papillarray_ros_v2Config.cmake"
    "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/build/papillarray_ros_v2/catkin_generated/installspace/papillarray_ros_v2Config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/papillarray_ros_v2" TYPE FILE FILES "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/package.xml")
endif()

