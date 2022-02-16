; Auto-generated. Do not edit!


(cl:in-package contactile_gripper-srv)


;//! \htmlinclude StepperSetLimit-request.msg.html

(cl:defclass <StepperSetLimit-request> (roslisp-msg-protocol:ros-message)
  ((switch
    :reader switch
    :initarg :switch
    :type cl:string
    :initform "")
   (action
    :reader action
    :initarg :action
    :type cl:string
    :initform ""))
)

(cl:defclass StepperSetLimit-request (<StepperSetLimit-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StepperSetLimit-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StepperSetLimit-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name contactile_gripper-srv:<StepperSetLimit-request> is deprecated: use contactile_gripper-srv:StepperSetLimit-request instead.")))

(cl:ensure-generic-function 'switch-val :lambda-list '(m))
(cl:defmethod switch-val ((m <StepperSetLimit-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader contactile_gripper-srv:switch-val is deprecated.  Use contactile_gripper-srv:switch instead.")
  (switch m))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <StepperSetLimit-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader contactile_gripper-srv:action-val is deprecated.  Use contactile_gripper-srv:action instead.")
  (action m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StepperSetLimit-request>) ostream)
  "Serializes a message object of type '<StepperSetLimit-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'switch))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'switch))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'action))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'action))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StepperSetLimit-request>) istream)
  "Deserializes a message object of type '<StepperSetLimit-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'switch) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'switch) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'action) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'action) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StepperSetLimit-request>)))
  "Returns string type for a service object of type '<StepperSetLimit-request>"
  "contactile_gripper/StepperSetLimitRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StepperSetLimit-request)))
  "Returns string type for a service object of type 'StepperSetLimit-request"
  "contactile_gripper/StepperSetLimitRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StepperSetLimit-request>)))
  "Returns md5sum for a message object of type '<StepperSetLimit-request>"
  "5b0187267379b2af4b8e7118fa12084a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StepperSetLimit-request)))
  "Returns md5sum for a message object of type 'StepperSetLimit-request"
  "5b0187267379b2af4b8e7118fa12084a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StepperSetLimit-request>)))
  "Returns full string definition for message of type '<StepperSetLimit-request>"
  (cl:format cl:nil "string switch~%string action~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StepperSetLimit-request)))
  "Returns full string definition for message of type 'StepperSetLimit-request"
  (cl:format cl:nil "string switch~%string action~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StepperSetLimit-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'switch))
     4 (cl:length (cl:slot-value msg 'action))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StepperSetLimit-request>))
  "Converts a ROS message object to a list"
  (cl:list 'StepperSetLimit-request
    (cl:cons ':switch (switch msg))
    (cl:cons ':action (action msg))
))
;//! \htmlinclude StepperSetLimit-response.msg.html

(cl:defclass <StepperSetLimit-response> (roslisp-msg-protocol:ros-message)
  ((response
    :reader response
    :initarg :response
    :type cl:integer
    :initform 0))
)

(cl:defclass StepperSetLimit-response (<StepperSetLimit-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StepperSetLimit-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StepperSetLimit-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name contactile_gripper-srv:<StepperSetLimit-response> is deprecated: use contactile_gripper-srv:StepperSetLimit-response instead.")))

(cl:ensure-generic-function 'response-val :lambda-list '(m))
(cl:defmethod response-val ((m <StepperSetLimit-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader contactile_gripper-srv:response-val is deprecated.  Use contactile_gripper-srv:response instead.")
  (response m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StepperSetLimit-response>) ostream)
  "Serializes a message object of type '<StepperSetLimit-response>"
  (cl:let* ((signed (cl:slot-value msg 'response)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StepperSetLimit-response>) istream)
  "Deserializes a message object of type '<StepperSetLimit-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'response) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StepperSetLimit-response>)))
  "Returns string type for a service object of type '<StepperSetLimit-response>"
  "contactile_gripper/StepperSetLimitResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StepperSetLimit-response)))
  "Returns string type for a service object of type 'StepperSetLimit-response"
  "contactile_gripper/StepperSetLimitResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StepperSetLimit-response>)))
  "Returns md5sum for a message object of type '<StepperSetLimit-response>"
  "5b0187267379b2af4b8e7118fa12084a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StepperSetLimit-response)))
  "Returns md5sum for a message object of type 'StepperSetLimit-response"
  "5b0187267379b2af4b8e7118fa12084a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StepperSetLimit-response>)))
  "Returns full string definition for message of type '<StepperSetLimit-response>"
  (cl:format cl:nil "int64 response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StepperSetLimit-response)))
  "Returns full string definition for message of type 'StepperSetLimit-response"
  (cl:format cl:nil "int64 response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StepperSetLimit-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StepperSetLimit-response>))
  "Converts a ROS message object to a list"
  (cl:list 'StepperSetLimit-response
    (cl:cons ':response (response msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'StepperSetLimit)))
  'StepperSetLimit-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'StepperSetLimit)))
  'StepperSetLimit-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StepperSetLimit)))
  "Returns string type for a service object of type '<StepperSetLimit>"
  "contactile_gripper/StepperSetLimit")