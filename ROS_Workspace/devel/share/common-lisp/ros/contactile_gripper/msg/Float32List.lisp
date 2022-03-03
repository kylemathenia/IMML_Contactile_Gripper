; Auto-generated. Do not edit!


(cl:in-package contactile_gripper-msg)


;//! \htmlinclude Float32List.msg.html

(cl:defclass <Float32List> (roslisp-msg-protocol:ros-message)
  ((list
    :reader list
    :initarg :list
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass Float32List (<Float32List>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Float32List>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Float32List)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name contactile_gripper-msg:<Float32List> is deprecated: use contactile_gripper-msg:Float32List instead.")))

(cl:ensure-generic-function 'list-val :lambda-list '(m))
(cl:defmethod list-val ((m <Float32List>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader contactile_gripper-msg:list-val is deprecated.  Use contactile_gripper-msg:list instead.")
  (list m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Float32List>) ostream)
  "Serializes a message object of type '<Float32List>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'list))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'list))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Float32List>) istream)
  "Deserializes a message object of type '<Float32List>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'list) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'list)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Float32List>)))
  "Returns string type for a message object of type '<Float32List>"
  "contactile_gripper/Float32List")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Float32List)))
  "Returns string type for a message object of type 'Float32List"
  "contactile_gripper/Float32List")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Float32List>)))
  "Returns md5sum for a message object of type '<Float32List>"
  "f899bbf34605ab8c1065aaee8c9708ca")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Float32List)))
  "Returns md5sum for a message object of type 'Float32List"
  "f899bbf34605ab8c1065aaee8c9708ca")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Float32List>)))
  "Returns full string definition for message of type '<Float32List>"
  (cl:format cl:nil "float32[] list~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Float32List)))
  "Returns full string definition for message of type 'Float32List"
  (cl:format cl:nil "float32[] list~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Float32List>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'list) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Float32List>))
  "Converts a ROS message object to a list"
  (cl:list 'Float32List
    (cl:cons ':list (list msg))
))
