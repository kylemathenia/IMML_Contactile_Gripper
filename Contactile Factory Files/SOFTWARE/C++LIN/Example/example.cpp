// USER_APP_EXAMPLE.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>
#ifdef _WIN32
#include <tchar.h>
#endif

#ifndef PTSDKCONSTANTS_H
#include "PTSDKConstants.h"
#endif
#ifndef PTSDKLISTENER_H
#include "PTSDKListener.h"
#endif
#ifndef PTSDKSENSOR_H
#include "PTSDKSensor.h"
#endif

#ifndef _WIN32
#include <ctime>
#include <chrono>
#include <thread>
#endif

#ifdef _WIN32
int _tmain(int argc, _TCHAR* argv[])
#else
int main()
#endif
{
	int example;
	//example = 1; 		// Single thread example
	example = 2; 		// Multi-threaded example

	bool isLogging;
	isLogging = true;	// Log data to .csv file
	//isLogging = false;	// Don't log data to .csv file

	int sampleRate;
	sampleRate = SAMP_RATE_500;	// Set sampling rate to 500 Hz
	//sampleRate = SAMP_RATE_100;	// Set sampling rate to 100 Hz

	bool isFlush;
	isFlush = true;			// Flush hardware input buffer if too many bytes
	//isFlush = false;		// Don't flush hardware input buffer

	/* Initialise a PTSDKSensor object for sensor connected to SEN0 port */
	PTSDKSensor sen0 = PTSDKSensor();

	/* Initialise a PTSDKSensor object for SEN1 sensor */
	PTSDKSensor sen1 = PTSDKSensor();

	/* Initialise the PTSDKListener object */
	PTSDKListener listener = PTSDKListener(isLogging);

	/* Add sensor 0 to the listener */
	listener.addSensor(&sen0);

	/* Add sensor 1 to the listener */
	listener.addSensor(&sen1);

	/* Initialise connection parameters */
#ifdef _WIN32
	char port[] = "\\\\.\\COM5"; 	// The name of the COM port to connect with
#else
	char port[] = "/dev/ttyACM0";
#endif
	int rate = 11520;//9600; 	// The rate of the serial connection
	int parity = 0; 		// 0=PARITY_NONE, 1=PARITY_ODD, 2=PARITY_EVEN
	char byteSize = 8; 		// The number of bits in a byte


	/*
	 * EXAMPLE 1: Single thread
	 */

	if (example == 1) {
		/* Connect to serial port */
		if (listener.connect(port, rate, parity, byteSize) == 0) {
			printf("main(): Successfully connected to %s\n", port);
		}
		else {
			printf("main(): FAILED to connect to %s\n", port);
			return -1;
		}

		/* Perform bias */
		if(listener.sendBiasRequest()){
			printf("main(): Successfully sent bias request.\n");
		}else{
			printf("main(): FAILED to send bias request.\n");
			return -1;
		}
#ifdef _WIN32
		Sleep(1000);
#else
		std::this_thread::sleep_for(std::chrono::milliseconds(1300));
#endif

		/* Set sampling rate */
		if(listener.setSamplingRate(sampleRate)){
			printf("main(): Successfully set sampling rate to %d.\n",sampleRate);
		}else{
			printf("main(): FAILED to set sampling rate.\n");
			return -1;
		}

		/* Read samples and do something */
		int sampleCount = 0;
		while (true) {
			sampleCount++;
			if (listener.readNextSample(isFlush)) {
				// Print every 100th sample
				if (sampleCount%100 == 0) {
					// Print XYZ force of pillar 3 on SEN0
					int pInd = 3;
					double force[NDIM];
					sen0.getPillarForces(pInd, force);
					for (int dInd = 0; dInd < NDIM; dInd++) {
						printf("S0_P%d: F%d = %.3f\n", pInd, dInd, force[dInd]);
					}
					printf("\n");

					// Print XYZ displacement of pillar 5 on SEN0
					pInd = 5;
					double displacement[NDIM];
					sen0.getPillarDisplacements(pInd, displacement);
					for (int dInd = 0; dInd < NDIM; dInd++) {
						printf("S0_P%d: D%d = %.3f\n", pInd, dInd, displacement[dInd]);
					}
					printf("\n");
				}
			}
			else {
				printf("main(): FAILED to read sample.\n");
			}
		}

		listener.disconnect();
		return 0;
	}


	/*
	 * EXAMPLE 2: Multi-threaded
	 */
	if (example == 2) {
		/* Connect to the serial port and start listening for and processing data in a separate thread */
		if (listener.connectAndStartListening(port, rate, parity, byteSize, isFlush) == 0) {
			printf("main(): Successfully connected to %s & started listening.\n", port);
		}
		else {
			printf("main(): FAILED to connect to %s\n, didn't start listening", port);
			return -1;
		}

		/* Perform bias */
		if(listener.sendBiasRequest()){
			printf("main(): Successfully sent bias request.\n");
		}else{
			printf("main(): FAILED to send bias request.\n");
			return -1;
		}
#ifdef _WIN32
		Sleep(1000);
#else
		std::this_thread::sleep_for(std::chrono::milliseconds(1300));
#endif

		/* Set sampling rate */
		if(listener.setSamplingRate(sampleRate)){
			printf("main(): Successfully set sampling rate to %d.\n",sampleRate);
		}else{
			printf("main(): FAILED to set sampling rate.\n");
			return -1;
		}

		/* Print sample once every second for 10 seconds */
		for (int i = 0; i < 10; i++) {
#ifdef _WIN32
			Sleep(1000);
#else
			std::this_thread::sleep_for(std::chrono::milliseconds(1000));
#endif
			// Get the XYZ global force on SEN1
			double globalForce[NDIM];
			sen1.getGlobalForce(globalForce);
			for (int dInd = 0; dInd < NDIM; dInd++) {
				printf("main(): S1: global F%d = %.3f\n", dInd, globalForce[dInd]);
			}
			printf("\n");

			// Get XYZ displacements of all pillars of SEN1
			double  allDisplacements[NDIM][MAX_NPILLAR];
			sen1.getAllDisplacements(allDisplacements);
			for (int pInd = 0; pInd < sen1.getNPillar(); pInd++) {
				printf("S1_P%d:",pInd);
				for (int dInd = 0; dInd < NDIM; dInd++) {
					printf("\tD%d: %.3f", dInd, allDisplacements[dInd][pInd]);
				}
				printf("\n");
			}
			printf("\n");
		}

#ifdef _WIN32
			Sleep(1000);
#else
			std::this_thread::sleep_for(std::chrono::milliseconds(1300));
#endif
			printf("main(): Start slip detection.\n");
			listener.startSlipDetection();

#ifdef _WIN32
			Sleep(1000);
#else
			std::this_thread::sleep_for(std::chrono::milliseconds(1000));
#endif

			printf("main(): Stop slip detection.\n");
			listener.stopSlipDetection();

#ifdef _WIN32
			Sleep(1000);
#else
			std::this_thread::sleep_for(std::chrono::milliseconds(1000));
#endif

		/* Stop listening and disconnect from the serial port */
		listener.stopListeningAndDisconnect();
		return 0;
	}
}

