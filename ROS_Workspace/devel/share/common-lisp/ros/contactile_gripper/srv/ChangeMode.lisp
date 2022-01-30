; Auto-generated. Do not edit!


(cl:in-package contactile_gripper-srv)


;//! \htmlinclude ChangeMode-request.msg.html

(cl:defclass <ChangeMode-request> (roslisp-msg-protocol:ros-message)
  ((mode
    :reader mode
    :initarg :mode
    :type cl:string
    :initform ""))
)

(cl:defclass ChangeMode-request (<ChangeMode-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChangeMode-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChangeMode-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name contactile_gripper-srv:<ChangeMode-request> is deprecated: use contactile_gripper-srv:ChangeMode-request instead.")))

(cl:ensure-generic-function 'mode-val :lambda-list '(m))
(cl:defmethod mode-val ((m <ChangeMode-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader contactile_gripper-srv:mode-val is deprecated.  Use contactile_gripper-srv:mode instead.")
  (mode m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChangeMode-request>) ostream)
  "Serializes a message object of type '<ChangeMode-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'mode))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'mode))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChangeMode-request>) istream)
  "Deserializes a message object of type '<ChangeMode-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mode) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'mode) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChangeMode-request>)))
  "Returns string type for a service object of type '<ChangeMode-request>"
  "contactile_gripper/ChangeModeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeMode-request)))
  "Returns string type for a service object of type 'ChangeMode-request"
  "contactile_gripper/ChangeModeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChangeMode-request>)))
  "Returns md5sum for a message object of type '<ChangeMode-request>"
  "e1606556eb3ead28777d8c5a5ac25eb4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChangeMode-request)))
  "Returns md5sum for a message object of type 'ChangeMode-request"
  "e1606556eb3ead28777d8c5a5ac25eb4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChangeMode-request>)))
  "Returns full string definition for message of type '<ChangeMode-request>"
  (cl:format cl:nil "string mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChangeMode-request)))
  "Returns full string definition for message of type 'ChangeMode-request"
  (cl:format cl:nil "string mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChangeMode-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'mode))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChangeMode-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ChangeMode-request
    (cl:cons ':mode (mode msg))
))
;//! \htmlinclude ChangeMode-response.msg.html

(cl:defclass <ChangeMode-response> (roslisp-msg-protocol:ros-message)
  ((response
    :reader response
    :initarg :response
    :type cl:string
    :initform ""))
)

(cl:defclass ChangeMode-response (<ChangeMode-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChangeMode-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChangeMode-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name contactile_gripper-srv:<ChangeMode-response> is deprecated: use contactile_gripper-srv:ChangeMode-response instead.")))

(cl:ensure-generic-function 'response-val :lambda-list '(m))
(cl:defmethod response-val ((m <ChangeMode-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader contactile_gripper-srv:response-val is deprecated.  Use contactile_gripper-srv:response instead.")
  (response m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChangeMode-response>) ostream)
  "Serializes a message object of type '<ChangeMode-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'response))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'response))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChangeMode-response>) istream)
  "Deserializes a message object of type '<ChangeMode-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'response) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'response) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChangeMode-response>)))
  "Returns string type for a service object of type '<ChangeMode-response>"
  "contactile_gripper/ChangeModeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeMode-response)))
  "Returns string type for a service object of type 'ChangeMode-response"
  "contactile_gripper/ChangeModeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChangeMode-response>)))
  "Returns md5sum for a message object of type '<ChangeMode-response>"
  "e1606556eb3ead28777d8c5a5ac25eb4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChangeMode-response)))
  "Returns md5sum for a message object of type 'ChangeMode-response"
  "e1606556eb3ead28777d8c5a5ac25eb4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChangeMode-response>)))
  "Returns full string definition for message of type '<ChangeMode-response>"
  (cl:format cl:nil "string response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChangeMode-response)))
  "Returns full string definition for message of type 'ChangeMode-response"
  (cl:format cl:nil "string response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChangeMode-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'response))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChangeMode-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ChangeMode-response
    (cl:cons ':response (response msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ChangeMode)))
  'ChangeMode-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ChangeMode)))
  'ChangeMode-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeMode)))
  "Returns string type for a service object of type '<ChangeMode>"
  "contactile_gripper/ChangeMode")