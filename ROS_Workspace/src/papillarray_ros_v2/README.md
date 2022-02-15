# README #

## Overview ##

A ROS wrapper around the Contactile PapillArraySDK

## Setup ##
The following instructions have been tested on Ubuntu 18.04 and Ubuntu 20.04.

1) Copy the repository into your catkin workspace
```
	cp papillarray_ros_v2 <ws_location>/src
```
	
2) Build catkin ws
```
	cd <ws_location>
	catkin_make
	source devel/setup.bash
```

3) Edit parameters in papillarray.launch and ensure calibration files are placed in <path\_to\_papillarray\_ros\>/bin folder

4) Run
```
	roslaunch papillarray_ros papillarray.launch
```

## Publishers ##

A publisher is set up for each sensor connected. Data from each sensor is published as a _SensorState_ message on the ROS topic ```/papillarray_node/sensor_n```, where n is the sensor id (0 to _num\_sensors_ - 1).

## Services ##

Several ROS services are provided to interact with the sensors.

_**/send_bias_request**_

Sends a bias request to the communications hub. Should be performed if the sensors are known to be unloaded

_**/start_slip_detection**_

Starts the slip detection algorithm for specified sensor.  Should be called after a number of pillars of the sensor are already in contact, before tangential loading of the sensor.

_**/stop_slip_detection**_

Stops and resets the slip detection algorithms.
