// Generated by gencpp from file contactile_gripper/StepperOffRequest.msg
// DO NOT EDIT!


#ifndef CONTACTILE_GRIPPER_MESSAGE_STEPPEROFFREQUEST_H
#define CONTACTILE_GRIPPER_MESSAGE_STEPPEROFFREQUEST_H


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
struct StepperOffRequest_
{
  typedef StepperOffRequest_<ContainerAllocator> Type;

  StepperOffRequest_()
    : mode()  {
    }
  StepperOffRequest_(const ContainerAllocator& _alloc)
    : mode(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _mode_type;
  _mode_type mode;





  typedef boost::shared_ptr< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> const> ConstPtr;

}; // struct StepperOffRequest_

typedef ::contactile_gripper::StepperOffRequest_<std::allocator<void> > StepperOffRequest;

typedef boost::shared_ptr< ::contactile_gripper::StepperOffRequest > StepperOffRequestPtr;
typedef boost::shared_ptr< ::contactile_gripper::StepperOffRequest const> StepperOffRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::contactile_gripper::StepperOffRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::contactile_gripper::StepperOffRequest_<ContainerAllocator1> & lhs, const ::contactile_gripper::StepperOffRequest_<ContainerAllocator2> & rhs)
{
  return lhs.mode == rhs.mode;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::contactile_gripper::StepperOffRequest_<ContainerAllocator1> & lhs, const ::contactile_gripper::StepperOffRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace contactile_gripper

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e84dc3ad5dc323bb64f0aca01c2d1eef";
  }

  static const char* value(const ::contactile_gripper::StepperOffRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe84dc3ad5dc323bbULL;
  static const uint64_t static_value2 = 0x64f0aca01c2d1eefULL;
};

template<class ContainerAllocator>
struct DataType< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "contactile_gripper/StepperOffRequest";
  }

  static const char* value(const ::contactile_gripper::StepperOffRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string mode\n"
;
  }

  static const char* value(const ::contactile_gripper::StepperOffRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.mode);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct StepperOffRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::contactile_gripper::StepperOffRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::contactile_gripper::StepperOffRequest_<ContainerAllocator>& v)
  {
    s << indent << "mode: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.mode);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CONTACTILE_GRIPPER_MESSAGE_STEPPEROFFREQUEST_H