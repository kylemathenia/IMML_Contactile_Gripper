;; Auto-generated. Do not edit!


(when (boundp 'contactile_gripper::StepperOff)
  (if (not (find-package "CONTACTILE_GRIPPER"))
    (make-package "CONTACTILE_GRIPPER"))
  (shadow 'StepperOff (find-package "CONTACTILE_GRIPPER")))
(unless (find-package "CONTACTILE_GRIPPER::STEPPEROFF")
  (make-package "CONTACTILE_GRIPPER::STEPPEROFF"))
(unless (find-package "CONTACTILE_GRIPPER::STEPPEROFFREQUEST")
  (make-package "CONTACTILE_GRIPPER::STEPPEROFFREQUEST"))
(unless (find-package "CONTACTILE_GRIPPER::STEPPEROFFRESPONSE")
  (make-package "CONTACTILE_GRIPPER::STEPPEROFFRESPONSE"))

(in-package "ROS")





(defclass contactile_gripper::StepperOffRequest
  :super ros::object
  :slots (_mode ))

(defmethod contactile_gripper::StepperOffRequest
  (:init
   (&key
    ((:mode __mode) "")
    )
   (send-super :init)
   (setq _mode (string __mode))
   self)
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:serialization-length
   ()
   (+
    ;; string _mode
    4 (length _mode)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _mode
       (write-long (length _mode) s) (princ _mode s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _mode
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _mode (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass contactile_gripper::StepperOffResponse
  :super ros::object
  :slots (_response ))

(defmethod contactile_gripper::StepperOffResponse
  (:init
   (&key
    ((:response __response) "")
    )
   (send-super :init)
   (setq _response (string __response))
   self)
  (:response
   (&optional __response)
   (if __response (setq _response __response)) _response)
  (:serialization-length
   ()
   (+
    ;; string _response
    4 (length _response)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _response
       (write-long (length _response) s) (princ _response s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _response
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _response (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass contactile_gripper::StepperOff
  :super ros::object
  :slots ())

(setf (get contactile_gripper::StepperOff :md5sum-) "e1606556eb3ead28777d8c5a5ac25eb4")
(setf (get contactile_gripper::StepperOff :datatype-) "contactile_gripper/StepperOff")
(setf (get contactile_gripper::StepperOff :request) contactile_gripper::StepperOffRequest)
(setf (get contactile_gripper::StepperOff :response) contactile_gripper::StepperOffResponse)

(defmethod contactile_gripper::StepperOffRequest
  (:response () (instance contactile_gripper::StepperOffResponse :init)))

(setf (get contactile_gripper::StepperOffRequest :md5sum-) "e1606556eb3ead28777d8c5a5ac25eb4")
(setf (get contactile_gripper::StepperOffRequest :datatype-) "contactile_gripper/StepperOffRequest")
(setf (get contactile_gripper::StepperOffRequest :definition-)
      "string mode
---
string response
")

(setf (get contactile_gripper::StepperOffResponse :md5sum-) "e1606556eb3ead28777d8c5a5ac25eb4")
(setf (get contactile_gripper::StepperOffResponse :datatype-) "contactile_gripper/StepperOffResponse")
(setf (get contactile_gripper::StepperOffResponse :definition-)
      "string mode
---
string response
")



(provide :contactile_gripper/StepperOff "e1606556eb3ead28777d8c5a5ac25eb4")


