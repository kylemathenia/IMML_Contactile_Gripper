;; Auto-generated. Do not edit!


(when (boundp 'papillarray_ros_v2::PillarState)
  (if (not (find-package "PAPILLARRAY_ROS_V2"))
    (make-package "PAPILLARRAY_ROS_V2"))
  (shadow 'PillarState (find-package "PAPILLARRAY_ROS_V2")))
(unless (find-package "PAPILLARRAY_ROS_V2::PILLARSTATE")
  (make-package "PAPILLARRAY_ROS_V2::PILLARSTATE"))

(in-package "ROS")
;;//! \htmlinclude PillarState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass papillarray_ros_v2::PillarState
  :super ros::object
  :slots (_header _id _dX _dY _dZ _fX _fY _fZ _in_contact _slip_state ))

(defmethod papillarray_ros_v2::PillarState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:id __id) 0)
    ((:dX __dX) 0.0)
    ((:dY __dY) 0.0)
    ((:dZ __dZ) 0.0)
    ((:fX __fX) 0.0)
    ((:fY __fY) 0.0)
    ((:fZ __fZ) 0.0)
    ((:in_contact __in_contact) nil)
    ((:slip_state __slip_state) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _id (round __id))
   (setq _dX (float __dX))
   (setq _dY (float __dY))
   (setq _dZ (float __dZ))
   (setq _fX (float __fX))
   (setq _fY (float __fY))
   (setq _fZ (float __fZ))
   (setq _in_contact __in_contact)
   (setq _slip_state (round __slip_state))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:dX
   (&optional __dX)
   (if __dX (setq _dX __dX)) _dX)
  (:dY
   (&optional __dY)
   (if __dY (setq _dY __dY)) _dY)
  (:dZ
   (&optional __dZ)
   (if __dZ (setq _dZ __dZ)) _dZ)
  (:fX
   (&optional __fX)
   (if __fX (setq _fX __fX)) _fX)
  (:fY
   (&optional __fY)
   (if __fY (setq _fY __fY)) _fY)
  (:fZ
   (&optional __fZ)
   (if __fZ (setq _fZ __fZ)) _fZ)
  (:in_contact
   (&optional __in_contact)
   (if __in_contact (setq _in_contact __in_contact)) _in_contact)
  (:slip_state
   (&optional __slip_state)
   (if __slip_state (setq _slip_state __slip_state)) _slip_state)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _id
    4
    ;; float32 _dX
    4
    ;; float32 _dY
    4
    ;; float32 _dZ
    4
    ;; float32 _fX
    4
    ;; float32 _fY
    4
    ;; float32 _fZ
    4
    ;; bool _in_contact
    1
    ;; int32 _slip_state
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _id
       (write-long _id s)
     ;; float32 _dX
       (sys::poke _dX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _dY
       (sys::poke _dY (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _dZ
       (sys::poke _dZ (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _fX
       (sys::poke _fX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _fY
       (sys::poke _fY (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _fZ
       (sys::poke _fZ (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _in_contact
       (if _in_contact (write-byte -1 s) (write-byte 0 s))
     ;; int32 _slip_state
       (write-long _slip_state s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _dX
     (setq _dX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _dY
     (setq _dY (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _dZ
     (setq _dZ (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _fX
     (setq _fX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _fY
     (setq _fY (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _fZ
     (setq _fZ (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _in_contact
     (setq _in_contact (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int32 _slip_state
     (setq _slip_state (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get papillarray_ros_v2::PillarState :md5sum-) "f75cd8df721a8e7158c9671c32de7f98")
(setf (get papillarray_ros_v2::PillarState :datatype-) "papillarray_ros_v2/PillarState")
(setf (get papillarray_ros_v2::PillarState :definition-)
      "Header header
int32 id
float32 dX
float32 dY
float32 dZ
float32 fX
float32 fY
float32 fZ
bool in_contact
int32 slip_state

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :papillarray_ros_v2/PillarState "f75cd8df721a8e7158c9671c32de7f98")


