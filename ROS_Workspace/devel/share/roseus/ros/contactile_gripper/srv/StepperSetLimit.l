;; Auto-generated. Do not edit!


(when (boundp 'contactile_gripper::StepperSetLimit)
  (if (not (find-package "CONTACTILE_GRIPPER"))
    (make-package "CONTACTILE_GRIPPER"))
  (shadow 'StepperSetLimit (find-package "CONTACTILE_GRIPPER")))
(unless (find-package "CONTACTILE_GRIPPER::STEPPERSETLIMIT")
  (make-package "CONTACTILE_GRIPPER::STEPPERSETLIMIT"))
(unless (find-package "CONTACTILE_GRIPPER::STEPPERSETLIMITREQUEST")
  (make-package "CONTACTILE_GRIPPER::STEPPERSETLIMITREQUEST"))
(unless (find-package "CONTACTILE_GRIPPER::STEPPERSETLIMITRESPONSE")
  (make-package "CONTACTILE_GRIPPER::STEPPERSETLIMITRESPONSE"))

(in-package "ROS")





(defclass contactile_gripper::StepperSetLimitRequest
  :super ros::object
  :slots (_switch _action ))

(defmethod contactile_gripper::StepperSetLimitRequest
  (:init
   (&key
    ((:switch __switch) "")
    ((:action __action) "")
    )
   (send-super :init)
   (setq _switch (string __switch))
   (setq _action (string __action))
   self)
  (:switch
   (&optional __switch)
   (if __switch (setq _switch __switch)) _switch)
  (:action
   (&optional __action)
   (if __action (setq _action __action)) _action)
  (:serialization-length
   ()
   (+
    ;; string _switch
    4 (length _switch)
    ;; string _action
    4 (length _action)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _switch
       (write-long (length _switch) s) (princ _switch s)
     ;; string _action
       (write-long (length _action) s) (princ _action s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _switch
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _switch (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _action
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _action (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass contactile_gripper::StepperSetLimitResponse
  :super ros::object
  :slots (_response ))

(defmethod contactile_gripper::StepperSetLimitResponse
  (:init
   (&key
    ((:response __response) 0)
    )
   (send-super :init)
   (setq _response (round __response))
   self)
  (:response
   (&optional __response)
   (if __response (setq _response __response)) _response)
  (:serialization-length
   ()
   (+
    ;; int64 _response
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _response
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _response (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _response) (= (length (_response . bv)) 2)) ;; bignum
              (write-long (ash (elt (_response . bv) 0) 0) s)
              (write-long (ash (elt (_response . bv) 1) -1) s))
             ((and (class _response) (= (length (_response . bv)) 1)) ;; big1
              (write-long (elt (_response . bv) 0) s)
              (write-long (if (>= _response 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _response s)(write-long (if (>= _response 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _response
#+(or :alpha :irix6 :x86_64)
      (setf _response (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _response (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass contactile_gripper::StepperSetLimit
  :super ros::object
  :slots ())

(setf (get contactile_gripper::StepperSetLimit :md5sum-) "5b0187267379b2af4b8e7118fa12084a")
(setf (get contactile_gripper::StepperSetLimit :datatype-) "contactile_gripper/StepperSetLimit")
(setf (get contactile_gripper::StepperSetLimit :request) contactile_gripper::StepperSetLimitRequest)
(setf (get contactile_gripper::StepperSetLimit :response) contactile_gripper::StepperSetLimitResponse)

(defmethod contactile_gripper::StepperSetLimitRequest
  (:response () (instance contactile_gripper::StepperSetLimitResponse :init)))

(setf (get contactile_gripper::StepperSetLimitRequest :md5sum-) "5b0187267379b2af4b8e7118fa12084a")
(setf (get contactile_gripper::StepperSetLimitRequest :datatype-) "contactile_gripper/StepperSetLimitRequest")
(setf (get contactile_gripper::StepperSetLimitRequest :definition-)
      "string switch
string action
---
int64 response
")

(setf (get contactile_gripper::StepperSetLimitResponse :md5sum-) "5b0187267379b2af4b8e7118fa12084a")
(setf (get contactile_gripper::StepperSetLimitResponse :datatype-) "contactile_gripper/StepperSetLimitResponse")
(setf (get contactile_gripper::StepperSetLimitResponse :definition-)
      "string switch
string action
---
int64 response
")



(provide :contactile_gripper/StepperSetLimit "5b0187267379b2af4b8e7118fa12084a")


