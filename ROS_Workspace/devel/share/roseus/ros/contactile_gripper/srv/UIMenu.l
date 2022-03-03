;; Auto-generated. Do not edit!


(when (boundp 'contactile_gripper::UIMenu)
  (if (not (find-package "CONTACTILE_GRIPPER"))
    (make-package "CONTACTILE_GRIPPER"))
  (shadow 'UIMenu (find-package "CONTACTILE_GRIPPER")))
(unless (find-package "CONTACTILE_GRIPPER::UIMENU")
  (make-package "CONTACTILE_GRIPPER::UIMENU"))
(unless (find-package "CONTACTILE_GRIPPER::UIMENUREQUEST")
  (make-package "CONTACTILE_GRIPPER::UIMENUREQUEST"))
(unless (find-package "CONTACTILE_GRIPPER::UIMENURESPONSE")
  (make-package "CONTACTILE_GRIPPER::UIMENURESPONSE"))

(in-package "ROS")





(defclass contactile_gripper::UIMenuRequest
  :super ros::object
  :slots (_menu ))

(defmethod contactile_gripper::UIMenuRequest
  (:init
   (&key
    ((:menu __menu) "")
    )
   (send-super :init)
   (setq _menu (string __menu))
   self)
  (:menu
   (&optional __menu)
   (if __menu (setq _menu __menu)) _menu)
  (:serialization-length
   ()
   (+
    ;; string _menu
    4 (length _menu)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _menu
       (write-long (length _menu) s) (princ _menu s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _menu
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _menu (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass contactile_gripper::UIMenuResponse
  :super ros::object
  :slots (_response ))

(defmethod contactile_gripper::UIMenuResponse
  (:init
   (&key
    ((:response __response) "")
    )
   (send-super :init)
   (setq _response (string __response))
   self)
  (:response
   (&optional __response)
   (if __response (setq _response __response)) _response)
  (:serialization-length
   ()
   (+
    ;; string _response
    4 (length _response)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _response
       (write-long (length _response) s) (princ _response s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _response
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _response (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass contactile_gripper::UIMenu
  :super ros::object
  :slots ())

(setf (get contactile_gripper::UIMenu :md5sum-) "61c60e1f23cfdf7f6bcc81df7ce1f6cc")
(setf (get contactile_gripper::UIMenu :datatype-) "contactile_gripper/UIMenu")
(setf (get contactile_gripper::UIMenu :request) contactile_gripper::UIMenuRequest)
(setf (get contactile_gripper::UIMenu :response) contactile_gripper::UIMenuResponse)

(defmethod contactile_gripper::UIMenuRequest
  (:response () (instance contactile_gripper::UIMenuResponse :init)))

(setf (get contactile_gripper::UIMenuRequest :md5sum-) "61c60e1f23cfdf7f6bcc81df7ce1f6cc")
(setf (get contactile_gripper::UIMenuRequest :datatype-) "contactile_gripper/UIMenuRequest")
(setf (get contactile_gripper::UIMenuRequest :definition-)
      "string menu
---
string response
")

(setf (get contactile_gripper::UIMenuResponse :md5sum-) "61c60e1f23cfdf7f6bcc81df7ce1f6cc")
(setf (get contactile_gripper::UIMenuResponse :datatype-) "contactile_gripper/UIMenuResponse")
(setf (get contactile_gripper::UIMenuResponse :definition-)
      "string menu
---
string response
")



(provide :contactile_gripper/UIMenu "61c60e1f23cfdf7f6bcc81df7ce1f6cc")


