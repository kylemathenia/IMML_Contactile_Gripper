# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "papillarray_ros_v2: 2 messages, 3 services")

set(MSG_I_FLAGS "-Ipapillarray_ros_v2:/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(papillarray_ros_v2_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv" NAME_WE)
add_custom_target(_papillarray_ros_v2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "papillarray_ros_v2" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv" ""
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv" NAME_WE)
add_custom_target(_papillarray_ros_v2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "papillarray_ros_v2" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv" ""
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg" NAME_WE)
add_custom_target(_papillarray_ros_v2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "papillarray_ros_v2" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg" "papillarray_ros_v2/PillarState:std_msgs/Header"
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg" NAME_WE)
add_custom_target(_papillarray_ros_v2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "papillarray_ros_v2" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv" NAME_WE)
add_custom_target(_papillarray_ros_v2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "papillarray_ros_v2" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg"
  "${MSG_I_FLAGS}"
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/papillarray_ros_v2
)
_generate_msg_cpp(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/papillarray_ros_v2
)

### Generating Services
_generate_srv_cpp(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/papillarray_ros_v2
)
_generate_srv_cpp(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/papillarray_ros_v2
)
_generate_srv_cpp(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/papillarray_ros_v2
)

### Generating Module File
_generate_module_cpp(papillarray_ros_v2
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/papillarray_ros_v2
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(papillarray_ros_v2_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(papillarray_ros_v2_generate_messages papillarray_ros_v2_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_cpp _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_cpp _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_cpp _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_cpp _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_cpp _papillarray_ros_v2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(papillarray_ros_v2_gencpp)
add_dependencies(papillarray_ros_v2_gencpp papillarray_ros_v2_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS papillarray_ros_v2_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg"
  "${MSG_I_FLAGS}"
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/papillarray_ros_v2
)
_generate_msg_eus(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/papillarray_ros_v2
)

### Generating Services
_generate_srv_eus(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/papillarray_ros_v2
)
_generate_srv_eus(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/papillarray_ros_v2
)
_generate_srv_eus(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/papillarray_ros_v2
)

### Generating Module File
_generate_module_eus(papillarray_ros_v2
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/papillarray_ros_v2
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(papillarray_ros_v2_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(papillarray_ros_v2_generate_messages papillarray_ros_v2_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_eus _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_eus _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_eus _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_eus _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_eus _papillarray_ros_v2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(papillarray_ros_v2_geneus)
add_dependencies(papillarray_ros_v2_geneus papillarray_ros_v2_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS papillarray_ros_v2_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg"
  "${MSG_I_FLAGS}"
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/papillarray_ros_v2
)
_generate_msg_lisp(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/papillarray_ros_v2
)

### Generating Services
_generate_srv_lisp(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/papillarray_ros_v2
)
_generate_srv_lisp(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/papillarray_ros_v2
)
_generate_srv_lisp(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/papillarray_ros_v2
)

### Generating Module File
_generate_module_lisp(papillarray_ros_v2
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/papillarray_ros_v2
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(papillarray_ros_v2_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(papillarray_ros_v2_generate_messages papillarray_ros_v2_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_lisp _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_lisp _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_lisp _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_lisp _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_lisp _papillarray_ros_v2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(papillarray_ros_v2_genlisp)
add_dependencies(papillarray_ros_v2_genlisp papillarray_ros_v2_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS papillarray_ros_v2_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg"
  "${MSG_I_FLAGS}"
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/papillarray_ros_v2
)
_generate_msg_nodejs(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/papillarray_ros_v2
)

### Generating Services
_generate_srv_nodejs(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/papillarray_ros_v2
)
_generate_srv_nodejs(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/papillarray_ros_v2
)
_generate_srv_nodejs(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/papillarray_ros_v2
)

### Generating Module File
_generate_module_nodejs(papillarray_ros_v2
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/papillarray_ros_v2
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(papillarray_ros_v2_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(papillarray_ros_v2_generate_messages papillarray_ros_v2_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_nodejs _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_nodejs _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_nodejs _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_nodejs _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_nodejs _papillarray_ros_v2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(papillarray_ros_v2_gennodejs)
add_dependencies(papillarray_ros_v2_gennodejs papillarray_ros_v2_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS papillarray_ros_v2_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg"
  "${MSG_I_FLAGS}"
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/papillarray_ros_v2
)
_generate_msg_py(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/papillarray_ros_v2
)

### Generating Services
_generate_srv_py(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/papillarray_ros_v2
)
_generate_srv_py(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/papillarray_ros_v2
)
_generate_srv_py(papillarray_ros_v2
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/papillarray_ros_v2
)

### Generating Module File
_generate_module_py(papillarray_ros_v2
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/papillarray_ros_v2
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(papillarray_ros_v2_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(papillarray_ros_v2_generate_messages papillarray_ros_v2_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StartSlipDetection.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_py _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/BiasRequest.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_py _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/SensorState.msg" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_py _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/msg/PillarState.msg" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_py _papillarray_ros_v2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/papillarray_ros_v2/srv/StopSlipDetection.srv" NAME_WE)
add_dependencies(papillarray_ros_v2_generate_messages_py _papillarray_ros_v2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(papillarray_ros_v2_genpy)
add_dependencies(papillarray_ros_v2_genpy papillarray_ros_v2_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS papillarray_ros_v2_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/papillarray_ros_v2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/papillarray_ros_v2
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(papillarray_ros_v2_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/papillarray_ros_v2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/papillarray_ros_v2
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(papillarray_ros_v2_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/papillarray_ros_v2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/papillarray_ros_v2
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(papillarray_ros_v2_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/papillarray_ros_v2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/papillarray_ros_v2
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(papillarray_ros_v2_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/papillarray_ros_v2)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/papillarray_ros_v2\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/papillarray_ros_v2
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(papillarray_ros_v2_generate_messages_py std_msgs_generate_messages_py)
endif()
