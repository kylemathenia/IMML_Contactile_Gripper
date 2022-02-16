;; Auto-generated. Do not edit!


(when (boundp 'contactile_gripper::GripperChangeMode)
  (if (not (find-package "CONTACTILE_GRIPPER"))
    (make-package "CONTACTILE_GRIPPER"))
  (shadow 'GripperChangeMode (find-package "CONTACTILE_GRIPPER")))
(unless (find-package "CONTACTILE_GRIPPER::GRIPPERCHANGEMODE")
  (make-package "CONTACTILE_GRIPPER::GRIPPERCHANGEMODE"))
(unless (find-package "CONTACTILE_GRIPPER::GRIPPERCHANGEMODEREQUEST")
  (make-package "CONTACTILE_GRIPPER::GRIPPERCHANGEMODEREQUEST"))
(unless (find-package "CONTACTILE_GRIPPER::GRIPPERCHANGEMODERESPONSE")
  (make-package "CONTACTILE_GRIPPER::GRIPPERCHANGEMODERESPONSE"))

(in-package "ROS")





(defclass contactile_gripper::GripperChangeModeRequest
  :super ros::object
  :slots (_mode ))

(defmethod contactile_gripper::GripperChangeModeRequest
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

(defclass contactile_gripper::GripperChangeModeResponse
  :super ros::object
  :slots (_response ))

(defmethod contactile_gripper::GripperChangeModeResponse
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

(defclass contactile_gripper::GripperChangeMode
  :super ros::object
  :slots ())

(setf (get contactile_gripper::GripperChangeMode :md5sum-) "e1606556eb3ead28777d8c5a5ac25eb4")
(setf (get contactile_gripper::GripperChangeMode :datatype-) "contactile_gripper/GripperChangeMode")
(setf (get contactile_gripper::GripperChangeMode :request) contactile_gripper::GripperChangeModeRequest)
(setf (get contactile_gripper::GripperChangeMode :response) contactile_gripper::GripperChangeModeResponse)

(defmethod contactile_gripper::GripperChangeModeRequest
  (:response () (instance contactile_gripper::GripperChangeModeResponse :init)))

(setf (get contactile_gripper::GripperChangeModeRequest :md5sum-) "e1606556eb3ead28777d8c5a5ac25eb4")
(setf (get contactile_gripper::GripperChangeModeRequest :datatype-) "contactile_gripper/GripperChangeModeRequest")
(setf (get contactile_gripper::GripperChangeModeRequest :definition-)
      "string mode
---
string response
")

(setf (get contactile_gripper::GripperChangeModeResponse :md5sum-) "e1606556eb3ead28777d8c5a5ac25eb4")
(setf (get contactile_gripper::GripperChangeModeResponse :datatype-) "contactile_gripper/GripperChangeModeResponse")
(setf (get contactile_gripper::GripperChangeModeResponse :definition-)
      "string mode
---
string response
")



(provide :contactile_gripper/GripperChangeMode "e1606556eb3ead28777d8c5a5ac25eb4")


