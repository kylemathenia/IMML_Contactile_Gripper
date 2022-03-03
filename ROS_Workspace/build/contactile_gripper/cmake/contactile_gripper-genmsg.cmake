# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "contactile_gripper: 2 messages, 6 services")

set(MSG_I_FLAGS "-Icontactile_gripper:/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(contactile_gripper_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg" NAME_WE)
add_custom_target(_contactile_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "contactile_gripper" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg" ""
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv" NAME_WE)
add_custom_target(_contactile_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "contactile_gripper" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv" ""
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv" NAME_WE)
add_custom_target(_contactile_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "contactile_gripper" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv" ""
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv" NAME_WE)
add_custom_target(_contactile_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "contactile_gripper" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv" ""
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv" NAME_WE)
add_custom_target(_contactile_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "contactile_gripper" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv" ""
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg" NAME_WE)
add_custom_target(_contactile_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "contactile_gripper" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg" ""
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv" NAME_WE)
add_custom_target(_contactile_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "contactile_gripper" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv" ""
)

get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv" NAME_WE)
add_custom_target(_contactile_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "contactile_gripper" "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper
)
_generate_msg_cpp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper
)

### Generating Services
_generate_srv_cpp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper
)
_generate_srv_cpp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper
)
_generate_srv_cpp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper
)
_generate_srv_cpp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper
)
_generate_srv_cpp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper
)
_generate_srv_cpp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper
)

### Generating Module File
_generate_module_cpp(contactile_gripper
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(contactile_gripper_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(contactile_gripper_generate_messages contactile_gripper_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_cpp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_cpp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_cpp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_cpp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_cpp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_cpp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_cpp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_cpp _contactile_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(contactile_gripper_gencpp)
add_dependencies(contactile_gripper_gencpp contactile_gripper_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS contactile_gripper_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper
)
_generate_msg_eus(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper
)

### Generating Services
_generate_srv_eus(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper
)
_generate_srv_eus(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper
)
_generate_srv_eus(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper
)
_generate_srv_eus(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper
)
_generate_srv_eus(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper
)
_generate_srv_eus(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper
)

### Generating Module File
_generate_module_eus(contactile_gripper
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(contactile_gripper_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(contactile_gripper_generate_messages contactile_gripper_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_eus _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_eus _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_eus _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_eus _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_eus _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_eus _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_eus _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_eus _contactile_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(contactile_gripper_geneus)
add_dependencies(contactile_gripper_geneus contactile_gripper_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS contactile_gripper_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper
)
_generate_msg_lisp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper
)

### Generating Services
_generate_srv_lisp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper
)
_generate_srv_lisp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper
)
_generate_srv_lisp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper
)
_generate_srv_lisp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper
)
_generate_srv_lisp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper
)
_generate_srv_lisp(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper
)

### Generating Module File
_generate_module_lisp(contactile_gripper
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(contactile_gripper_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(contactile_gripper_generate_messages contactile_gripper_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_lisp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_lisp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_lisp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_lisp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_lisp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_lisp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_lisp _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_lisp _contactile_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(contactile_gripper_genlisp)
add_dependencies(contactile_gripper_genlisp contactile_gripper_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS contactile_gripper_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper
)
_generate_msg_nodejs(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper
)

### Generating Services
_generate_srv_nodejs(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper
)
_generate_srv_nodejs(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper
)
_generate_srv_nodejs(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper
)
_generate_srv_nodejs(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper
)
_generate_srv_nodejs(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper
)
_generate_srv_nodejs(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper
)

### Generating Module File
_generate_module_nodejs(contactile_gripper
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(contactile_gripper_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(contactile_gripper_generate_messages contactile_gripper_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_nodejs _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_nodejs _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_nodejs _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_nodejs _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_nodejs _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_nodejs _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_nodejs _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_nodejs _contactile_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(contactile_gripper_gennodejs)
add_dependencies(contactile_gripper_gennodejs contactile_gripper_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS contactile_gripper_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper
)
_generate_msg_py(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper
)

### Generating Services
_generate_srv_py(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper
)
_generate_srv_py(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper
)
_generate_srv_py(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper
)
_generate_srv_py(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper
)
_generate_srv_py(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper
)
_generate_srv_py(contactile_gripper
  "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper
)

### Generating Module File
_generate_module_py(contactile_gripper
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(contactile_gripper_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(contactile_gripper_generate_messages contactile_gripper_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Float32List.msg" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_py _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperSetLimit.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_py _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/GripperChangeMode.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_py _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/StepperOff.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_py _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/ChangeMode.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_py _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/msg/Int32List.msg" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_py _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/DataRecorder.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_py _contactile_gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/srv/UIMenu.srv" NAME_WE)
add_dependencies(contactile_gripper_generate_messages_py _contactile_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(contactile_gripper_genpy)
add_dependencies(contactile_gripper_genpy contactile_gripper_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS contactile_gripper_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/contactile_gripper
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(contactile_gripper_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/contactile_gripper
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(contactile_gripper_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/contactile_gripper
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(contactile_gripper_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/contactile_gripper
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(contactile_gripper_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/contactile_gripper
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(contactile_gripper_generate_messages_py std_msgs_generate_messages_py)
endif()
