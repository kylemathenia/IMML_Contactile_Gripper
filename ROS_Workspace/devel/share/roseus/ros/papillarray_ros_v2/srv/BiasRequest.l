;; Auto-generated. Do not edit!


(when (boundp 'papillarray_ros_v2::BiasRequest)
  (if (not (find-package "PAPILLARRAY_ROS_V2"))
    (make-package "PAPILLARRAY_ROS_V2"))
  (shadow 'BiasRequest (find-package "PAPILLARRAY_ROS_V2")))
(unless (find-package "PAPILLARRAY_ROS_V2::BIASREQUEST")
  (make-package "PAPILLARRAY_ROS_V2::BIASREQUEST"))
(unless (find-package "PAPILLARRAY_ROS_V2::BIASREQUESTREQUEST")
  (make-package "PAPILLARRAY_ROS_V2::BIASREQUESTREQUEST"))
(unless (find-package "PAPILLARRAY_ROS_V2::BIASREQUESTRESPONSE")
  (make-package "PAPILLARRAY_ROS_V2::BIASREQUESTRESPONSE"))

(in-package "ROS")





(defclass papillarray_ros_v2::BiasRequestRequest
  :super ros::object
  :slots ())

(defmethod papillarray_ros_v2::BiasRequestRequest
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

(defclass papillarray_ros_v2::BiasRequestResponse
  :super ros::object
  :slots (_result ))

(defmethod papillarray_ros_v2::BiasRequestResponse
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

(defclass papillarray_ros_v2::BiasRequest
  :super ros::object
  :slots ())

(setf (get papillarray_ros_v2::BiasRequest :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get papillarray_ros_v2::BiasRequest :datatype-) "papillarray_ros_v2/BiasRequest")
(setf (get papillarray_ros_v2::BiasRequest :request) papillarray_ros_v2::BiasRequestRequest)
(setf (get papillarray_ros_v2::BiasRequest :response) papillarray_ros_v2::BiasRequestResponse)

(defmethod papillarray_ros_v2::BiasRequestRequest
  (:response () (instance papillarray_ros_v2::BiasRequestResponse :init)))

(setf (get papillarray_ros_v2::BiasRequestRequest :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get papillarray_ros_v2::BiasRequestRequest :datatype-) "papillarray_ros_v2/BiasRequestRequest")
(setf (get papillarray_ros_v2::BiasRequestRequest :definition-)
      "---
bool result

")

(setf (get papillarray_ros_v2::BiasRequestResponse :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get papillarray_ros_v2::BiasRequestResponse :datatype-) "papillarray_ros_v2/BiasRequestResponse")
(setf (get papillarray_ros_v2::BiasRequestResponse :definition-)
      "---
bool result

")



(provide :papillarray_ros_v2/BiasRequest "eb13ac1f1354ccecb7941ee8fa2192e8")


