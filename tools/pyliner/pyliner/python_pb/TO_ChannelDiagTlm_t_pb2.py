# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_TO_ChannelDiagTlm_t.proto

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
  name='_py_TO_ChannelDiagTlm_t.proto',
  package='',
  serialized_pb=_b('\n\x1d_py_TO_ChannelDiagTlm_t.proto\"|\n\x1aTO_MessageFlowDiagTlm_t_pb\x12\x10\n\x08MsgLimit\x18\x01 \x02(\r\x12\r\n\x05MsgId\x18\x02 \x02(\r\x12\x15\n\rDroppedMsgCnt\x18\x03 \x02(\r\x12\x14\n\x0cQueuedMsgCnt\x18\x04 \x02(\r\x12\x10\n\x08PQueueID\x18\x05 \x02(\r\"b\n\x1aTO_OutputQueueDiagTlm_t_pb\x12\x1a\n\x12\x43urrentlyQueuedCnt\x18\x01 \x02(\r\x12\x11\n\tSentCount\x18\x02 \x02(\r\x12\x15\n\rHighwaterMark\x18\x03 \x02(\r\"\xa9\x01\n\x17TO_PriorityDiagTlm_t_pb\x12\x15\n\rHighwaterMark\x18\x01 \x02(\r\x12\x1a\n\x12\x43urrentlyQueuedCnt\x18\x02 \x02(\r\x12\x14\n\x0cQueuedMsgCnt\x18\x03 \x02(\r\x12\r\n\x05State\x18\x04 \x02(\r\x12\x15\n\rDroppedMsgCnt\x18\x05 \x02(\r\x12\x10\n\x08MsgLimit\x18\x06 \x02(\r\x12\r\n\x05QType\x18\x07 \x02(\r\"\xc7\x02\n\x16TO_ChannelDiagTlm_t_pb\x12\r\n\x05Index\x18\x01 \x02(\r\x12(\n\x06PQueue\x18\x02 \x03(\x0b\x32\x18.TO_PriorityDiagTlm_t_pb\x12\x13\n\x0bucTlmHeader\x18\x03 \x03(\r\x12\x1b\n\x13\x43onfigTableFileName\x18\x04 \x03(\t\x12\x30\n\x0bMessageFlow\x18\x05 \x03(\x0b\x32\x1b.TO_MessageFlowDiagTlm_t_pb\x12\r\n\x05State\x18\x06 \x02(\r\x12\x0f\n\x07TableID\x18\x07 \x02(\r\x12\x15\n\rDumpTableName\x18\x08 \x03(\t\x12+\n\x06OQueue\x18\t \x02(\x0b\x32\x1b.TO_OutputQueueDiagTlm_t_pb\x12\x17\n\x0f\x43onfigTableName\x18\n \x03(\t\x12\x13\n\x0b\x43hannelName\x18\x0b \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TO_MESSAGEFLOWDIAGTLM_T_PB = _descriptor.Descriptor(
  name='TO_MessageFlowDiagTlm_t_pb',
  full_name='TO_MessageFlowDiagTlm_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MsgLimit', full_name='TO_MessageFlowDiagTlm_t_pb.MsgLimit', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MsgId', full_name='TO_MessageFlowDiagTlm_t_pb.MsgId', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DroppedMsgCnt', full_name='TO_MessageFlowDiagTlm_t_pb.DroppedMsgCnt', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='QueuedMsgCnt', full_name='TO_MessageFlowDiagTlm_t_pb.QueuedMsgCnt', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PQueueID', full_name='TO_MessageFlowDiagTlm_t_pb.PQueueID', index=4,
      number=5, type=13, cpp_type=3, label=2,
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
  serialized_end=157,
)


_TO_OUTPUTQUEUEDIAGTLM_T_PB = _descriptor.Descriptor(
  name='TO_OutputQueueDiagTlm_t_pb',
  full_name='TO_OutputQueueDiagTlm_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='CurrentlyQueuedCnt', full_name='TO_OutputQueueDiagTlm_t_pb.CurrentlyQueuedCnt', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SentCount', full_name='TO_OutputQueueDiagTlm_t_pb.SentCount', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HighwaterMark', full_name='TO_OutputQueueDiagTlm_t_pb.HighwaterMark', index=2,
      number=3, type=13, cpp_type=3, label=2,
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
  serialized_start=159,
  serialized_end=257,
)


_TO_PRIORITYDIAGTLM_T_PB = _descriptor.Descriptor(
  name='TO_PriorityDiagTlm_t_pb',
  full_name='TO_PriorityDiagTlm_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='HighwaterMark', full_name='TO_PriorityDiagTlm_t_pb.HighwaterMark', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CurrentlyQueuedCnt', full_name='TO_PriorityDiagTlm_t_pb.CurrentlyQueuedCnt', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='QueuedMsgCnt', full_name='TO_PriorityDiagTlm_t_pb.QueuedMsgCnt', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='State', full_name='TO_PriorityDiagTlm_t_pb.State', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DroppedMsgCnt', full_name='TO_PriorityDiagTlm_t_pb.DroppedMsgCnt', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MsgLimit', full_name='TO_PriorityDiagTlm_t_pb.MsgLimit', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='QType', full_name='TO_PriorityDiagTlm_t_pb.QType', index=6,
      number=7, type=13, cpp_type=3, label=2,
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
  serialized_start=260,
  serialized_end=429,
)


