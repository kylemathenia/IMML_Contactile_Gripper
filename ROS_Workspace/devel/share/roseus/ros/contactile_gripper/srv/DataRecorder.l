;; Auto-generated. Do not edit!


(when (boundp 'contactile_gripper::DataRecorder)
  (if (not (find-package "CONTACTILE_GRIPPER"))
    (make-package "CONTACTILE_GRIPPER"))
  (shadow 'DataRecorder (find-package "CONTACTILE_GRIPPER")))
(unless (find-package "CONTACTILE_GRIPPER::DATARECORDER")
  (make-package "CONTACTILE_GRIPPER::DATARECORDER"))
(unless (find-package "CONTACTILE_GRIPPER::DATARECORDERREQUEST")
  (make-package "CONTACTILE_GRIPPER::DATARECORDERREQUEST"))
(unless (find-package "CONTACTILE_GRIPPER::DATARECORDERRESPONSE")
  (make-package "CONTACTILE_GRIPPER::DATARECORDERRESPONSE"))

(in-package "ROS")





(defclass contactile_gripper::DataRecorderRequest
  :super ros::object
  :slots (_file_prefix _topic_list _stop ))

(defmethod contactile_gripper::DataRecorderRequest
  (:init
   (&key
    ((:file_prefix __file_prefix) "")
    ((:topic_list __topic_list) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:stop __stop) nil)
    )
   (send-super :init)
   (setq _file_prefix (string __file_prefix))
   (setq _topic_list __topic_list)
   (setq _stop __stop)
   self)
  (:file_prefix
   (&optional __file_prefix)
   (if __file_prefix (setq _file_prefix __file_prefix)) _file_prefix)
  (:topic_list
   (&optional __topic_list)
   (if __topic_list (setq _topic_list __topic_list)) _topic_list)
  (:stop
   (&optional __stop)
   (if __stop (setq _stop __stop)) _stop)
  (:serialization-length
   ()
   (+
    ;; string _file_prefix
    4 (length _file_prefix)
    ;; string[] _topic_list
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _topic_list)) 4
    ;; bool _stop
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _file_prefix
       (write-long (length _file_prefix) s) (princ _file_prefix s)
     ;; string[] _topic_list
     (write-long (length _topic_list) s)
     (dolist (elem _topic_list)
       (write-long (length elem) s) (princ elem s)
       )
     ;; bool _stop
       (if _stop (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _file_prefix
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _file_prefix (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string[] _topic_list
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _topic_list (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _topic_list i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; bool _stop
     (setq _stop (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass contactile_gripper::DataRecorderResponse
  :super ros::object
  :slots ())

(defmethod contactile_gripper::DataRecorderResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass contactile_gripper::DataRecorder
  :super ros::object
  :slots ())

(setf (get contactile_gripper::DataRecorder :md5sum-) "86296c4752d7ffaaedf71fd495fe5e5f")
(setf (get contactile_gripper::DataRecorder :datatype-) "contactile_gripper/DataRecorder")
(setf (get contactile_gripper::DataRecorder :request) contactile_gripper::DataRecorderRequest)
(setf (get contactile_gripper::DataRecorder :response) contactile_gripper::DataRecorderResponse)

(defmethod contactile_gripper::DataRecorderRequest
  (:response () (instance contactile_gripper::DataRecorderResponse :init)))

(setf (get contactile_gripper::DataRecorderRequest :md5sum-) "86296c4752d7ffaaedf71fd495fe5e5f")
(setf (get contactile_gripper::DataRecorderRequest :datatype-) "contactile_gripper/DataRecorderRequest")
(setf (get contactile_gripper::DataRecorderRequest :definition-)
      "string file_prefix
string[] topic_list
bool stop
---
")

(setf (get contactile_gripper::DataRecorderResponse :md5sum-) "86296c4752d7ffaaedf71fd495fe5e5f")
(setf (get contactile_gripper::DataRecorderResponse :datatype-) "contactile_gripper/DataRecorderResponse")
(setf (get contactile_gripper::DataRecorderResponse :definition-)
      "string file_prefix
string[] topic_list
bool stop
---
")



(provide :contactile_gripper/DataRecorder "86296c4752d7ffaaedf71fd495fe5e5f")


