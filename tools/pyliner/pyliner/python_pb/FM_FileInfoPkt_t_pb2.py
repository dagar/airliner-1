# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_FM_FileInfoPkt_t.proto

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
  name='_py_FM_FileInfoPkt_t.proto',
  package='',
  serialized_pb=_b('\n\x1a_py_FM_FileInfoPkt_t.proto\"\xba\x01\n\x13\x46M_FileInfoPkt_t_pb\x12\x14\n\x0c\x43RC_Computed\x18\x01 \x02(\r\x12\x10\n\x08\x46ilename\x18\x02 \x03(\t\x12\x0b\n\x03\x43RC\x18\x03 \x02(\r\x12\x12\n\nFileStatus\x18\x04 \x02(\r\x12\x11\n\tTlmHeader\x18\x05 \x03(\r\x12\r\n\x05Spare\x18\x06 \x03(\r\x12\x10\n\x08\x46ileSize\x18\x07 \x02(\r\x12\x18\n\x10LastModifiedTime\x18\x08 \x02(\r\x12\x0c\n\x04Mode\x18\t \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FM_FILEINFOPKT_T_PB = _descriptor.Descriptor(
  name='FM_FileInfoPkt_t_pb',
  full_name='FM_FileInfoPkt_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='CRC_Computed', full_name='FM_FileInfoPkt_t_pb.CRC_Computed', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Filename', full_name='FM_FileInfoPkt_t_pb.Filename', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CRC', full_name='FM_FileInfoPkt_t_pb.CRC', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FileStatus', full_name='FM_FileInfoPkt_t_pb.FileStatus', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='FM_FileInfoPkt_t_pb.TlmHeader', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Spare', full_name='FM_FileInfoPkt_t_pb.Spare', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FileSize', full_name='FM_FileInfoPkt_t_pb.FileSize', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastModifiedTime', full_name='FM_FileInfoPkt_t_pb.LastModifiedTime', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Mode', full_name='FM_FileInfoPkt_t_pb.Mode', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_end=217,
)

DESCRIPTOR.message_types_by_name['FM_FileInfoPkt_t_pb'] = _FM_FILEINFOPKT_T_PB

FM_FileInfoPkt_t_pb = _reflection.GeneratedProtocolMessageType('FM_FileInfoPkt_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _FM_FILEINFOPKT_T_PB,
  __module__ = '_py_FM_FileInfoPkt_t_pb2'
  # @@protoc_insertion_point(class_scope:FM_FileInfoPkt_t_pb)
  ))
_sym_db.RegisterMessage(FM_FileInfoPkt_t_pb)


# @@protoc_insertion_point(module_scope)