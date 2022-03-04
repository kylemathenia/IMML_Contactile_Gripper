#include <papillarray_ros_node.hpp>

PapillArrayNode::PapillArrayNode(ros::NodeHandle& nh) : listener_(true) { // listener_ argument: isLogging to .csv file; Log file written to /home/.ros/Logs

	ROS_INFO("Loading parameters...\n");
	loadParams(nh);

	// Create sensors and add to listener
	ROS_INFO("Creating sensors...\n");

	for (int i = 0; i < n_sensors_; i++) {
		ROS_INFO("Creating sensor %d...", i);
		auto sensor = std::make_unique<PTSDKSensor>();
		ROS_INFO("Adding sensor %d to listener...", i);
		listener_.addSensor(sensor.get());
		ROS_INFO("Added sensor %d to listener!\n", i);
		sensors_.push_back(std::move(sensor));

		// Setup publisher for sensor
		std::string topic = "/hub_" + std::to_string(hub_id_) + "/sensor_" + std::to_string(i);
		ros::Publisher sensor_pub = nh.advertise<papillarray_ros_v2::SensorState>(topic, 1);
		sensor_pubs_.push_back(sensor_pub);
	}

	// Start services
	ROS_INFO("Starting services...");
	std::string service_name = "/hub_" + std::to_string(hub_id_) + "/start_slip_detection";
	start_sd_srv_ = nh.advertiseService(service_name,&PapillArrayNode::startSlipDetectionSrvCallback,this);
	if (ros::service::exists(service_name, true)) {
		ROS_INFO("Started %s service", service_name.c_str());
	} else {
		ROS_WARN("%s service not advertised", service_name.c_str());
	}

	service_name = "/hub_" + std::to_string(hub_id_) + "/stop_slip_detection";
	stop_sd_srv_ = nh.advertiseService(service_name,&PapillArrayNode::stopSlipDetectionSrvCallback,this);
	if (ros::service::exists(service_name, true)) {
		ROS_INFO("Started %s service", service_name.c_str());
	} else {
		ROS_WARN("%s service not advertised", service_name.c_str());
	}

	service_name = "/hub_" + std::to_string(hub_id_) + "/send_bias_request";
	send_bias_request_srv_ = nh.advertiseService(service_name,&PapillArrayNode::sendBiasRequestSrvCallback,this);
	if (ros::service::exists(service_name, true)) {
		ROS_INFO("Started %s service", service_name.c_str());
	} else {
		ROS_WARN("%s service not advertised", service_name.c_str());
	}

	// Start listener
	ROS_INFO("Connecting to %s port...", port_.c_str());
	if (listener_.connectAndStartListening(port_.c_str(), baud_rate_, parity_, char(byte_size_), is_flush_)) {
		ROS_FATAL("Failed to connect to port: %s", port_.c_str());
	} else {
		ROS_INFO("Connected to port: %s", port_.c_str());
	}

	// Set sampling rate
	ROS_INFO("Setting sampling rate to %u...",sampling_rate_);
	if (!listener_.setSamplingRate(sampling_rate_)) {
		ROS_WARN("Failed to set sampling rate to: %u", sampling_rate_);
	} else {
		ROS_INFO("Sampling rate set to %u", sampling_rate_);
	}
}

void PapillArrayNode::loadParams(ros::NodeHandle& nh) {
	if (nh.getParam("hub_id", hub_id_)) {
		ROS_INFO("Hub id: %d", hub_id_);
	} else {
		ROS_ERROR("Failed to read hub id param. Ensure set correctly in launch file");
	}
	if (nh.getParam("n_sensors", n_sensors_)) {
		if (n_sensors_ > MAX_NSENSOR or n_sensors_ < 1) {
			ROS_ERROR("Invalid number of sensors!  %d selected (must be no more than %d)", n_sensors_, MAX_NSENSOR);
		} else {
			ROS_INFO("Using %d sensor/s", n_sensors_);
		}
	} else {
		ROS_ERROR("Failed to read number_of_sensors param.  Ensure set correctly in launch file");
	}
	if (nh.getParam("com_port", port_)) {
		ROS_INFO("Reading from serial COM port: %s", port_.c_str());
	} else {
		ROS_ERROR("Failed to read COM port param. Ensure set correctly in launch file");
	}
	if (nh.getParam("baud_rate", baud_rate_)) {
		ROS_INFO("Baud rate: %d Hz", baud_rate_);
	} else {
		ROS_ERROR("Failed to read baud_rate param.  Ensure set correctly in launch file");
	}
	if (nh.getParam("parity", parity_)) {
		ROS_INFO("Parity set to: %d (0=PARITY_NONE, 1=PARITY_ODD, 2=PARITY_EVEN)", parity_);
	} else {
		ROS_ERROR("Failed to read paraty param.  Ensure set correctly in launch file");
	}
	if (nh.getParam("byte_size", byte_size_)) {
		ROS_INFO("Byte size: %d bits", byte_size_);
	} else {
		ROS_ERROR("Failed to read byte_size param.  Ensure set correctly in launch file");
	}

	if (nh.getParam("is_flush", is_flush_)) {
		ROS_INFO("Is Flush: %d", is_flush_);
	} else {
		ROS_ERROR("Failed to read is_flush param. Ensure set correctly in launch file");
	}

	if (nh.getParam("sampling_rate", sampling_rate_)) {
		ROS_INFO("Sampling rate: %d Hz", sampling_rate_);
	} else {
		ROS_ERROR("Failed to read sampling_rate param. Ensure set correctly in launch file");
	}

	ROS_INFO("Loaded parameters.\n");
}

