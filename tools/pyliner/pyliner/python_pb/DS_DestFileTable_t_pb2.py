# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_DS_DestFileTable_t.proto

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
  name='_py_DS_DestFileTable_t.proto',
  package='',
  serialized_pb=_b('\n\x1c_py_DS_DestFileTable_t.proto\"\xb9\x01\n\x15\x44S_DestFileEntry_t_pb\x12\x12\n\nMaxFileAge\x18\x01 \x02(\r\x12\x11\n\tExtension\x18\x02 \x03(\t\x12\x13\n\x0bMaxFileSize\x18\x03 \x02(\r\x12\x10\n\x08\x42\x61sename\x18\x04 \x03(\t\x12\x13\n\x0b\x45nableState\x18\x05 \x02(\r\x12\x14\n\x0c\x46ileNameType\x18\x06 \x02(\r\x12\x10\n\x08Pathname\x18\x07 \x03(\t\x12\x15\n\rSequenceCount\x18\x08 \x02(\r\"Q\n\x15\x44S_DestFileTable_t_pb\x12\x12\n\nDescriptor\x18\x01 \x03(\t\x12$\n\x04\x46ile\x18\x02 \x03(\x0b\x32\x16.DS_DestFileEntry_t_pb')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DS_DESTFILEENTRY_T_PB = _descriptor.Descriptor(
  name='DS_DestFileEntry_t_pb',
  full_name='DS_DestFileEntry_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MaxFileAge', full_name='DS_DestFileEntry_t_pb.MaxFileAge', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Extension', full_name='DS_DestFileEntry_t_pb.Extension', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MaxFileSize', full_name='DS_DestFileEntry_t_pb.MaxFileSize', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Basename', full_name='DS_DestFileEntry_t_pb.Basename', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EnableState', full_name='DS_DestFileEntry_t_pb.EnableState', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FileNameType', full_name='DS_DestFileEntry_t_pb.FileNameType', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pathname', full_name='DS_DestFileEntry_t_pb.Pathname', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SequenceCount', full_name='DS_DestFileEntry_t_pb.SequenceCount', index=7,
      number=8, type=13, cpp_type=3, label=2,
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
  serialized_start=33,
  serialized_end=218,
)


_DS_DESTFILETABLE_T_PB = _descriptor.Descriptor(
  name='DS_DestFileTable_t_pb',
  full_name='DS_DestFileTable_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Descriptor', full_name='DS_DestFileTable_t_pb.Descriptor', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='File', full_name='DS_DestFileTable_t_pb.File', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=220,
  serialized_end=301,
)

_DS_DESTFILETABLE_T_PB.fields_by_name['File'].message_type = _DS_DESTFILEENTRY_T_PB
DESCRIPTOR.message_types_by_name['DS_DestFileEntry_t_pb'] = _DS_DESTFILEENTRY_T_PB
DESCRIPTOR.message_types_by_name['DS_DestFileTable_t_pb'] = _DS_DESTFILETABLE_T_PB

DS_DestFileEntry_t_pb = _reflection.GeneratedProtocolMessageType('DS_DestFileEntry_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _DS_DESTFILEENTRY_T_PB,
  __module__ = '_py_DS_DestFileTable_t_pb2'
  # @@protoc_insertion_point(class_scope:DS_DestFileEntry_t_pb)
  ))
_sym_db.RegisterMessage(DS_DestFileEntry_t_pb)

DS_DestFileTable_t_pb = _reflection.GeneratedProtocolMessageType('DS_DestFileTable_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _DS_DESTFILETABLE_T_PB,
  __module__ = '_py_DS_DestFileTable_t_pb2'
  # @@protoc_insertion_point(class_scope:DS_DestFileTable_t_pb)
  ))
_sym_db.RegisterMessage(DS_DestFileTable_t_pb)


# @@protoc_insertion_point(module_scope)