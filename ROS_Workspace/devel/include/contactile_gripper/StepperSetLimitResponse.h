// Generated by gencpp from file contactile_gripper/StepperSetLimitResponse.msg
// DO NOT EDIT!


#ifndef CONTACTILE_GRIPPER_MESSAGE_STEPPERSETLIMITRESPONSE_H
#define CONTACTILE_GRIPPER_MESSAGE_STEPPERSETLIMITRESPONSE_H


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
struct StepperSetLimitResponse_
{
  typedef StepperSetLimitResponse_<ContainerAllocator> Type;

  StepperSetLimitResponse_()
    : response(0)  {
    }
  StepperSetLimitResponse_(const ContainerAllocator& _alloc)
    : response(0)  {
  (void)_alloc;
    }



   typedef int64_t _response_type;
  _response_type response;





  typedef boost::shared_ptr< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> const> ConstPtr;

}; // struct StepperSetLimitResponse_

typedef ::contactile_gripper::StepperSetLimitResponse_<std::allocator<void> > StepperSetLimitResponse;

typedef boost::shared_ptr< ::contactile_gripper::StepperSetLimitResponse > StepperSetLimitResponsePtr;
typedef boost::shared_ptr< ::contactile_gripper::StepperSetLimitResponse const> StepperSetLimitResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator1> & lhs, const ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator2> & rhs)
{
  return lhs.response == rhs.response;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator1> & lhs, const ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace contactile_gripper

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4bf37bc717f68787645077428bea3751";
  }

  static const char* value(const ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4bf37bc717f68787ULL;
  static const uint64_t static_value2 = 0x645077428bea3751ULL;
};

template<class ContainerAllocator>
struct DataType< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "contactile_gripper/StepperSetLimitResponse";
  }

  static const char* value(const ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 response\n"
;
  }

  static const char* value(const ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.response);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct StepperSetLimitResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::contactile_gripper::StepperSetLimitResponse_<ContainerAllocator>& v)
  {
    s << indent << "response: ";
    Printer<int64_t>::stream(s, indent + "  ", v.response);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CONTACTILE_GRIPPER_MESSAGE_STEPPERSETLIMITRESPONSE_H