void PapillArrayNode::updateData() {
	if (n_sensors_ == 0) {
		return;
	}

	for (int sensor_id = 0; sensor_id < sensors_.size(); sensor_id++) {
		papillarray_ros_v2::SensorState ss_msg;

		//ROS_INFO("N pillars: %d", sensors_[sensor_id]->getNPillar());
		std_msgs::Header h;
		auto time = ros::Time::now();
		h.stamp.sec = time.sec;
		h.stamp.nsec = time.nsec;
		ss_msg.header = h;

		long timestamp_us = sensors_[sensor_id]->getTimestamp_us();
		ss_msg.tus = timestamp_us;

		double globalForce[NDIM];
		double globalTorque[NDIM];

		// Read global forces
		sensors_[sensor_id]->getGlobalForce(globalForce);
		ss_msg.gfX = static_cast<float>(globalForce[X_IND]);
		ss_msg.gfY = static_cast<float>(globalForce[Y_IND]);
		ss_msg.gfZ = static_cast<float>(globalForce[Z_IND]);
		// Read global torques
		sensors_[sensor_id]->getGlobalTorque(globalTorque);
		ss_msg.gtX = static_cast<float>(globalTorque[X_IND]);
		ss_msg.gtY = static_cast<float>(globalTorque[Y_IND]);
		ss_msg.gtZ = static_cast<float>(globalTorque[Z_IND]);

		// Friction estimate
		ss_msg.friction_est = static_cast<float>(sensors_[sensor_id]->getFrictionEstimate());

		// Target grip force (-1 if no friction estimate)
		ss_msg.target_grip_force = static_cast<float>(sensors_[sensor_id]->getTargetGripForce());

		int n_pillar = sensors_[sensor_id]->getNPillar();

		bool is_sd_active;
		bool is_ref_loaded;
		bool contact_states[n_pillar];
		int slip_states[n_pillar];

		sensors_[sensor_id]->getAllSlipStatus(&is_sd_active,
								&is_ref_loaded,
								contact_states,
								slip_states);

		ss_msg.is_sd_active = is_sd_active;
		ss_msg.is_ref_loaded = is_ref_loaded;
		ss_msg.is_contact = false;

		// Get PillarState data for all pillars in sensor array
		for (int pillar_id = 0; pillar_id < n_pillar; pillar_id++) {
			papillarray_ros_v2::PillarState ps_msg;

			ps_msg.id = pillar_id;
			ps_msg.slip_state = slip_states[pillar_id];
			ps_msg.in_contact = contact_states[pillar_id];

			ss_msg.is_contact = ss_msg.is_contact | ps_msg.in_contact;

			double pillar_d[NDIM];
			sensors_[sensor_id]->getPillarDisplacements(pillar_id, pillar_d);
			ps_msg.dX = static_cast<float>(pillar_d[X_IND]);
			ps_msg.dY = static_cast<float>(pillar_d[Y_IND]);
			ps_msg.dZ = static_cast<float>(pillar_d[Z_IND]);

			double pillar_f[NDIM];
			sensors_[sensor_id]->getPillarForces(pillar_id, pillar_f);
			ps_msg.fX = static_cast<float>(pillar_f[X_IND]);
			ps_msg.fY = static_cast<float>(pillar_f[Y_IND]);
			ps_msg.fZ = static_cast<float>(pillar_f[Z_IND]);

			ss_msg.pillars.push_back(ps_msg);

			if(pillar_id == 0){
				//ROS_INFO("From C++API: %.2f; From ROS: %.2f\n",pillar_f[2], ps_msg.fZ);
			}
		}

		// Publish SensorState message
		sensor_pubs_[sensor_id].publish(ss_msg);
	}
}

bool PapillArrayNode::startSlipDetectionSrvCallback(papillarray_ros_v2::StartSlipDetection::Request &req,
						papillarray_ros_v2::StartSlipDetection::Response &resp) {
	ROS_INFO("startSlipDetection callback");
	resp.result = listener_.startSlipDetection();
	ros::Duration(0.1).sleep(); // wait
	return resp.result;
}

bool PapillArrayNode::stopSlipDetectionSrvCallback(papillarray_ros_v2::StopSlipDetection::Request &req,
						   papillarray_ros_v2::StopSlipDetection::Response &resp) {
	ROS_INFO("stopSlipDetection callback");
	resp.result = listener_.stopSlipDetection();
	ros::Duration(0.1).sleep(); // wait
	return resp.result;
}

bool PapillArrayNode::sendBiasRequestSrvCallback(papillarray_ros_v2::BiasRequest::Request &req,
						 papillarray_ros_v2::BiasRequest::Response &resp) {
	ROS_INFO("sendBiasRequest callback");
	resp.result = listener_.sendBiasRequest();
	ros::Duration(0.1).sleep(); // wait
	return resp.result;
}

int main(int argc, char **argv) {
	ros::init(argc, argv, "papillarray_ros_v2");

	ros::NodeHandle nh("~");

	PapillArrayNode papill_array_node(nh);

	ros::Rate loop_rate(papill_array_node.getSamplingRate());
	loop_rate.sleep();

	int i = 0;
	while (ros::ok()) {
		ros::spinOnce();
		loop_rate.sleep();
		papill_array_node.updateData();	// Update sensor data and publish
		//ROS_INFO("Still spinning: %d",i);
		i++;
	}

	return 0;
}
