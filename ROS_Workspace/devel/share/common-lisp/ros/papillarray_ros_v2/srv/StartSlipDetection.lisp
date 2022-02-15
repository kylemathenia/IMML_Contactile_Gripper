; Auto-generated. Do not edit!


(cl:in-package papillarray_ros_v2-srv)


;//! \htmlinclude StartSlipDetection-request.msg.html

(cl:defclass <StartSlipDetection-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass StartSlipDetection-request (<StartSlipDetection-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StartSlipDetection-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StartSlipDetection-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name papillarray_ros_v2-srv:<StartSlipDetection-request> is deprecated: use papillarray_ros_v2-srv:StartSlipDetection-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StartSlipDetection-request>) ostream)
  "Serializes a message object of type '<StartSlipDetection-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StartSlipDetection-request>) istream)
  "Deserializes a message object of type '<StartSlipDetection-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StartSlipDetection-request>)))
  "Returns string type for a service object of type '<StartSlipDetection-request>"
  "papillarray_ros_v2/StartSlipDetectionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StartSlipDetection-request)))
  "Returns string type for a service object of type 'StartSlipDetection-request"
  "papillarray_ros_v2/StartSlipDetectionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StartSlipDetection-request>)))
  "Returns md5sum for a message object of type '<StartSlipDetection-request>"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StartSlipDetection-request)))
  "Returns md5sum for a message object of type 'StartSlipDetection-request"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StartSlipDetection-request>)))
  "Returns full string definition for message of type '<StartSlipDetection-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StartSlipDetection-request)))
  "Returns full string definition for message of type 'StartSlipDetection-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StartSlipDetection-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StartSlipDetection-request>))
  "Converts a ROS message object to a list"
  (cl:list 'StartSlipDetection-request
))
;//! \htmlinclude StartSlipDetection-response.msg.html

(cl:defclass <StartSlipDetection-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass StartSlipDetection-response (<StartSlipDetection-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StartSlipDetection-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StartSlipDetection-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name papillarray_ros_v2-srv:<StartSlipDetection-response> is deprecated: use papillarray_ros_v2-srv:StartSlipDetection-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <StartSlipDetection-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-srv:result-val is deprecated.  Use papillarray_ros_v2-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StartSlipDetection-response>) ostream)
  "Serializes a message object of type '<StartSlipDetection-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StartSlipDetection-response>) istream)
  "Deserializes a message object of type '<StartSlipDetection-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StartSlipDetection-response>)))
  "Returns string type for a service object of type '<StartSlipDetection-response>"
  "papillarray_ros_v2/StartSlipDetectionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StartSlipDetection-response)))
  "Returns string type for a service object of type 'StartSlipDetection-response"
  "papillarray_ros_v2/StartSlipDetectionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StartSlipDetection-response>)))
  "Returns md5sum for a message object of type '<StartSlipDetection-response>"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StartSlipDetection-response)))
  "Returns md5sum for a message object of type 'StartSlipDetection-response"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StartSlipDetection-response>)))
  "Returns full string definition for message of type '<StartSlipDetection-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StartSlipDetection-response)))
  "Returns full string definition for message of type 'StartSlipDetection-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StartSlipDetection-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StartSlipDetection-response>))
  "Converts a ROS message object to a list"
  (cl:list 'StartSlipDetection-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'StartSlipDetection)))
  'StartSlipDetection-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'StartSlipDetection)))
  'StartSlipDetection-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StartSlipDetection)))
  "Returns string type for a service object of type '<StartSlipDetection>"
  "papillarray_ros_v2/StartSlipDetection")