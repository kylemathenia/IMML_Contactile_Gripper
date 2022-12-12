#ifndef PTSDKLISTENER_H
#define PTSDKLISTENER_H
#endif

#ifdef _WIN32
#ifndef PTSDK_CPP_LIB_H
#include "PTSDK_CPP_LIB.h"
#endif
#endif

#ifndef PTSDKCONSTANTS_H
#include "PTSDKConstants.h"
#endif

#ifndef PTSDKSENSOR_H
#include "PTSDKSensor.h"
#endif

#include <stdio.h>
//#include <stdint.h>
//#include <string>

#ifdef _WIN32
#include <windows.h>
#endif
#ifndef _WIN32
#include <cstddef>
#include <cstdint>
#include <stdint.h>
#include <pthread.h>
#define BYTE byte
#define DWORD uint32_t
#define HANDLE int
#endif

#define NBYTES_STARTPACKET		4		// Number of bytes in the start packet
#define NBYTES_ENDPACKET		4		// Number of bytes in the end packet
#define MAX_DATAPACKETLEN		2048		// Maximum number of bytes in the data packet (the actual number of bytes may be variable)
#define LOG_BUF_LEN			5000
#define LOG_FILENAME_LEN		100

using namespace std;

#ifdef _WIN32
void PTSDK_CPP_LIB_API PTSDKListener_event_thread_start(void* arg);
#else
void* PTSDKListener_event_thread_start(void* arg);
#endif

/** \brief The PTSDKListener class describes a listener for the Communications Hub with a number of PapillArray Tactile Sensors connected.
 *
 * The PTSDKListener class describes a listener for the Communications Hub with a number of PapillArray Tactile Sensors connected.
 *
 * @author Contactile Pty Ltd
 * @version March 2020
 */
#ifdef _WIN32
class PTSDK_CPP_LIB_API PTSDKListener {
#else
class PTSDKListener {
#endif

private:

	/* Private member variables */

	bool isLogging;						// Flag indicating whether to log data to .csv file
	bool isFlushBuffer;					// Flag indicating whether to flush the hardware input buffer if it contains too many bytes

	BYTE startBytes[NBYTES_STARTPACKET];			// The bytes to match to a start packet from the controller
	BYTE endBytes[NBYTES_ENDPACKET];			// The bytes to match to an end packet from the controller

	BYTE dataPacketBuf[MAX_DATAPACKETLEN];			// A buffer containing the data packet read from the COM port

	int nSensor;						// The number of sensors connected to the communications hub
	PTSDKSensor* pSensors[MAX_NSENSOR];			// Sensors connected to the communications hub

#ifdef _WIN32
	HANDLE serial_handle;					// The handle to the serial port
#else
	int serial_handle;
#endif
#ifdef _WIN32
	HANDLE thread_handle;					// The handle to the thread for listening to the COM port
#else
	pthread_t thread_handle;
#endif
	unsigned int  threadid;					// The id of the thread for listening to the COM port
	bool isListening;					// Set to true when the thread begins, and set to false when we want to kill the thread

	HANDLE logFile_handle;					// The handle to the log file
	char logBuf[LOG_BUF_LEN];				// Buffer for the log file
	int sampleCounter;					// The number of samples read from the comms hub

	/* Private helper functions */

	bool parseDataPacket(BYTE* dataPacketBuf, uint32_t nDataPacketBuf);
	bool validateChecksum(IN const BYTE* dataPacketBuf, IN const uint32_t nDataPacketBuf, IN uint32_t checksum_index);

	void unpackAddress(IN const BYTE data[MAX_DATAPACKETLEN], IN OUT uint32_t* pByteInd, IN uint16_t addressSize, IN OUT uint32_t* pVal);
	void unpackUint8(IN const BYTE data[MAX_DATAPACKETLEN], IN OUT uint32_t* pByteInd, OUT uint8_t* pVal);
	void unpackUint16(IN const BYTE data[MAX_DATAPACKETLEN], IN OUT uint32_t* pByteInd, OUT uint16_t* pVal);
	void unpackUint32(IN const BYTE data[MAX_DATAPACKETLEN], IN OUT uint32_t* pByteInd, OUT uint32_t* pVal);
	void unpackUint64(IN const BYTE data[MAX_DATAPACKETLEN], IN OUT uint32_t* pByteInd, OUT uint64_t* pVal);
	void unpackFloat(IN const BYTE data[MAX_DATAPACKETLEN], IN OUT uint32_t* pByteInd, OUT float* pVal);
	void unpackDouble(IN const BYTE data[MAX_DATAPACKETLEN], IN OUT uint32_t* pByteInd, OUT double* pVal);

	void startListening(void);
	void stopListening(void);

