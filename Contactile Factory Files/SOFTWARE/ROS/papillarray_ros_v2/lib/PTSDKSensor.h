#ifndef PTSDKSENSOR_H
#define PTSDKSENSOR_H
#endif

#ifdef _WIN32
#ifndef PTSDK_CPP_LIB_H
#include "PTSDK_CPP_LIB.h"
#endif
#endif

#ifndef PTSDKCONSTANTS_H
#include "PTSDKConstants.h"
#endif

#ifndef PTSDKPILLAR_H
#include "PTSDKPillar.h"
#endif

#include <stdint.h>

/** \brief The PTSDKSensor class describes a PapillArray Tactile Sensor comprised of multiple pillars.
 *
 * The PTSDKSensor class describes a PapillArray sensor comprised of multiple pillars.
 *
 * @author Contactile Pty Ltd
 * @version March 2020
 */
#ifdef _WIN32
class PTSDK_CPP_LIB_API PTSDKSensor {
#else
class PTSDKSensor {
#endif

	friend class PTSDKListener;

private:
	/* Private member variables of PTSDKSensor class */

	uint64_t timestamp_us;

	PTSDKPillar* pPillars[MAX_NPILLAR];		// Array of Pillars in this Sensor
	int nPillar;					// Number of Pillars in this sensor

	double globalForceVals[NDIM];			// Buffer of 3D force values
	double globalTorqueVals[NDIM];			// Buffer of 3D torque values

	bool isSlipDetectionActive;			// The slip detection status (active or inactive)
	bool isRefPillarLoaded;
	int pillarSlipStates[MAX_NPILLAR];		// The slip status (slipped or not slipped) of each pillar of this status
	double pillarFrictionEstimates[MAX_NPILLAR];
	double sensorFrictionEstimate;			// The current friction estimate from this sensor
	double sensorTargetGripForce;			// The current target grip force base on this sensor friction estimate and tangential force


	/* private member functions of the PTSDKSensor class */

	void init(IN const int nPillar);
	void addSensorSample(IN const float globalForceVals[NDIM], IN const float globalTorqueVals[NDIM], IN const uint64_t timestamp_us);
	void addPillarSample(IN const float pillarForceVlas[MAX_NPILLAR][NDIM], IN const float pillarDisplacementVals[MAX_NPILLAR][NDIM], IN const uint64_t timestamp_us);
	void addSensorSlipSample(IN const uint8_t sensorSlipState, IN const float sensorFrictionEstimate, IN const float sensorTargetGripForce);
	void addPillarSlipSample(IN const uint8_t pillarSlipStates[MAX_NPILLAR], IN const float pillarFrictionEstimates[MAX_NPILLAR]);

public:

	/**
	 * Constructor - Initialises pillars and their calibrations.
	 *
	 * @param[in] calibrationFilename The name of the calibration file.
	 */
	PTSDKSensor(void);

	/**
	 * Destructor.
	 */
	~PTSDKSensor(void);

	/**
	 * Gets the current X, Y and Z displacements (mm) of all pillars of this sensor.
	 *
	 * @param[out] result The X, Y and Z displacements (mm) of all pillars.
	 */
	void getAllDisplacements(OUT double result[NDIM][MAX_NPILLAR]);

	/**
	 * Gets the current X, Y and Z forces (N) of all pillars of this sensor.
	 *
	 * @param[out] result The X, Y and Z forces (N) of all pillars.
	 */
	void getAllForces(OUT double result[NDIM][MAX_NPILLAR]);

	/**
	 * Gets the slip status of all pillars of this sensor.
	 *
	 * @param[out] isSlipDetectionActive True if slip detection is active, false otherwise.
	 * @param[out] contactStates For each pillar, true if the pillar normal force exceeds the threshold for contact, false otherwise.
	 * @param[out] slipStates The slip state of all pillars - INELIGIBLE if the pillar was not in contact when slip detection started, CONTACT_AT_START if the pillar was in contact when slip detection started, LOST_CONTACT if the pillar lost contact after slip detection started, TLOADING if the pillar is being tangentially loaded, or SLIPPED if the pillar has slipped.
	 */
	void getAllSlipStatus(OUT bool* isSlipDetectionActive, OUT bool* isRefPillarLoaded, OUT bool contactStates[MAX_NPILLAR], OUT int slipStates[MAX_NPILLAR]);

	/**
	 * Gets the current friction estimate from this sensor.
	 *
	 * @return The current friction estimate from this sensor; -1 if estimate of friction is not available.
	 */
	double getFrictionEstimate(void);

	/**
	 * Gets the target grip force to prevent slip.
	 *
	 * @return The target grip force to prevent slip; -1 if there is no friction estimate;
	 */
	double getTargetGripForce(void);

	/**
	 * Gets the global X,Y,Z force (N) acting on the sensor.
	 *
	 * @param[out] result The global X, Y and Z force (N).
	 */
	void getGlobalForce(OUT double result[NDIM]);

	/**
	 * Gets the global X,Y,Z torque (N.mm) acting on the sensor.
	 *
	 * @param[out] result The global X, Y and Z torque (N.mm).
	 */
	void getGlobalTorque(OUT double result[NDIM]);

	/**
	 * Gets the number of pillars in this sensor.
	 *
	 * @return The number of pillars in this sensor.
	 */
	int getNPillar(void);

	/**
	 * Gets the current X, Y and Z displacement (mm) of a pillar.
	 *
	 * @param[in] pillarInd The index of the pillar.
	 * @param[out] result The X, Y and Z displacement (mm) of the pillar.
	 *
	 * @return True if the pillar index is valid; false otherwise.
	 */
	bool getPillarDisplacements(IN const int pillarInd, OUT double result[NDIM]);

	/**
	 * Gets the current X, Y and Z force (N) of a pillar.
	 *
	 * @param[in] pillarInd The index of the pillar.
	 * @param[out] result The X, Y and Z force (N) of the pillar.
	 *
	 * @return True if the pillar index is valid; false otherwise.
	 */
	bool getPillarForces(IN const int pillarInd, OUT double result[NDIM]);

	/**
	 * Gets the current absolute force (N) of a pillar.
	 *
	 * @param[in] pillarInd The index of the pillar.
	 * @param[out] result The absolute force (N) of the pillar.
	 *
	 * @return True if the pillar index is valid; false otherwise.
	 */
	bool getPillarForceAbs(IN const int pillarInd, OUT double* result);

	/**
	 * Gets the current normal (Z) force (N) of a pillar.
	 *
	 * @param[in] pillarInd The index of the pillar.
	 * @param[out] result The normal (Z) force (N) of the pillar.
	 *
	 * @return True if the pillar index is valid; false otherwise.
	 */
	bool getPillarForceN(IN const int pillarInd, OUT double* result);

	/**
	 * Gets the current tangential (XY) force (N) of a pillar.
	 *
	 * @param[in] pillarInd The index of the pillar.
	 * @param[out] result The tangential (XY) force (N) of the pillar.
	 *
	 * @return True if the pillar index is valid; false otherwise.
	 */
	bool getPillarForceT(IN const int pillarInd, OUT double* result);

	/**
	 * Gets the current timestamp in us.
	 *
	 * @return The current timestamp in us.
	 */
	uint64_t getTimestamp_us(void);

	/**
	 * Gets whether the sensor is in contact.
	 *
	 * @return True if at least one pillar is in contact; false otherwise.
	 */
	bool isSensorInContact(void);

};
