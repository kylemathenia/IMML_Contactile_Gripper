; Auto-generated. Do not edit!


(cl:in-package papillarray_ros_v2-srv)


;//! \htmlinclude BiasRequest-request.msg.html

(cl:defclass <BiasRequest-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass BiasRequest-request (<BiasRequest-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BiasRequest-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BiasRequest-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name papillarray_ros_v2-srv:<BiasRequest-request> is deprecated: use papillarray_ros_v2-srv:BiasRequest-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BiasRequest-request>) ostream)
  "Serializes a message object of type '<BiasRequest-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BiasRequest-request>) istream)
  "Deserializes a message object of type '<BiasRequest-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BiasRequest-request>)))
  "Returns string type for a service object of type '<BiasRequest-request>"
  "papillarray_ros_v2/BiasRequestRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BiasRequest-request)))
  "Returns string type for a service object of type 'BiasRequest-request"
  "papillarray_ros_v2/BiasRequestRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BiasRequest-request>)))
  "Returns md5sum for a message object of type '<BiasRequest-request>"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BiasRequest-request)))
  "Returns md5sum for a message object of type 'BiasRequest-request"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BiasRequest-request>)))
  "Returns full string definition for message of type '<BiasRequest-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BiasRequest-request)))
  "Returns full string definition for message of type 'BiasRequest-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BiasRequest-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BiasRequest-request>))
  "Converts a ROS message object to a list"
  (cl:list 'BiasRequest-request
))
;//! \htmlinclude BiasRequest-response.msg.html

(cl:defclass <BiasRequest-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass BiasRequest-response (<BiasRequest-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BiasRequest-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BiasRequest-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name papillarray_ros_v2-srv:<BiasRequest-response> is deprecated: use papillarray_ros_v2-srv:BiasRequest-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <BiasRequest-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader papillarray_ros_v2-srv:result-val is deprecated.  Use papillarray_ros_v2-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BiasRequest-response>) ostream)
  "Serializes a message object of type '<BiasRequest-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BiasRequest-response>) istream)
  "Deserializes a message object of type '<BiasRequest-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BiasRequest-response>)))
  "Returns string type for a service object of type '<BiasRequest-response>"
  "papillarray_ros_v2/BiasRequestResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BiasRequest-response)))
  "Returns string type for a service object of type 'BiasRequest-response"
  "papillarray_ros_v2/BiasRequestResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BiasRequest-response>)))
  "Returns md5sum for a message object of type '<BiasRequest-response>"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BiasRequest-response)))
  "Returns md5sum for a message object of type 'BiasRequest-response"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BiasRequest-response>)))
  "Returns full string definition for message of type '<BiasRequest-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BiasRequest-response)))
  "Returns full string definition for message of type 'BiasRequest-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BiasRequest-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BiasRequest-response>))
  "Converts a ROS message object to a list"
  (cl:list 'BiasRequest-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'BiasRequest)))
  'BiasRequest-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'BiasRequest)))
  'BiasRequest-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BiasRequest)))
  "Returns string type for a service object of type '<BiasRequest>"
  "papillarray_ros_v2/BiasRequest")