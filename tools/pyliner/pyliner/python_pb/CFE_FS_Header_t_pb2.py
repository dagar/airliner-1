# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CFE_FS_Header_t.proto

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
  name='_py_CFE_FS_Header_t.proto',
  package='',
  serialized_pb=_b('\n\x19_py_CFE_FS_Header_t.proto\"\xce\x01\n\x12\x43\x46\x45_FS_Header_t_pb\x12\x13\n\x0b\x43ontentType\x18\x01 \x02(\r\x12\x13\n\x0b\x44\x65scription\x18\x02 \x03(\t\x12\x14\n\x0cSpacecraftID\x18\x03 \x02(\r\x12\x16\n\x0eTimeSubSeconds\x18\x04 \x02(\r\x12\x13\n\x0bProcessorID\x18\x05 \x02(\r\x12\x0f\n\x07SubType\x18\x06 \x02(\r\x12\x0e\n\x06Length\x18\x07 \x02(\r\x12\x13\n\x0bTimeSeconds\x18\x08 \x02(\r\x12\x15\n\rApplicationID\x18\t \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CFE_FS_HEADER_T_PB = _descriptor.Descriptor(
  name='CFE_FS_Header_t_pb',
  full_name='CFE_FS_Header_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ContentType', full_name='CFE_FS_Header_t_pb.ContentType', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Description', full_name='CFE_FS_Header_t_pb.Description', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpacecraftID', full_name='CFE_FS_Header_t_pb.SpacecraftID', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeSubSeconds', full_name='CFE_FS_Header_t_pb.TimeSubSeconds', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ProcessorID', full_name='CFE_FS_Header_t_pb.ProcessorID', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SubType', full_name='CFE_FS_Header_t_pb.SubType', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Length', full_name='CFE_FS_Header_t_pb.Length', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeSeconds', full_name='CFE_FS_Header_t_pb.TimeSeconds', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ApplicationID', full_name='CFE_FS_Header_t_pb.ApplicationID', index=8,
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
  serialized_start=30,
  serialized_end=236,
)

DESCRIPTOR.message_types_by_name['CFE_FS_Header_t_pb'] = _CFE_FS_HEADER_T_PB

CFE_FS_Header_t_pb = _reflection.GeneratedProtocolMessageType('CFE_FS_Header_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_FS_HEADER_T_PB,
  __module__ = '_py_CFE_FS_Header_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_FS_Header_t_pb)
  ))
_sym_db.RegisterMessage(CFE_FS_Header_t_pb)


# @@protoc_insertion_point(module_scope)