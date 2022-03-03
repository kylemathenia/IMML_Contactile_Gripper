;; Auto-generated. Do not edit!


(when (boundp 'contactile_gripper::Int32List)
  (if (not (find-package "CONTACTILE_GRIPPER"))
    (make-package "CONTACTILE_GRIPPER"))
  (shadow 'Int32List (find-package "CONTACTILE_GRIPPER")))
(unless (find-package "CONTACTILE_GRIPPER::INT32LIST")
  (make-package "CONTACTILE_GRIPPER::INT32LIST"))

(in-package "ROS")
;;//! \htmlinclude Int32List.msg.html


(defclass contactile_gripper::Int32List
  :super ros::object
  :slots (_list ))

(defmethod contactile_gripper::Int32List
  (:init
   (&key
    ((:list __list) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _list __list)
   self)
  (:list
   (&optional __list)
   (if __list (setq _list __list)) _list)
  (:serialization-length
   ()
   (+
    ;; int32[] _list
    (* 4    (length _list)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _list
     (write-long (length _list) s)
     (dotimes (i (length _list))
       (write-long (elt _list i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _list
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _list (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _list i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get contactile_gripper::Int32List :md5sum-) "33cd48253e96459f6910f32d963eda83")
(setf (get contactile_gripper::Int32List :datatype-) "contactile_gripper/Int32List")
(setf (get contactile_gripper::Int32List :definition-)
      "int32[] list
")



(provide :contactile_gripper/Int32List "33cd48253e96459f6910f32d963eda83")


