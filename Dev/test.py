#!/usr/bin/env python3

import cv2
import numpy as np
import time

def main():
    start_time = time.perf_counter()
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame.
        # This method returns True/False as well as the video frame.
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        duration = time.perf_counter() - start_time
        if duration > 5:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()