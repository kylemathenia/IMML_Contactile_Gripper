
(cl:in-package :asdf)

(defsystem "contactile_gripper-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ChangeMode" :depends-on ("_package_ChangeMode"))
    (:file "_package_ChangeMode" :depends-on ("_package"))
    (:file "DataRecorder" :depends-on ("_package_DataRecorder"))
    (:file "_package_DataRecorder" :depends-on ("_package"))
    (:file "GripperChangeMode" :depends-on ("_package_GripperChangeMode"))
    (:file "_package_GripperChangeMode" :depends-on ("_package"))
    (:file "StepperOff" :depends-on ("_package_StepperOff"))
    (:file "_package_StepperOff" :depends-on ("_package"))
    (:file "StepperSetLimit" :depends-on ("_package_StepperSetLimit"))
    (:file "_package_StepperSetLimit" :depends-on ("_package"))
    (:file "UIMenu" :depends-on ("_package_UIMenu"))
    (:file "_package_UIMenu" :depends-on ("_package"))
  ))