; Auto-generated. Do not edit!


(cl:in-package contactile_gripper-srv)


;//! \htmlinclude UIMenu-request.msg.html

(cl:defclass <UIMenu-request> (roslisp-msg-protocol:ros-message)
  ((menu
    :reader menu
    :initarg :menu
    :type cl:string
    :initform ""))
)

(cl:defclass UIMenu-request (<UIMenu-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UIMenu-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UIMenu-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name contactile_gripper-srv:<UIMenu-request> is deprecated: use contactile_gripper-srv:UIMenu-request instead.")))

(cl:ensure-generic-function 'menu-val :lambda-list '(m))
(cl:defmethod menu-val ((m <UIMenu-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader contactile_gripper-srv:menu-val is deprecated.  Use contactile_gripper-srv:menu instead.")
  (menu m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UIMenu-request>) ostream)
  "Serializes a message object of type '<UIMenu-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'menu))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'menu))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UIMenu-request>) istream)
  "Deserializes a message object of type '<UIMenu-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'menu) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'menu) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UIMenu-request>)))
  "Returns string type for a service object of type '<UIMenu-request>"
  "contactile_gripper/UIMenuRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UIMenu-request)))
  "Returns string type for a service object of type 'UIMenu-request"
  "contactile_gripper/UIMenuRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UIMenu-request>)))
  "Returns md5sum for a message object of type '<UIMenu-request>"
  "c203365aa9fc4c84f5cecbbb5ac3272a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UIMenu-request)))
  "Returns md5sum for a message object of type 'UIMenu-request"
  "c203365aa9fc4c84f5cecbbb5ac3272a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UIMenu-request>)))
  "Returns full string definition for message of type '<UIMenu-request>"
  (cl:format cl:nil "string menu~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UIMenu-request)))
  "Returns full string definition for message of type 'UIMenu-request"
  (cl:format cl:nil "string menu~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UIMenu-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'menu))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UIMenu-request>))
  "Converts a ROS message object to a list"
  (cl:list 'UIMenu-request
    (cl:cons ':menu (menu msg))
))
;//! \htmlinclude UIMenu-response.msg.html

(cl:defclass <UIMenu-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass UIMenu-response (<UIMenu-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UIMenu-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UIMenu-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name contactile_gripper-srv:<UIMenu-response> is deprecated: use contactile_gripper-srv:UIMenu-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UIMenu-response>) ostream)
  "Serializes a message object of type '<UIMenu-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UIMenu-response>) istream)
  "Deserializes a message object of type '<UIMenu-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UIMenu-response>)))
  "Returns string type for a service object of type '<UIMenu-response>"
  "contactile_gripper/UIMenuResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UIMenu-response)))
  "Returns string type for a service object of type 'UIMenu-response"
  "contactile_gripper/UIMenuResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UIMenu-response>)))
  "Returns md5sum for a message object of type '<UIMenu-response>"
  "c203365aa9fc4c84f5cecbbb5ac3272a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UIMenu-response)))
  "Returns md5sum for a message object of type 'UIMenu-response"
  "c203365aa9fc4c84f5cecbbb5ac3272a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UIMenu-response>)))
  "Returns full string definition for message of type '<UIMenu-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UIMenu-response)))
  "Returns full string definition for message of type 'UIMenu-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UIMenu-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UIMenu-response>))
  "Converts a ROS message object to a list"
  (cl:list 'UIMenu-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'UIMenu)))
  'UIMenu-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'UIMenu)))
  'UIMenu-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UIMenu)))
  "Returns string type for a service object of type '<UIMenu>"
  "contactile_gripper/UIMenu")