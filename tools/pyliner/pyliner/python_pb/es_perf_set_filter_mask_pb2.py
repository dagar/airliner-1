# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_es_perf_set_filter_mask.proto

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
  name='_py_es_perf_set_filter_mask.proto',
  package='',
  serialized_pb=_b('\n!_py_es_perf_set_filter_mask.proto\"O\n\"es_perf_set_filter_mask_payload_pb\x12\x15\n\rFilterMaskNum\x18\x01 \x02(\r\x12\x12\n\nFilterMask\x18\x02 \x02(\r\"R\n\x1a\x65s_perf_set_filter_mask_pb\x12\x34\n\x07Payload\x18\x01 \x02(\x0b\x32#.es_perf_set_filter_mask_payload_pb')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ES_PERF_SET_FILTER_MASK_PAYLOAD_PB = _descriptor.Descriptor(
  name='es_perf_set_filter_mask_payload_pb',
  full_name='es_perf_set_filter_mask_payload_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FilterMaskNum', full_name='es_perf_set_filter_mask_payload_pb.FilterMaskNum', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FilterMask', full_name='es_perf_set_filter_mask_payload_pb.FilterMask', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=37,
  serialized_end=116,
)


_ES_PERF_SET_FILTER_MASK_PB = _descriptor.Descriptor(
  name='es_perf_set_filter_mask_pb',
  full_name='es_perf_set_filter_mask_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Payload', full_name='es_perf_set_filter_mask_pb.Payload', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=118,
  serialized_end=200,
)

_ES_PERF_SET_FILTER_MASK_PB.fields_by_name['Payload'].message_type = _ES_PERF_SET_FILTER_MASK_PAYLOAD_PB
DESCRIPTOR.message_types_by_name['es_perf_set_filter_mask_payload_pb'] = _ES_PERF_SET_FILTER_MASK_PAYLOAD_PB
DESCRIPTOR.message_types_by_name['es_perf_set_filter_mask_pb'] = _ES_PERF_SET_FILTER_MASK_PB

es_perf_set_filter_mask_payload_pb = _reflection.GeneratedProtocolMessageType('es_perf_set_filter_mask_payload_pb', (_message.Message,), dict(
  DESCRIPTOR = _ES_PERF_SET_FILTER_MASK_PAYLOAD_PB,
  __module__ = '_py_es_perf_set_filter_mask_pb2'
  # @@protoc_insertion_point(class_scope:es_perf_set_filter_mask_payload_pb)
  ))
_sym_db.RegisterMessage(es_perf_set_filter_mask_payload_pb)

es_perf_set_filter_mask_pb = _reflection.GeneratedProtocolMessageType('es_perf_set_filter_mask_pb', (_message.Message,), dict(
  DESCRIPTOR = _ES_PERF_SET_FILTER_MASK_PB,
  __module__ = '_py_es_perf_set_filter_mask_pb2'
  # @@protoc_insertion_point(class_scope:es_perf_set_filter_mask_pb)
  ))
_sym_db.RegisterMessage(es_perf_set_filter_mask_pb)


# @@protoc_insertion_point(module_scope)