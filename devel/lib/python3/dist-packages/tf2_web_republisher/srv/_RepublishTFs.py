# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tf2_web_republisher/RepublishTFsRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class RepublishTFsRequest(genpy.Message):
  _md5sum = "f13b5a5a70ee41b437384d6715cbcd91"
  _type = "tf2_web_republisher/RepublishTFsRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """## Notify the tf2_web_republisher that republishing of certain
## TFs is desired
string[] source_frames
string target_frame
float32 angular_thres
float32 trans_thres
float32 rate
duration timeout # tf2_web_republisher will stop publishing the topic if it has zero subscribers for this amount of time
"""
  __slots__ = ['source_frames','target_frame','angular_thres','trans_thres','rate','timeout']
  _slot_types = ['string[]','string','float32','float32','float32','duration']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       source_frames,target_frame,angular_thres,trans_thres,rate,timeout

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RepublishTFsRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.source_frames is None:
        self.source_frames = []
      if self.target_frame is None:
        self.target_frame = ''
      if self.angular_thres is None:
        self.angular_thres = 0.
      if self.trans_thres is None:
        self.trans_thres = 0.
      if self.rate is None:
        self.rate = 0.
      if self.timeout is None:
        self.timeout = genpy.Duration()
    else:
      self.source_frames = []
      self.target_frame = ''
      self.angular_thres = 0.
      self.trans_thres = 0.
      self.rate = 0.
      self.timeout = genpy.Duration()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.source_frames)
      buff.write(_struct_I.pack(length))
      for val1 in self.source_frames:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      _x = self.target_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3f2i().pack(_x.angular_thres, _x.trans_thres, _x.rate, _x.timeout.secs, _x.timeout.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.timeout is None:
        self.timeout = genpy.Duration()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.source_frames = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.source_frames.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.target_frame = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.target_frame = str[start:end]
      _x = self
      start = end
      end += 20
      (_x.angular_thres, _x.trans_thres, _x.rate, _x.timeout.secs, _x.timeout.nsecs,) = _get_struct_3f2i().unpack(str[start:end])
      self.timeout.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.source_frames)
      buff.write(_struct_I.pack(length))
      for val1 in self.source_frames:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      _x = self.target_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3f2i().pack(_x.angular_thres, _x.trans_thres, _x.rate, _x.timeout.secs, _x.timeout.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.timeout is None:
        self.timeout = genpy.Duration()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.source_frames = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.source_frames.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.target_frame = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.target_frame = str[start:end]
      _x = self
      start = end
      end += 20
      (_x.angular_thres, _x.trans_thres, _x.rate, _x.timeout.secs, _x.timeout.nsecs,) = _get_struct_3f2i().unpack(str[start:end])
      self.timeout.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3f2i = None
def _get_struct_3f2i():
    global _struct_3f2i
    if _struct_3f2i is None:
        _struct_3f2i = struct.Struct("<3f2i")
    return _struct_3f2i
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tf2_web_republisher/RepublishTFsResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RepublishTFsResponse(genpy.Message):
  _md5sum = "b38cc2f19f45368c2db7867751ce95a9"
  _type = "tf2_web_republisher/RepublishTFsResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# response
string topic_name # a topic of type geometry_msgs/TransformStamped[] that publishes the requested transforms
"""
  __slots__ = ['topic_name']
  _slot_types = ['string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       topic_name

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RepublishTFsResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.topic_name is None:
        self.topic_name = ''
    else:
      self.topic_name = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.topic_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topic_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.topic_name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.topic_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topic_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.topic_name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
class RepublishTFs(object):
  _type          = 'tf2_web_republisher/RepublishTFs'
  _md5sum = 'ec8570dea2e6015c309eb6611d1a57d0'
  _request_class  = RepublishTFsRequest
  _response_class = RepublishTFsResponse
