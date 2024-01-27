// Generated by gencpp from file tf2_web_republisher/TFSubscriptionGoal.msg
// DO NOT EDIT!


#ifndef TF2_WEB_REPUBLISHER_MESSAGE_TFSUBSCRIPTIONGOAL_H
#define TF2_WEB_REPUBLISHER_MESSAGE_TFSUBSCRIPTIONGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace tf2_web_republisher
{
template <class ContainerAllocator>
struct TFSubscriptionGoal_
{
  typedef TFSubscriptionGoal_<ContainerAllocator> Type;

  TFSubscriptionGoal_()
    : source_frames()
    , target_frame()
    , angular_thres(0.0)
    , trans_thres(0.0)
    , rate(0.0)  {
    }
  TFSubscriptionGoal_(const ContainerAllocator& _alloc)
    : source_frames(_alloc)
    , target_frame(_alloc)
    , angular_thres(0.0)
    , trans_thres(0.0)
    , rate(0.0)  {
  (void)_alloc;
    }



   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _source_frames_type;
  _source_frames_type source_frames;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _target_frame_type;
  _target_frame_type target_frame;

   typedef float _angular_thres_type;
  _angular_thres_type angular_thres;

   typedef float _trans_thres_type;
  _trans_thres_type trans_thres;

   typedef float _rate_type;
  _rate_type rate;





  typedef boost::shared_ptr< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> const> ConstPtr;

}; // struct TFSubscriptionGoal_

typedef ::tf2_web_republisher::TFSubscriptionGoal_<std::allocator<void> > TFSubscriptionGoal;

typedef boost::shared_ptr< ::tf2_web_republisher::TFSubscriptionGoal > TFSubscriptionGoalPtr;
typedef boost::shared_ptr< ::tf2_web_republisher::TFSubscriptionGoal const> TFSubscriptionGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator1> & lhs, const ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator2> & rhs)
{
  return lhs.source_frames == rhs.source_frames &&
    lhs.target_frame == rhs.target_frame &&
    lhs.angular_thres == rhs.angular_thres &&
    lhs.trans_thres == rhs.trans_thres &&
    lhs.rate == rhs.rate;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator1> & lhs, const ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace tf2_web_republisher

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b2dae39608227a5c1c4a91ad77023a27";
  }

  static const char* value(const ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb2dae39608227a5cULL;
  static const uint64_t static_value2 = 0x1c4a91ad77023a27ULL;
};

template<class ContainerAllocator>
struct DataType< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "tf2_web_republisher/TFSubscriptionGoal";
  }

  static const char* value(const ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# goal\n"
"string[] source_frames\n"
"string target_frame\n"
"float32 angular_thres\n"
"float32 trans_thres\n"
"float32 rate\n"
;
  }

  static const char* value(const ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.source_frames);
      stream.next(m.target_frame);
      stream.next(m.angular_thres);
      stream.next(m.trans_thres);
      stream.next(m.rate);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TFSubscriptionGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::tf2_web_republisher::TFSubscriptionGoal_<ContainerAllocator>& v)
  {
    s << indent << "source_frames[]" << std::endl;
    for (size_t i = 0; i < v.source_frames.size(); ++i)
    {
      s << indent << "  source_frames[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.source_frames[i]);
    }
    s << indent << "target_frame: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.target_frame);
    s << indent << "angular_thres: ";
    Printer<float>::stream(s, indent + "  ", v.angular_thres);
    s << indent << "trans_thres: ";
    Printer<float>::stream(s, indent + "  ", v.trans_thres);
    s << indent << "rate: ";
    Printer<float>::stream(s, indent + "  ", v.rate);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TF2_WEB_REPUBLISHER_MESSAGE_TFSUBSCRIPTIONGOAL_H
