# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_PE_HkTlm_t.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='_py_PE_HkTlm_t.proto',
  package='',
  serialized_pb=_b('\n\x14_py_PE_HkTlm_t.proto\"\xf2\x05\n\rPE_HkTlm_t_pb\x12\"\n\x1a\x45stimatorGlobalInitialized\x18\x01 \x02(\x08\x12\x10\n\x08GpsFault\x18\x02 \x02(\x08\x12\x10\n\x08GpsFused\x18\x03 \x02(\x08\x12\x12\n\nUlrTimeout\x18\x04 \x02(\x08\x12\x13\n\x0bTimeLastUlr\x18\x05 \x02(\x04\x12\x10\n\x08UlrFused\x18\x06 \x02(\x08\x12\x11\n\tAltOrigin\x18\x07 \x02(\x02\x12\x16\n\x0em_UlrAltOrigin\x18\x08 \x02(\x02\x12\x11\n\tBaroFused\x18\t \x02(\x08\x12\x11\n\tTimestamp\x18\n \x02(\x04\x12\x11\n\tLandFault\x18\x0b \x02(\x08\x12\x10\n\x08usCmdCnt\x18\x0c \x02(\r\x12\x14\n\x0cGpsAltOrigin\x18\r \x02(\x02\x12\x11\n\tZEstValid\x18\x0e \x02(\x08\x12\x13\n\x0bTimeLastGps\x18\x0f \x02(\x04\x12\x13\n\x0bLandTimeout\x18\x10 \x02(\x08\x12\x15\n\rBaroAltOrigin\x18\x11 \x02(\x02\x12\x16\n\x0eGpsInitialized\x18\x12 \x02(\x08\x12\x11\n\tBaroFault\x18\x13 \x02(\x08\x12\x17\n\x0fLandInitialized\x18\x14 \x02(\x08\x12\x11\n\tLandFused\x18\x15 \x02(\x08\x12\x12\n\nGpsTimeout\x18\x16 \x02(\x08\x12\x10\n\x08UlrFault\x18\x17 \x02(\x08\x12\x11\n\tTlmHeader\x18\x18 \x03(\r\x12\x14\n\x0cTimeLastBaro\x18\x19 \x02(\x04\x12!\n\x19\x45stimatorLocalInitialized\x18\x1a \x02(\x08\x12\x12\n\nTzEstValid\x18\x1b \x02(\x08\x12\x1c\n\x14\x41ltOriginInitialized\x18\x1c \x02(\x08\x12\x14\n\x0cTimeLastLand\x18\x1d \x02(\x04\x12\x12\n\nXyEstValid\x18\x1e \x02(\x08\x12\x13\n\x0busCmdErrCnt\x18\x1f \x02(\r\x12\x13\n\x0b\x42\x61roTimeout\x18  \x02(\x08\x12\x16\n\x0eUlrInitialized\x18! \x02(\x08\x12\x17\n\x0f\x42\x61roInitialized\x18\" \x02(\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PE_HKTLM_T_PB = _descriptor.Descriptor(
  name='PE_HkTlm_t_pb',
  full_name='PE_HkTlm_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='EstimatorGlobalInitialized', full_name='PE_HkTlm_t_pb.EstimatorGlobalInitialized', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GpsFault', full_name='PE_HkTlm_t_pb.GpsFault', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GpsFused', full_name='PE_HkTlm_t_pb.GpsFused', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UlrTimeout', full_name='PE_HkTlm_t_pb.UlrTimeout', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeLastUlr', full_name='PE_HkTlm_t_pb.TimeLastUlr', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UlrFused', full_name='PE_HkTlm_t_pb.UlrFused', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AltOrigin', full_name='PE_HkTlm_t_pb.AltOrigin', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m_UlrAltOrigin', full_name='PE_HkTlm_t_pb.m_UlrAltOrigin', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BaroFused', full_name='PE_HkTlm_t_pb.BaroFused', index=8,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='PE_HkTlm_t_pb.Timestamp', index=9,
      number=10, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LandFault', full_name='PE_HkTlm_t_pb.LandFault', index=10,
      number=11, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usCmdCnt', full_name='PE_HkTlm_t_pb.usCmdCnt', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GpsAltOrigin', full_name='PE_HkTlm_t_pb.GpsAltOrigin', index=12,
      number=13, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ZEstValid', full_name='PE_HkTlm_t_pb.ZEstValid', index=13,
      number=14, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeLastGps', full_name='PE_HkTlm_t_pb.TimeLastGps', index=14,
      number=15, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LandTimeout', full_name='PE_HkTlm_t_pb.LandTimeout', index=15,
      number=16, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BaroAltOrigin', full_name='PE_HkTlm_t_pb.BaroAltOrigin', index=16,
      number=17, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GpsInitialized', full_name='PE_HkTlm_t_pb.GpsInitialized', index=17,
      number=18, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BaroFault', full_name='PE_HkTlm_t_pb.BaroFault', index=18,
      number=19, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LandInitialized', full_name='PE_HkTlm_t_pb.LandInitialized', index=19,
      number=20, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LandFused', full_name='PE_HkTlm_t_pb.LandFused', index=20,
      number=21, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GpsTimeout', full_name='PE_HkTlm_t_pb.GpsTimeout', index=21,
      number=22, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UlrFault', full_name='PE_HkTlm_t_pb.UlrFault', index=22,
      number=23, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='PE_HkTlm_t_pb.TlmHeader', index=23,
      number=24, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeLastBaro', full_name='PE_HkTlm_t_pb.TimeLastBaro', index=24,
      number=25, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EstimatorLocalInitialized', full_name='PE_HkTlm_t_pb.EstimatorLocalInitialized', index=25,
      number=26, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TzEstValid', full_name='PE_HkTlm_t_pb.TzEstValid', index=26,
      number=27, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AltOriginInitialized', full_name='PE_HkTlm_t_pb.AltOriginInitialized', index=27,
      number=28, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeLastLand', full_name='PE_HkTlm_t_pb.TimeLastLand', index=28,
      number=29, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='XyEstValid', full_name='PE_HkTlm_t_pb.XyEstValid', index=29,
      number=30, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usCmdErrCnt', full_name='PE_HkTlm_t_pb.usCmdErrCnt', index=30,
      number=31, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BaroTimeout', full_name='PE_HkTlm_t_pb.BaroTimeout', index=31,
      number=32, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UlrInitialized', full_name='PE_HkTlm_t_pb.UlrInitialized', index=32,
      number=33, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BaroInitialized', full_name='PE_HkTlm_t_pb.BaroInitialized', index=33,
      number=34, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=779,
)

DESCRIPTOR.message_types_by_name['PE_HkTlm_t_pb'] = _PE_HKTLM_T_PB

PE_HkTlm_t_pb = _reflection.GeneratedProtocolMessageType('PE_HkTlm_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _PE_HKTLM_T_PB,
  __module__ = '_py_PE_HkTlm_t_pb2'
  # @@protoc_insertion_point(class_scope:PE_HkTlm_t_pb)
  ))
_sym_db.RegisterMessage(PE_HkTlm_t_pb)


# @@protoc_insertion_point(module_scope)