	bool openLogFile(void);
	void closeLogFile(void);
	bool writeHeaderToLog(void);
	bool writeSampleToLog(void);

#ifndef _WIN32
	bool ReadFile(int file_handle, BYTE* buf, DWORD nBytesToRead, DWORD* nBytesRead, void* pOverlapped);
	bool WriteFile(int file_handle, char* buf, DWORD nBytesToWrite, DWORD* nBytesWritten, void* pOverlapped);
	int strcat_s(char* dest, int destsz, const char* src);
	void Sleep(int milliseconds);
#endif

public:

	/* Constructors */

	/**
	 * Constructor.
	 *
	 * @param[in] logFlag A flag indicating whether to log data to CSV file.
	 */
	PTSDKListener(IN const bool logFlag);

	/* Destructors */

	/**
	 * Destructor.
	 */
	~PTSDKListener();

	/* Public member functions */

	/**
	 * Adds a sensor object to the PTSDKListener.
	 *
	 * @param[in] pSensor A pointer to the sensor object.
	 */
	void addSensor(IN PTSDKSensor* pSensor);

	/**
	 * Connects to the COM port.
	 * Used in conjunction with the readNextSample and disconnect functions.
	 *
	 * @param[in] port The COM port name.
	 * @param[in] rate The rate of the connection.
	 * @param[in] parity The parity of the connection.
	 * @param[in] byteSize The byte size for the connection.
	 * @return 0 if successfully connected, error code if unsuccessful.
	 */
	int connect(IN const char* portArg, IN int const baudRateArg, IN const int parityArg, IN const char byteSizeArg);

	/**
	 * Reads the next sample from the COM port and logs the data to the  log file if logging.
	 * Used in conjunction with the connect and disconnect functions.
	 *
	 * @param[in] isFlush Flag to flush the hardware input buffer if too many bytes
	 * @return 0 if successfully read, error code if unsuccessful.
	 */
	bool readNextSample(IN const bool isFlush);

	/**
	 * Disconnects from the COM port and closes the log file if logging
	 * Used in conjunction with the connect and readNextSample functions.
	 */
	void disconnect(void);

	/**
	 * The 'infinite' loop of the listening thread.
	 * The thread implementation necessitates that this is a public member function.
	 * However, this function should never be called except through the startListening function
	 * when the listening thread is spawned.
	 */
	void run(void);

	/**
	 * Connects to the COM port and starts listeneing for data (starts the listening thread),
	 * processes the data and logs the data to a log file.
	 * Used in conjunction with the stopListeningAndDisconnect function.
	 *
	 * @param[in] port The COM port name.
	 * @param[in] rate The rate of the connection.
	 * @param[in] parity The parity of the connection.
	 * @param[in] byteSize The byte size for the connection.
	 * @param[in] isFlush Flag to flush the hardware input buffer if too many bytes
	 * @return 0 if successfully connected, error code if unsuccessful.
	 */
	int connectAndStartListening(IN const char* port, IN const int rate, IN const int parity, IN const char byteSize, IN const bool isFlush);

	/**
	 * Stops listening for data from the serial port (and kills the listening thread), stops logging data to the log file
	 * and disconnects from the COM port.
	 * Used in conjunction with the connectAndStartListening function.
	 */
	void stopListeningAndDisconnect(void);

	/**
	 * Sends a bias request to the controller hub.
	 * A bias should be performed after connecting to the serial port and starting to stream data with the sensor unloaded.
	 * A bias should be performed each time the sensor is known to be unloaded.
	 * A bias operation takes approximately 2 s. Ensure that the sensor remains unloaded throughout this time.
	 * @return true if successfully sent the request, false if unsuccessful.
	 */
	bool sendBiasRequest(void);

	/**
	 * Sets the sampling rate on the Controller.
	 * @param[in] samplingRate The sampling rate in Hz for the Controller: SAMP_RATE_100, SAMP_RATE_250, SAMP_RATE_500 or SAMP_RATE_1000 (default).
	 * @return true if successfully sent the request, false if unsuccessful.
	 */
	bool setSamplingRate(IN const int samplingRate);

	/**
	 * Sends a request to start slip detection to the controller hub.
	 * Slip detection should be started only after the sensor is in stable contact
	 * @return true if successfully sent the request, false if unsuccessful.
	 */
	bool startSlipDetection(void);

	/**
	 * Sends a request to stop slip detection to the controller hub.
	 * Slip detection should be stopped before the sensor is releases the object
	 * @return true if successfully sent the request, false if unsuccessful.
	 */
	bool stopSlipDetection(void);

	/**
	 * Returns the target grip force (max target grip force for all sensors
	 *
	 * @return Target grip force; -1 if no friction estimates
	 */
	double getTargetGripForce(void);

};
