# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CF_EnDisPollCmd_t.proto

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
  name='_py_CF_EnDisPollCmd_t.proto',
  package='',
  serialized_pb=_b('\n\x1b_py_CF_EnDisPollCmd_t.proto\"S\n\x14\x43\x46_EnDisPollCmd_t_pb\x12\r\n\x05Spare\x18\x01 \x03(\r\x12\x0c\n\x04\x43han\x18\x02 \x02(\r\x12\x0b\n\x03\x44ir\x18\x03 \x02(\r\x12\x11\n\tCmdHeader\x18\x04 \x03(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CF_ENDISPOLLCMD_T_PB = _descriptor.Descriptor(
  name='CF_EnDisPollCmd_t_pb',
  full_name='CF_EnDisPollCmd_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Spare', full_name='CF_EnDisPollCmd_t_pb.Spare', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Chan', full_name='CF_EnDisPollCmd_t_pb.Chan', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Dir', full_name='CF_EnDisPollCmd_t_pb.Dir', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdHeader', full_name='CF_EnDisPollCmd_t_pb.CmdHeader', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=31,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['CF_EnDisPollCmd_t_pb'] = _CF_ENDISPOLLCMD_T_PB

CF_EnDisPollCmd_t_pb = _reflection.GeneratedProtocolMessageType('CF_EnDisPollCmd_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CF_ENDISPOLLCMD_T_PB,
  __module__ = '_py_CF_EnDisPollCmd_t_pb2'
  # @@protoc_insertion_point(class_scope:CF_EnDisPollCmd_t_pb)
  ))
_sym_db.RegisterMessage(CF_EnDisPollCmd_t_pb)


# @@protoc_insertion_point(module_scope)