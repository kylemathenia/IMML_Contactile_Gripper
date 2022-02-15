;; Auto-generated. Do not edit!


(when (boundp 'papillarray_ros_v2::StartSlipDetection)
  (if (not (find-package "PAPILLARRAY_ROS_V2"))
    (make-package "PAPILLARRAY_ROS_V2"))
  (shadow 'StartSlipDetection (find-package "PAPILLARRAY_ROS_V2")))
(unless (find-package "PAPILLARRAY_ROS_V2::STARTSLIPDETECTION")
  (make-package "PAPILLARRAY_ROS_V2::STARTSLIPDETECTION"))
(unless (find-package "PAPILLARRAY_ROS_V2::STARTSLIPDETECTIONREQUEST")
  (make-package "PAPILLARRAY_ROS_V2::STARTSLIPDETECTIONREQUEST"))
(unless (find-package "PAPILLARRAY_ROS_V2::STARTSLIPDETECTIONRESPONSE")
  (make-package "PAPILLARRAY_ROS_V2::STARTSLIPDETECTIONRESPONSE"))

(in-package "ROS")





(defclass papillarray_ros_v2::StartSlipDetectionRequest
  :super ros::object
  :slots ())

(defmethod papillarray_ros_v2::StartSlipDetectionRequest
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

(defclass papillarray_ros_v2::StartSlipDetectionResponse
  :super ros::object
  :slots (_result ))

(defmethod papillarray_ros_v2::StartSlipDetectionResponse
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

(defclass papillarray_ros_v2::StartSlipDetection
  :super ros::object
  :slots ())

(setf (get papillarray_ros_v2::StartSlipDetection :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get papillarray_ros_v2::StartSlipDetection :datatype-) "papillarray_ros_v2/StartSlipDetection")
(setf (get papillarray_ros_v2::StartSlipDetection :request) papillarray_ros_v2::StartSlipDetectionRequest)
(setf (get papillarray_ros_v2::StartSlipDetection :response) papillarray_ros_v2::StartSlipDetectionResponse)

(defmethod papillarray_ros_v2::StartSlipDetectionRequest
  (:response () (instance papillarray_ros_v2::StartSlipDetectionResponse :init)))

(setf (get papillarray_ros_v2::StartSlipDetectionRequest :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get papillarray_ros_v2::StartSlipDetectionRequest :datatype-) "papillarray_ros_v2/StartSlipDetectionRequest")
(setf (get papillarray_ros_v2::StartSlipDetectionRequest :definition-)
      "---
bool result

")

(setf (get papillarray_ros_v2::StartSlipDetectionResponse :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get papillarray_ros_v2::StartSlipDetectionResponse :datatype-) "papillarray_ros_v2/StartSlipDetectionResponse")
(setf (get papillarray_ros_v2::StartSlipDetectionResponse :definition-)
      "---
bool result

")



(provide :papillarray_ros_v2/StartSlipDetection "eb13ac1f1354ccecb7941ee8fa2192e8")


