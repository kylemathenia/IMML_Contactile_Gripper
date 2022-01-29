#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/dynamixel_sdk"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/install/lib/python2.7/dist-packages:/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/build" \
    "/usr/bin/python2" \
    "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/dynamixel_sdk/setup.py" \
     \
    build --build-base "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/build/dynamixel_sdk" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/install" --install-scripts="/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/install/bin"
