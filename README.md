# IMML_Contactile_Gripper

![gripper](https://media.giphy.com/media/9kfGCiUqRPZpQja6VG/giphy-downsized-large.gif)

- Ubuntu 16.04
- ROS Melodic
- Launch the system by running "cd ~/insert_path_here/IMML_Contactile_Gripper && ./launch.py"

## Tips
### .bashrc
- add source /opt/ros/melodic/setup.bash to find ros.
- add source /insert_path_here/IMML_Contactile_Gripper/ROS_Workspace/devel/setup.bash to setup the ros workspace.
- add export ROS_PACKAGE_PATH=/insert_path_here/IMML_Contactile_Gripper/ROS_Workspace:$ROS_PACKAGE_PATH to have ros know the package path for tab completion and such. 
- add alias launchgripper="cd /insert_path_here/IMML_Contactile_Gripper && ./launch.py" to start the system quickly. 
- add alias killros="rosnode kill -a" to quickly kill all ros nodes if the system becomes unresponsive. 

### General
- When debugging ros nodes, start them manually in the terminal. When they crash you can see the error this way, as opposed to the gnome terminal window disappearing. 
