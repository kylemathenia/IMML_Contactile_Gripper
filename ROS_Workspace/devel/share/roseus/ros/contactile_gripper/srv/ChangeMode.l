;; Auto-generated. Do not edit!


(when (boundp 'contactile_gripper::ChangeMode)
  (if (not (find-package "CONTACTILE_GRIPPER"))
    (make-package "CONTACTILE_GRIPPER"))
  (shadow 'ChangeMode (find-package "CONTACTILE_GRIPPER")))
(unless (find-package "CONTACTILE_GRIPPER::CHANGEMODE")
  (make-package "CONTACTILE_GRIPPER::CHANGEMODE"))
(unless (find-package "CONTACTILE_GRIPPER::CHANGEMODEREQUEST")
  (make-package "CONTACTILE_GRIPPER::CHANGEMODEREQUEST"))
(unless (find-package "CONTACTILE_GRIPPER::CHANGEMODERESPONSE")
  (make-package "CONTACTILE_GRIPPER::CHANGEMODERESPONSE"))

(in-package "ROS")





(defclass contactile_gripper::ChangeModeRequest
  :super ros::object
  :slots (_mode ))

(defmethod contactile_gripper::ChangeModeRequest
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

(defclass contactile_gripper::ChangeModeResponse
  :super ros::object
  :slots (_response ))

(defmethod contactile_gripper::ChangeModeResponse
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

(defclass contactile_gripper::ChangeMode
  :super ros::object
  :slots ())

(setf (get contactile_gripper::ChangeMode :md5sum-) "e1606556eb3ead28777d8c5a5ac25eb4")
(setf (get contactile_gripper::ChangeMode :datatype-) "contactile_gripper/ChangeMode")
(setf (get contactile_gripper::ChangeMode :request) contactile_gripper::ChangeModeRequest)
(setf (get contactile_gripper::ChangeMode :response) contactile_gripper::ChangeModeResponse)

(defmethod contactile_gripper::ChangeModeRequest
  (:response () (instance contactile_gripper::ChangeModeResponse :init)))

(setf (get contactile_gripper::ChangeModeRequest :md5sum-) "e1606556eb3ead28777d8c5a5ac25eb4")
(setf (get contactile_gripper::ChangeModeRequest :datatype-) "contactile_gripper/ChangeModeRequest")
(setf (get contactile_gripper::ChangeModeRequest :definition-)
      "string mode
---
string response
")

(setf (get contactile_gripper::ChangeModeResponse :md5sum-) "e1606556eb3ead28777d8c5a5ac25eb4")
(setf (get contactile_gripper::ChangeModeResponse :datatype-) "contactile_gripper/ChangeModeResponse")
(setf (get contactile_gripper::ChangeModeResponse :definition-)
      "string mode
---
string response
")



(provide :contactile_gripper/ChangeMode "e1606556eb3ead28777d8c5a5ac25eb4")


