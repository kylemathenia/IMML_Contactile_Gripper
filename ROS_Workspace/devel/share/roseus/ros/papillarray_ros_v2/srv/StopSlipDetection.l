;; Auto-generated. Do not edit!


(when (boundp 'papillarray_ros_v2::StopSlipDetection)
  (if (not (find-package "PAPILLARRAY_ROS_V2"))
    (make-package "PAPILLARRAY_ROS_V2"))
  (shadow 'StopSlipDetection (find-package "PAPILLARRAY_ROS_V2")))
(unless (find-package "PAPILLARRAY_ROS_V2::STOPSLIPDETECTION")
  (make-package "PAPILLARRAY_ROS_V2::STOPSLIPDETECTION"))
(unless (find-package "PAPILLARRAY_ROS_V2::STOPSLIPDETECTIONREQUEST")
  (make-package "PAPILLARRAY_ROS_V2::STOPSLIPDETECTIONREQUEST"))
(unless (find-package "PAPILLARRAY_ROS_V2::STOPSLIPDETECTIONRESPONSE")
  (make-package "PAPILLARRAY_ROS_V2::STOPSLIPDETECTIONRESPONSE"))

(in-package "ROS")





(defclass papillarray_ros_v2::StopSlipDetectionRequest
  :super ros::object
  :slots ())

(defmethod papillarray_ros_v2::StopSlipDetectionRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass papillarray_ros_v2::StopSlipDetectionResponse
  :super ros::object
  :slots (_result ))

(defmethod papillarray_ros_v2::StopSlipDetectionResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass papillarray_ros_v2::StopSlipDetection
  :super ros::object
  :slots ())

(setf (get papillarray_ros_v2::StopSlipDetection :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get papillarray_ros_v2::StopSlipDetection :datatype-) "papillarray_ros_v2/StopSlipDetection")
(setf (get papillarray_ros_v2::StopSlipDetection :request) papillarray_ros_v2::StopSlipDetectionRequest)
(setf (get papillarray_ros_v2::StopSlipDetection :response) papillarray_ros_v2::StopSlipDetectionResponse)

(defmethod papillarray_ros_v2::StopSlipDetectionRequest
  (:response () (instance papillarray_ros_v2::StopSlipDetectionResponse :init)))

(setf (get papillarray_ros_v2::StopSlipDetectionRequest :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get papillarray_ros_v2::StopSlipDetectionRequest :datatype-) "papillarray_ros_v2/StopSlipDetectionRequest")
(setf (get papillarray_ros_v2::StopSlipDetectionRequest :definition-)
      "---
bool result

")

(setf (get papillarray_ros_v2::StopSlipDetectionResponse :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get papillarray_ros_v2::StopSlipDetectionResponse :datatype-) "papillarray_ros_v2/StopSlipDetectionResponse")
(setf (get papillarray_ros_v2::StopSlipDetectionResponse :definition-)
      "---
bool result

")



(provide :papillarray_ros_v2/StopSlipDetection "eb13ac1f1354ccecb7941ee8fa2192e8")


