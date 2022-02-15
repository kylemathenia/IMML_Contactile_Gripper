; Auto-generated. Do not edit!


(cl:in-package papillarray_ros_v2-msg)


;//! \htmlinclude PillarState.msg.html

(cl:defclass <PillarState> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (dX
    :reader dX
    :initarg :dX
    :type cl:float
    :initform 0.0)
   (dY
    :reader dY
    :initarg :dY
    :type cl:float
    :initform 0.0)
   (dZ
    :reader dZ
    :initarg :dZ
    :type cl:float
    :initform 0.0)
   (fX
    :reader fX
    :initarg :fX
    :type cl:float
    :initform 0.0)
   (fY
    :reader fY
    :initarg :fY
    :type cl:float
    :initform 0.0)
   (fZ
    :reader fZ
    :initarg :fZ
    :type cl:float
    :initform 0.0)
   (in_contact
    :reader in_contact
    :initarg :in_contact
    :type cl:boolean
    :initform cl:nil)
   (slip_state
    :reader slip_state
    :initarg :slip_state
    :type cl:integer
    :initform 0))
)

(cl:defclass PillarState (<PillarState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PillarState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PillarState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name papillarray_ros_v2-msg:<PillarState> is deprecated: use papillarray_ros_v2-msg:PillarState instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <PillarState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-msg:header-val is deprecated.  Use papillarray_ros_v2-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <PillarState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-msg:id-val is deprecated.  Use papillarray_ros_v2-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'dX-val :lambda-list '(m))
(cl:defmethod dX-val ((m <PillarState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-msg:dX-val is deprecated.  Use papillarray_ros_v2-msg:dX instead.")
  (dX m))

(cl:ensure-generic-function 'dY-val :lambda-list '(m))
(cl:defmethod dY-val ((m <PillarState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-msg:dY-val is deprecated.  Use papillarray_ros_v2-msg:dY instead.")
  (dY m))

(cl:ensure-generic-function 'dZ-val :lambda-list '(m))
(cl:defmethod dZ-val ((m <PillarState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-msg:dZ-val is deprecated.  Use papillarray_ros_v2-msg:dZ instead.")
  (dZ m))

(cl:ensure-generic-function 'fX-val :lambda-list '(m))
(cl:defmethod fX-val ((m <PillarState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-msg:fX-val is deprecated.  Use papillarray_ros_v2-msg:fX instead.")
  (fX m))

(cl:ensure-generic-function 'fY-val :lambda-list '(m))
(cl:defmethod fY-val ((m <PillarState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-msg:fY-val is deprecated.  Use papillarray_ros_v2-msg:fY instead.")
  (fY m))

(cl:ensure-generic-function 'fZ-val :lambda-list '(m))
(cl:defmethod fZ-val ((m <PillarState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-msg:fZ-val is deprecated.  Use papillarray_ros_v2-msg:fZ instead.")
  (fZ m))

(cl:ensure-generic-function 'in_contact-val :lambda-list '(m))
(cl:defmethod in_contact-val ((m <PillarState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-msg:in_contact-val is deprecated.  Use papillarray_ros_v2-msg:in_contact instead.")
  (in_contact m))

(cl:ensure-generic-function 'slip_state-val :lambda-list '(m))
(cl:defmethod slip_state-val ((m <PillarState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-msg:slip_state-val is deprecated.  Use papillarray_ros_v2-msg:slip_state instead.")
  (slip_state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PillarState>) ostream)
  "Serializes a message object of type '<PillarState>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dY))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dZ))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'fX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'fY))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'fZ))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'in_contact) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'slip_state)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PillarState>) istream)
  "Deserializes a message object of type '<PillarState>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dX) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dY) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dZ) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'fX) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'fY) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'fZ) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'in_contact) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'slip_state) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PillarState>)))
  "Returns string type for a message object of type '<PillarState>"
  "papillarray_ros_v2/PillarState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PillarState)))
  "Returns string type for a message object of type 'PillarState"
  "papillarray_ros_v2/PillarState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PillarState>)))
  "Returns md5sum for a message object of type '<PillarState>"
  "f75cd8df721a8e7158c9671c32de7f98")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PillarState)))
  "Returns md5sum for a message object of type 'PillarState"
  "f75cd8df721a8e7158c9671c32de7f98")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PillarState>)))
  "Returns full string definition for message of type '<PillarState>"
  (cl:format cl:nil "Header header~%int32 id~%float32 dX~%float32 dY~%float32 dZ~%float32 fX~%float32 fY~%float32 fZ~%bool in_contact~%int32 slip_state~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PillarState)))
  "Returns full string definition for message of type 'PillarState"
  (cl:format cl:nil "Header header~%int32 id~%float32 dX~%float32 dY~%float32 dZ~%float32 fX~%float32 fY~%float32 fZ~%bool in_contact~%int32 slip_state~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PillarState>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
     4
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PillarState>))
  "Converts a ROS message object to a list"
  (cl:list 'PillarState
    (cl:cons ':header (header msg))
    (cl:cons ':id (id msg))
    (cl:cons ':dX (dX msg))
    (cl:cons ':dY (dY msg))
    (cl:cons ':dZ (dZ msg))
    (cl:cons ':fX (fX msg))
    (cl:cons ':fY (fY msg))
    (cl:cons ':fZ (fZ msg))
    (cl:cons ':in_contact (in_contact msg))
    (cl:cons ':slip_state (slip_state msg))
))
