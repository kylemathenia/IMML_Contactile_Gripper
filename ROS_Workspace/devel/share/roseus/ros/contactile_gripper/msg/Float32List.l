;; Auto-generated. Do not edit!


(when (boundp 'contactile_gripper::Float32List)
  (if (not (find-package "CONTACTILE_GRIPPER"))
    (make-package "CONTACTILE_GRIPPER"))
  (shadow 'Float32List (find-package "CONTACTILE_GRIPPER")))
(unless (find-package "CONTACTILE_GRIPPER::FLOAT32LIST")
  (make-package "CONTACTILE_GRIPPER::FLOAT32LIST"))

(in-package "ROS")
;;//! \htmlinclude Float32List.msg.html


(defclass contactile_gripper::Float32List
  :super ros::object
  :slots (_list ))

(defmethod contactile_gripper::Float32List
  (:init
   (&key
    ((:list __list) (make-array 0 :initial-element 0.0 :element-type :float))
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
    ;; float32[] _list
    (* 4    (length _list)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _list
     (write-long (length _list) s)
     (dotimes (i (length _list))
       (sys::poke (elt _list i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _list
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _list (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _list i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get contactile_gripper::Float32List :md5sum-) "f899bbf34605ab8c1065aaee8c9708ca")
(setf (get contactile_gripper::Float32List :datatype-) "contactile_gripper/Float32List")
(setf (get contactile_gripper::Float32List :definition-)
      "float32[] list
")



(provide :contactile_gripper/Float32List "f899bbf34605ab8c1065aaee8c9708ca")


