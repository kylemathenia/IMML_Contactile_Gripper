#ifndef PAPILLARRAY_ROS_V2_NODE_H_
#define PAPILLARRAY_ROS_V2_NODE_H_

#include <stdio.h>

#include <vector>

#include <ros/ros.h>

// Messages
#include <papillarray_ros_v2/PillarState.h>
#include <papillarray_ros_v2/SensorState.h>

// Services
#include <papillarray_ros_v2/StartSlipDetection.h>
#include <papillarray_ros_v2/StopSlipDetection.h>
#include <papillarray_ros_v2/BiasRequest.h>
//#include <papillarray_ros_v2/SetSamplingRate.h>

#ifdef __unix__
typedef unsigned char byte;
#endif

#ifndef PTSDKCONSTANTS_H
#include <PTSDKConstants.h>
#endif
#ifndef PTSDKLISTENER_H
#include <PTSDKListener.h>
#endif
#ifndef PTSDKSENSOR_H
#include <PTSDKSensor.h>
#endif

class PapillArrayNode {
public:
	// Constructor
	PapillArrayNode(ros::NodeHandle& nh);

	// Destructor
	~PapillArrayNode() {
		// Stop listening for and processing data and disconnect from the COM port
		listener_.stopListeningAndDisconnect();
	}

	// Update sensor data and publish
	void updateData();

	// Get the sampling rate
	int getSamplingRate(){ return sampling_rate_; };

private:
	int hub_id_;

	int n_sensors_;

	std::string port_;
	int baud_rate_;
	int parity_;
	int byte_size_;
	bool is_flush_;
	int sampling_rate_;

	PTSDKListener listener_;
	std::vector<std::unique_ptr<PTSDKSensor> > sensors_;

	// Sensor publishers
	std::vector<ros::Publisher> sensor_pubs_;

	// Services
	ros::ServiceServer start_sd_srv_;
	ros::ServiceServer stop_sd_srv_;
	ros::ServiceServer send_bias_request_srv_;

	// Service callback functions
	bool startSlipDetectionSrvCallback(papillarray_ros_v2::StartSlipDetection::Request &req,
					papillarray_ros_v2::StartSlipDetection::Response &resp);
	bool stopSlipDetectionSrvCallback(papillarray_ros_v2::StopSlipDetection::Request &req,
					papillarray_ros_v2::StopSlipDetection::Response &resp);
	bool sendBiasRequestSrvCallback(papillarray_ros_v2::BiasRequest::Request &req,
					papillarray_ros_v2::BiasRequest::Response &resp);

	// Load parameters from launch file
	void loadParams(ros::NodeHandle& nh);
};

#endif // PAPILLARRAY_ROS_NODE_H_
