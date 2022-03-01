; Auto-generated. Do not edit!


(cl:in-package contactile_gripper-srv)


;//! \htmlinclude DataRecorder-request.msg.html

(cl:defclass <DataRecorder-request> (roslisp-msg-protocol:ros-message)
  ((file_prefix
    :reader file_prefix
    :initarg :file_prefix
    :type cl:string
    :initform "")
   (topic_list
    :reader topic_list
    :initarg :topic_list
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (stop
    :reader stop
    :initarg :stop
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass DataRecorder-request (<DataRecorder-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DataRecorder-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DataRecorder-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name contactile_gripper-srv:<DataRecorder-request> is deprecated: use contactile_gripper-srv:DataRecorder-request instead.")))

(cl:ensure-generic-function 'file_prefix-val :lambda-list '(m))
(cl:defmethod file_prefix-val ((m <DataRecorder-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader contactile_gripper-srv:file_prefix-val is deprecated.  Use contactile_gripper-srv:file_prefix instead.")
  (file_prefix m))

(cl:ensure-generic-function 'topic_list-val :lambda-list '(m))
(cl:defmethod topic_list-val ((m <DataRecorder-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader contactile_gripper-srv:topic_list-val is deprecated.  Use contactile_gripper-srv:topic_list instead.")
  (topic_list m))

(cl:ensure-generic-function 'stop-val :lambda-list '(m))
(cl:defmethod stop-val ((m <DataRecorder-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader contactile_gripper-srv:stop-val is deprecated.  Use contactile_gripper-srv:stop instead.")
  (stop m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DataRecorder-request>) ostream)
  "Serializes a message object of type '<DataRecorder-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'file_prefix))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'file_prefix))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'topic_list))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'topic_list))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'stop) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DataRecorder-request>) istream)
  "Deserializes a message object of type '<DataRecorder-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'file_prefix) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'file_prefix) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'topic_list) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'topic_list)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
    (cl:setf (cl:slot-value msg 'stop) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DataRecorder-request>)))
  "Returns string type for a service object of type '<DataRecorder-request>"
  "contactile_gripper/DataRecorderRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DataRecorder-request)))
  "Returns string type for a service object of type 'DataRecorder-request"
  "contactile_gripper/DataRecorderRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DataRecorder-request>)))
  "Returns md5sum for a message object of type '<DataRecorder-request>"
  "86296c4752d7ffaaedf71fd495fe5e5f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DataRecorder-request)))
  "Returns md5sum for a message object of type 'DataRecorder-request"
  "86296c4752d7ffaaedf71fd495fe5e5f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DataRecorder-request>)))
  "Returns full string definition for message of type '<DataRecorder-request>"
  (cl:format cl:nil "string file_prefix~%string[] topic_list~%bool stop~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DataRecorder-request)))
  "Returns full string definition for message of type 'DataRecorder-request"
  (cl:format cl:nil "string file_prefix~%string[] topic_list~%bool stop~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DataRecorder-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'file_prefix))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'topic_list) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DataRecorder-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DataRecorder-request
    (cl:cons ':file_prefix (file_prefix msg))
    (cl:cons ':topic_list (topic_list msg))
    (cl:cons ':stop (stop msg))
))
;//! \htmlinclude DataRecorder-response.msg.html

(cl:defclass <DataRecorder-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass DataRecorder-response (<DataRecorder-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DataRecorder-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DataRecorder-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name contactile_gripper-srv:<DataRecorder-response> is deprecated: use contactile_gripper-srv:DataRecorder-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DataRecorder-response>) ostream)
  "Serializes a message object of type '<DataRecorder-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DataRecorder-response>) istream)
  "Deserializes a message object of type '<DataRecorder-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DataRecorder-response>)))
  "Returns string type for a service object of type '<DataRecorder-response>"
  "contactile_gripper/DataRecorderResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DataRecorder-response)))
  "Returns string type for a service object of type 'DataRecorder-response"
  "contactile_gripper/DataRecorderResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DataRecorder-response>)))
  "Returns md5sum for a message object of type '<DataRecorder-response>"
  "86296c4752d7ffaaedf71fd495fe5e5f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DataRecorder-response)))
  "Returns md5sum for a message object of type 'DataRecorder-response"
  "86296c4752d7ffaaedf71fd495fe5e5f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DataRecorder-response>)))
  "Returns full string definition for message of type '<DataRecorder-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DataRecorder-response)))
  "Returns full string definition for message of type 'DataRecorder-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DataRecorder-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DataRecorder-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DataRecorder-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DataRecorder)))
  'DataRecorder-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DataRecorder)))
  'DataRecorder-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DataRecorder)))
  "Returns string type for a service object of type '<DataRecorder>"
  "contactile_gripper/DataRecorder")