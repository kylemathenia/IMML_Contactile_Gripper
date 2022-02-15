
(cl:in-package :asdf)

(defsystem "papillarray_ros_v2-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "BiasRequest" :depends-on ("_package_BiasRequest"))
    (:file "_package_BiasRequest" :depends-on ("_package"))
    (:file "StartSlipDetection" :depends-on ("_package_StartSlipDetection"))
    (:file "_package_StartSlipDetection" :depends-on ("_package"))
    (:file "StopSlipDetection" :depends-on ("_package_StopSlipDetection"))
    (:file "_package_StopSlipDetection" :depends-on ("_package"))
  ))