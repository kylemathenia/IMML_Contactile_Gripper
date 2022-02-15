// Generated by gencpp from file papillarray_ros_v2/BiasRequestResponse.msg
// DO NOT EDIT!


#ifndef PAPILLARRAY_ROS_V2_MESSAGE_BIASREQUESTRESPONSE_H
#define PAPILLARRAY_ROS_V2_MESSAGE_BIASREQUESTRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace papillarray_ros_v2
{
template <class ContainerAllocator>
struct BiasRequestResponse_
{
  typedef BiasRequestResponse_<ContainerAllocator> Type;

  BiasRequestResponse_()
    : result(false)  {
    }
  BiasRequestResponse_(const ContainerAllocator& _alloc)
    : result(false)  {
  (void)_alloc;
    }



   typedef uint8_t _result_type;
  _result_type result;





  typedef boost::shared_ptr< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> const> ConstPtr;

}; // struct BiasRequestResponse_

typedef ::papillarray_ros_v2::BiasRequestResponse_<std::allocator<void> > BiasRequestResponse;

typedef boost::shared_ptr< ::papillarray_ros_v2::BiasRequestResponse > BiasRequestResponsePtr;
typedef boost::shared_ptr< ::papillarray_ros_v2::BiasRequestResponse const> BiasRequestResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator1> & lhs, const ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator2> & rhs)
{
  return lhs.result == rhs.result;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator1> & lhs, const ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace papillarray_ros_v2

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eb13ac1f1354ccecb7941ee8fa2192e8";
  }

  static const char* value(const ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeb13ac1f1354ccecULL;
  static const uint64_t static_value2 = 0xb7941ee8fa2192e8ULL;
};

template<class ContainerAllocator>
struct DataType< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "papillarray_ros_v2/BiasRequestResponse";
  }

  static const char* value(const ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool result\n"
"\n"
;
  }

  static const char* value(const ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct BiasRequestResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::papillarray_ros_v2::BiasRequestResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PAPILLARRAY_ROS_V2_MESSAGE_BIASREQUESTRESPONSE_H
