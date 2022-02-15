; Auto-generated. Do not edit!


(cl:in-package papillarray_ros_v2-srv)


;//! \htmlinclude StopSlipDetection-request.msg.html

(cl:defclass <StopSlipDetection-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass StopSlipDetection-request (<StopSlipDetection-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StopSlipDetection-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StopSlipDetection-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name papillarray_ros_v2-srv:<StopSlipDetection-request> is deprecated: use papillarray_ros_v2-srv:StopSlipDetection-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StopSlipDetection-request>) ostream)
  "Serializes a message object of type '<StopSlipDetection-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StopSlipDetection-request>) istream)
  "Deserializes a message object of type '<StopSlipDetection-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StopSlipDetection-request>)))
  "Returns string type for a service object of type '<StopSlipDetection-request>"
  "papillarray_ros_v2/StopSlipDetectionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StopSlipDetection-request)))
  "Returns string type for a service object of type 'StopSlipDetection-request"
  "papillarray_ros_v2/StopSlipDetectionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StopSlipDetection-request>)))
  "Returns md5sum for a message object of type '<StopSlipDetection-request>"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StopSlipDetection-request)))
  "Returns md5sum for a message object of type 'StopSlipDetection-request"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StopSlipDetection-request>)))
  "Returns full string definition for message of type '<StopSlipDetection-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StopSlipDetection-request)))
  "Returns full string definition for message of type 'StopSlipDetection-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StopSlipDetection-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StopSlipDetection-request>))
  "Converts a ROS message object to a list"
  (cl:list 'StopSlipDetection-request
))
;//! \htmlinclude StopSlipDetection-response.msg.html

(cl:defclass <StopSlipDetection-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass StopSlipDetection-response (<StopSlipDetection-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StopSlipDetection-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StopSlipDetection-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name papillarray_ros_v2-srv:<StopSlipDetection-response> is deprecated: use papillarray_ros_v2-srv:StopSlipDetection-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <StopSlipDetection-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-srv:result-val is deprecated.  Use papillarray_ros_v2-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StopSlipDetection-response>) ostream)
  "Serializes a message object of type '<StopSlipDetection-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StopSlipDetection-response>) istream)
  "Deserializes a message object of type '<StopSlipDetection-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StopSlipDetection-response>)))
  "Returns string type for a service object of type '<StopSlipDetection-response>"
  "papillarray_ros_v2/StopSlipDetectionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StopSlipDetection-response)))
  "Returns string type for a service object of type 'StopSlipDetection-response"
  "papillarray_ros_v2/StopSlipDetectionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StopSlipDetection-response>)))
  "Returns md5sum for a message object of type '<StopSlipDetection-response>"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StopSlipDetection-response)))
  "Returns md5sum for a message object of type 'StopSlipDetection-response"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StopSlipDetection-response>)))
  "Returns full string definition for message of type '<StopSlipDetection-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StopSlipDetection-response)))
  "Returns full string definition for message of type 'StopSlipDetection-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StopSlipDetection-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StopSlipDetection-response>))
  "Converts a ROS message object to a list"
  (cl:list 'StopSlipDetection-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'StopSlipDetection)))
  'StopSlipDetection-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'StopSlipDetection)))
  'StopSlipDetection-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StopSlipDetection)))
  "Returns string type for a service object of type '<StopSlipDetection>"
  "papillarray_ros_v2/StopSlipDetection")