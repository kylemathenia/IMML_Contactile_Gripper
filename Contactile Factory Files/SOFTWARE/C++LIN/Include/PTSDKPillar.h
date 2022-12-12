#ifndef PTSDKPILLAR_H
#define PTSDKPILLAR_H
#endif

#ifdef _WIN32
#ifndef PTSDK_CPP_LIB_H
#include "PTSDK_CPP_LIB.h"
#endif
#endif

#ifndef PTSDKCONSTANTS_H
#include "PTSDKConstants.h"
#endif

#include <stdint.h>

/** \brief The PTSDKPillar class describes a single Pillar of the PapillArray Tactile Sensor.
 *
 * The PTSDKPillar class describes a single Pillar of the  PapillArray sensor.
 *
 * @author Contactile Pty Ltd
 * @version June 2021
 */
#ifdef _WIN32
class PTSDK_CPP_LIB_API PTSDKPillar {
#else
class PTSDKPillar {
#endif

private:

	uint64_t timestamps_us;		// Timestamp of current sample in micro seconds
	double displacementVals[NDIM];	// 3D displacement values
	double forceVals[NDIM];		// 3D force values

public:

	PTSDKPillar(void); // Default constructor.

	void addSample(IN const float newForceVals[NDIM], IN const float newDisplacementVals[NDIM], IN const uint64_t timesstamp_us);

	uint64_t getTimeSample_us(void);		// Gets the current time sample in us.
	void getDisplacement(OUT double result[NDIM]); 	// Gets the current X, Y and Z displacement of the pillar tip.
	void getForce(OUT double result[NDIM]); 	// Gets the current X, Y and Z force on the pillar tip.
	double getForceAbs(void); 	// Gets the current absolute force on the pillar tip.
	double getForceN(void); 	// Gets the current normal (Z) force on the pillar tip.
	double getForceT(void); 	// Gets the current tangential (XY) force on the pillar tip
	bool isInContact(void); 	// Gets whether the pillar normal force exceeds the threshold for contact
};
