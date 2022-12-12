// PTSDK_CPP_LIB.h
#pragma once

#ifdef PTSDK_CPP_LIB_EXPORTS
#define PTSDK_CPP_LIB_API __declspec(dllexport)
#else
#define PTSDK_CPP_LIB_API __declspec(dllimport)
#endif

#include <stdint.h>