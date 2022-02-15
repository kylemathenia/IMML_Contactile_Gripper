
(cl:in-package :asdf)

(defsystem "papillarray_ros_v2-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "PillarState" :depends-on ("_package_PillarState"))
    (:file "_package_PillarState" :depends-on ("_package"))
    (:file "SensorState" :depends-on ("_package_SensorState"))
    (:file "_package_SensorState" :depends-on ("_package"))
  ))