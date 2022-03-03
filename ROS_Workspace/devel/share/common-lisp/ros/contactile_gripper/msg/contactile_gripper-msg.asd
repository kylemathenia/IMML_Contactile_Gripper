
(cl:in-package :asdf)

(defsystem "contactile_gripper-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Float32List" :depends-on ("_package_Float32List"))
    (:file "_package_Float32List" :depends-on ("_package"))
    (:file "Int32List" :depends-on ("_package_Int32List"))
    (:file "_package_Int32List" :depends-on ("_package"))
  ))