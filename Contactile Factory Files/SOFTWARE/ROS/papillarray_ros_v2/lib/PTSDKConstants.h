#ifndef PTSDKCONTANTS_H
#define PTSDKCONTANTS_H

/* Input and output parameters */

#define IN					// Indicates that a parameter is an input parameter.
#define OUT					// Indicates that a parameter is an output parameter.

/* Constants related to the data packet */

#define STARTBYTE0 		0x55		// The first byte of the start packet
#define STARTBYTE1 		0x66		// The second byte of the start packet
#define STARTBYTE2 		0x77		// The third byte of the start packet
#define STARTBYTE3 		0x88		// The fourth byte of the start packet
#define ENDBYTE0		0xAA		// The first byte of the end packet
#define ENDBYTE1		0xBB		// The second byte of the end packet
#define ENDBYTE2		0xCC		// The third byte of the end packet
#define ENDBYTE3		0xDD		// The fourth byte of the end packet

/* Constants related to dimensions*/

#define X_IND			0		// The index of the X-dimension.
#define Y_IND			1		// The index of the Y-dimension.
#define Z_IND			2		// The index of the Z-dimension.
#define NDIM			3		// The number of dimensions

/* Constants related to sensor and pillars */

#define MAX_NSENSOR		4		// The maximum number of sensors connected to the communication hub
#define MAX_NPILLAR		100		// The maximum number of pillars in a sensor

/* Constants related to slip detection and friction estimation */

#define CONTACT_THRESH		0.5		// Normal force threshold for contact
#define INELIGIBLE		-2		// Slip state: pillar was not in contact when slip detection started
#define CONTACT_AT_START	1		// Slip state: pillar was in contact when slip detection started
#define LOST_CONTACT		-1		// Slip state: pillar was in contact when slip detection started, but has lost contact
#define TLOADING		2		// Slip state: pillar was in contact when slip detection started and is being loaded tangentially
#define SLIPPED			3		// Slip state: pillar was in contact when slip detection started and has slipped
#define NOFRICTIONEST		-1		// Value of friction estimate when there is no friction estimate

/* Constants related to Controller sampling rate */

#define SAMP_RATE_100		100		// Constant representing 100 Hz sampling rate
#define SAMP_RATE_250		250		// Constant representing 250 Hz sampling rate
#define SAMP_RATE_500		500		// Constant representing 500 Hz sampling rate
#define SAMP_RATE_1000		1000		// Constant representing 1000 Hz sampling rate

/* ----------------------------- */

#define ISDEBUGOUTPUT		0

#endif
