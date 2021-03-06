// Generated by gencpp from file contactile_gripper/StepperSetLimitRequest.msg
// DO NOT EDIT!


#ifndef CONTACTILE_GRIPPER_MESSAGE_STEPPERSETLIMITREQUEST_H
#define CONTACTILE_GRIPPER_MESSAGE_STEPPERSETLIMITREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace contactile_gripper
{
template <class ContainerAllocator>
struct StepperSetLimitRequest_
{
  typedef StepperSetLimitRequest_<ContainerAllocator> Type;

  StepperSetLimitRequest_()
    : switch()
    , action()  {
    }
  StepperSetLimitRequest_(const ContainerAllocator& _alloc)
    : switch(_alloc)
    , action(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _switch_type;
  _switch_type switch;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _action_type;
  _action_type action;





  typedef boost::shared_ptr< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> const> ConstPtr;

}; // struct StepperSetLimitRequest_

typedef ::contactile_gripper::StepperSetLimitRequest_<std::allocator<void> > StepperSetLimitRequest;

typedef boost::shared_ptr< ::contactile_gripper::StepperSetLimitRequest > StepperSetLimitRequestPtr;
typedef boost::shared_ptr< ::contactile_gripper::StepperSetLimitRequest const> StepperSetLimitRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator1> & lhs, const ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator2> & rhs)
{
  return lhs.switch == rhs.switch &&
    lhs.action == rhs.action;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator1> & lhs, const ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace contactile_gripper

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4c5c278c9ea572e11c6039a02c19e5a9";
  }

  static const char* value(const ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4c5c278c9ea572e1ULL;
  static const uint64_t static_value2 = 0x1c6039a02c19e5a9ULL;
};

template<class ContainerAllocator>
struct DataType< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "contactile_gripper/StepperSetLimitRequest";
  }

  static const char* value(const ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string switch\n"
"string action\n"
;
  }

  static const char* value(const ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.switch);
      stream.next(m.action);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct StepperSetLimitRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::contactile_gripper::StepperSetLimitRequest_<ContainerAllocator>& v)
  {
    s << indent << "switch: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.switch);
    s << indent << "action: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.action);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CONTACTILE_GRIPPER_MESSAGE_STEPPERSETLIMITREQUEST_H