_TO_CHANNELDIAGTLM_T_PB = _descriptor.Descriptor(
  name='TO_ChannelDiagTlm_t_pb',
  full_name='TO_ChannelDiagTlm_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Index', full_name='TO_ChannelDiagTlm_t_pb.Index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PQueue', full_name='TO_ChannelDiagTlm_t_pb.PQueue', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ucTlmHeader', full_name='TO_ChannelDiagTlm_t_pb.ucTlmHeader', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ConfigTableFileName', full_name='TO_ChannelDiagTlm_t_pb.ConfigTableFileName', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MessageFlow', full_name='TO_ChannelDiagTlm_t_pb.MessageFlow', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='State', full_name='TO_ChannelDiagTlm_t_pb.State', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TableID', full_name='TO_ChannelDiagTlm_t_pb.TableID', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DumpTableName', full_name='TO_ChannelDiagTlm_t_pb.DumpTableName', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OQueue', full_name='TO_ChannelDiagTlm_t_pb.OQueue', index=8,
      number=9, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ConfigTableName', full_name='TO_ChannelDiagTlm_t_pb.ConfigTableName', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChannelName', full_name='TO_ChannelDiagTlm_t_pb.ChannelName', index=10,
      number=11, type=9, cpp_type=9, label=3,
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
  serialized_start=432,
  serialized_end=759,
)

_TO_CHANNELDIAGTLM_T_PB.fields_by_name['PQueue'].message_type = _TO_PRIORITYDIAGTLM_T_PB
_TO_CHANNELDIAGTLM_T_PB.fields_by_name['MessageFlow'].message_type = _TO_MESSAGEFLOWDIAGTLM_T_PB
_TO_CHANNELDIAGTLM_T_PB.fields_by_name['OQueue'].message_type = _TO_OUTPUTQUEUEDIAGTLM_T_PB
DESCRIPTOR.message_types_by_name['TO_MessageFlowDiagTlm_t_pb'] = _TO_MESSAGEFLOWDIAGTLM_T_PB
DESCRIPTOR.message_types_by_name['TO_OutputQueueDiagTlm_t_pb'] = _TO_OUTPUTQUEUEDIAGTLM_T_PB
DESCRIPTOR.message_types_by_name['TO_PriorityDiagTlm_t_pb'] = _TO_PRIORITYDIAGTLM_T_PB
DESCRIPTOR.message_types_by_name['TO_ChannelDiagTlm_t_pb'] = _TO_CHANNELDIAGTLM_T_PB

TO_MessageFlowDiagTlm_t_pb = _reflection.GeneratedProtocolMessageType('TO_MessageFlowDiagTlm_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _TO_MESSAGEFLOWDIAGTLM_T_PB,
  __module__ = '_py_TO_ChannelDiagTlm_t_pb2'
  # @@protoc_insertion_point(class_scope:TO_MessageFlowDiagTlm_t_pb)
  ))
_sym_db.RegisterMessage(TO_MessageFlowDiagTlm_t_pb)

TO_OutputQueueDiagTlm_t_pb = _reflection.GeneratedProtocolMessageType('TO_OutputQueueDiagTlm_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _TO_OUTPUTQUEUEDIAGTLM_T_PB,
  __module__ = '_py_TO_ChannelDiagTlm_t_pb2'
  # @@protoc_insertion_point(class_scope:TO_OutputQueueDiagTlm_t_pb)
  ))
_sym_db.RegisterMessage(TO_OutputQueueDiagTlm_t_pb)

TO_PriorityDiagTlm_t_pb = _reflection.GeneratedProtocolMessageType('TO_PriorityDiagTlm_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _TO_PRIORITYDIAGTLM_T_PB,
  __module__ = '_py_TO_ChannelDiagTlm_t_pb2'
  # @@protoc_insertion_point(class_scope:TO_PriorityDiagTlm_t_pb)
  ))
_sym_db.RegisterMessage(TO_PriorityDiagTlm_t_pb)

TO_ChannelDiagTlm_t_pb = _reflection.GeneratedProtocolMessageType('TO_ChannelDiagTlm_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _TO_CHANNELDIAGTLM_T_PB,
  __module__ = '_py_TO_ChannelDiagTlm_t_pb2'
  # @@protoc_insertion_point(class_scope:TO_ChannelDiagTlm_t_pb)
  ))
_sym_db.RegisterMessage(TO_ChannelDiagTlm_t_pb)


# @@protoc_insertion_point(module_scope)