;; Auto-generated. Do not edit!


(when (boundp 'papillarray_ros_v2::SensorState)
  (if (not (find-package "PAPILLARRAY_ROS_V2"))
    (make-package "PAPILLARRAY_ROS_V2"))
  (shadow 'SensorState (find-package "PAPILLARRAY_ROS_V2")))
(unless (find-package "PAPILLARRAY_ROS_V2::SENSORSTATE")
  (make-package "PAPILLARRAY_ROS_V2::SENSORSTATE"))

(in-package "ROS")
;;//! \htmlinclude SensorState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass papillarray_ros_v2::SensorState
  :super ros::object
  :slots (_header _tus _pillars _gfX _gfY _gfZ _gtX _gtY _gtZ _friction_est _target_grip_force _is_sd_active _is_ref_loaded _is_contact ))

(defmethod papillarray_ros_v2::SensorState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:tus __tus) 0)
    ((:pillars __pillars) (let (r) (dotimes (i 0) (push (instance papillarray_ros_v2::PillarState :init) r)) r))
    ((:gfX __gfX) 0.0)
    ((:gfY __gfY) 0.0)
    ((:gfZ __gfZ) 0.0)
    ((:gtX __gtX) 0.0)
    ((:gtY __gtY) 0.0)
    ((:gtZ __gtZ) 0.0)
    ((:friction_est __friction_est) 0.0)
    ((:target_grip_force __target_grip_force) 0.0)
    ((:is_sd_active __is_sd_active) nil)
    ((:is_ref_loaded __is_ref_loaded) nil)
    ((:is_contact __is_contact) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _tus (round __tus))
   (setq _pillars __pillars)
   (setq _gfX (float __gfX))
   (setq _gfY (float __gfY))
   (setq _gfZ (float __gfZ))
   (setq _gtX (float __gtX))
   (setq _gtY (float __gtY))
   (setq _gtZ (float __gtZ))
   (setq _friction_est (float __friction_est))
   (setq _target_grip_force (float __target_grip_force))
   (setq _is_sd_active __is_sd_active)
   (setq _is_ref_loaded __is_ref_loaded)
   (setq _is_contact __is_contact)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:tus
   (&optional __tus)
   (if __tus (setq _tus __tus)) _tus)
  (:pillars
   (&rest __pillars)
   (if (keywordp (car __pillars))
       (send* _pillars __pillars)
     (progn
       (if __pillars (setq _pillars (car __pillars)))
       _pillars)))
  (:gfX
   (&optional __gfX)
   (if __gfX (setq _gfX __gfX)) _gfX)
  (:gfY
   (&optional __gfY)
   (if __gfY (setq _gfY __gfY)) _gfY)
  (:gfZ
   (&optional __gfZ)
   (if __gfZ (setq _gfZ __gfZ)) _gfZ)
  (:gtX
   (&optional __gtX)
   (if __gtX (setq _gtX __gtX)) _gtX)
  (:gtY
   (&optional __gtY)
   (if __gtY (setq _gtY __gtY)) _gtY)
  (:gtZ
   (&optional __gtZ)
   (if __gtZ (setq _gtZ __gtZ)) _gtZ)
  (:friction_est
   (&optional __friction_est)
   (if __friction_est (setq _friction_est __friction_est)) _friction_est)
  (:target_grip_force
   (&optional __target_grip_force)
   (if __target_grip_force (setq _target_grip_force __target_grip_force)) _target_grip_force)
  (:is_sd_active
   (&optional __is_sd_active)
   (if __is_sd_active (setq _is_sd_active __is_sd_active)) _is_sd_active)
  (:is_ref_loaded
   (&optional __is_ref_loaded)
   (if __is_ref_loaded (setq _is_ref_loaded __is_ref_loaded)) _is_ref_loaded)
  (:is_contact
   (&optional __is_contact)
   (if __is_contact (setq _is_contact __is_contact)) _is_contact)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int64 _tus
    8
    ;; papillarray_ros_v2/PillarState[] _pillars
    (apply #'+ (send-all _pillars :serialization-length)) 4
    ;; float32 _gfX
    4
    ;; float32 _gfY
    4
    ;; float32 _gfZ
    4
    ;; float32 _gtX
    4
    ;; float32 _gtY
    4
    ;; float32 _gtZ
    4
    ;; float32 _friction_est
    4
    ;; float32 _target_grip_force
    4
    ;; bool _is_sd_active
    1
    ;; bool _is_ref_loaded
    1
    ;; bool _is_contact
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int64 _tus
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _tus (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _tus) (= (length (_tus . bv)) 2)) ;; bignum
              (write-long (ash (elt (_tus . bv) 0) 0) s)
              (write-long (ash (elt (_tus . bv) 1) -1) s))
             ((and (class _tus) (= (length (_tus . bv)) 1)) ;; big1
              (write-long (elt (_tus . bv) 0) s)
              (write-long (if (>= _tus 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _tus s)(write-long (if (>= _tus 0) 0 #xffffffff) s)))
     ;; papillarray_ros_v2/PillarState[] _pillars
     (write-long (length _pillars) s)
     (dolist (elem _pillars)
       (send elem :serialize s)
       )
     ;; float32 _gfX
       (sys::poke _gfX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gfY
       (sys::poke _gfY (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gfZ
       (sys::poke _gfZ (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gtX
       (sys::poke _gtX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gtY
       (sys::poke _gtY (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gtZ
       (sys::poke _gtZ (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _friction_est
       (sys::poke _friction_est (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _target_grip_force
       (sys::poke _target_grip_force (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _is_sd_active
       (if _is_sd_active (write-byte -1 s) (write-byte 0 s))
     ;; bool _is_ref_loaded
       (if _is_ref_loaded (write-byte -1 s) (write-byte 0 s))
     ;; bool _is_contact
       (if _is_contact (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int64 _tus
#+(or :alpha :irix6 :x86_64)
      (setf _tus (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _tus (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; papillarray_ros_v2/PillarState[] _pillars
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pillars (let (r) (dotimes (i n) (push (instance papillarray_ros_v2::PillarState :init) r)) r))
     (dolist (elem- _pillars)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; float32 _gfX
     (setq _gfX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gfY
     (setq _gfY (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gfZ
     (setq _gfZ (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gtX
     (setq _gtX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gtY
     (setq _gtY (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gtZ
     (setq _gtZ (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _friction_est
     (setq _friction_est (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _target_grip_force
     (setq _target_grip_force (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _is_sd_active
     (setq _is_sd_active (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _is_ref_loaded
     (setq _is_ref_loaded (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _is_contact
     (setq _is_contact (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get papillarray_ros_v2::SensorState :md5sum-) "5d7c28da3453a417882d03f775d18f22")
(setf (get papillarray_ros_v2::SensorState :datatype-) "papillarray_ros_v2/SensorState")
(setf (get papillarray_ros_v2::SensorState :definition-)
      "Header header
int64 tus
PillarState[] pillars
float32 gfX
float32 gfY
float32 gfZ
float32 gtX
float32 gtY
float32 gtZ
float32 friction_est
float32 target_grip_force
bool is_sd_active
bool is_ref_loaded
bool is_contact

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

================================================================================
MSG: papillarray_ros_v2/PillarState
Header header
int32 id
float32 dX
float32 dY
float32 dZ
float32 fX
float32 fY
float32 fZ
bool in_contact
int32 slip_state

")



(provide :papillarray_ros_v2/SensorState "5d7c28da3453a417882d03f775d18f22")


