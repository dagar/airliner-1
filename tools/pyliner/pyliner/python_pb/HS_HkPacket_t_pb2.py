# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_HS_HkPacket_t.proto

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
  name='_py_HS_HkPacket_t.proto',
  package='',
  serialized_pb=_b('\n\x17_py_HS_HkPacket_t.proto\"\xb9\x03\n\x10HS_HkPacket_t_pb\x12\x13\n\x0b\x43mdErrCount\x18\x01 \x02(\r\x12\x1a\n\x12\x43urrentAppMonState\x18\x02 \x02(\r\x12\x1c\n\x14\x43urrentEventMonState\x18\x03 \x02(\r\x12\x1c\n\x14\x45ventsMonitoredCount\x18\x04 \x02(\r\x12\x12\n\nSpareBytes\x18\x05 \x02(\r\x12\x13\n\x0bUtilCpuPeak\x18\x06 \x02(\r\x12\x15\n\rAppMonEnables\x18\x07 \x03(\r\x12\x1a\n\x12\x43urrentCPUHogState\x18\x08 \x02(\r\x12\x12\n\nMsgActExec\x18\t \x02(\r\x12\x17\n\x0fResetsPerformed\x18\n \x02(\r\x12\x11\n\tTlmHeader\x18\x0b \x03(\r\x12\x12\n\nUtilCpuAvg\x18\x0c \x02(\r\x12\x11\n\tExeCounts\x18\r \x03(\r\x12\x1c\n\x14InvalidEventMonCount\x18\x0e \x02(\r\x12\x13\n\x0bStatusFlags\x18\x0f \x02(\r\x12\x11\n\tMaxResets\x18\x10 \x02(\r\x12\x10\n\x08\x43mdCount\x18\x11 \x02(\r\x12\x1d\n\x15\x43urrentAlivenessState\x18\x12 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HS_HKPACKET_T_PB = _descriptor.Descriptor(
  name='HS_HkPacket_t_pb',
  full_name='HS_HkPacket_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='CmdErrCount', full_name='HS_HkPacket_t_pb.CmdErrCount', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CurrentAppMonState', full_name='HS_HkPacket_t_pb.CurrentAppMonState', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CurrentEventMonState', full_name='HS_HkPacket_t_pb.CurrentEventMonState', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EventsMonitoredCount', full_name='HS_HkPacket_t_pb.EventsMonitoredCount', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpareBytes', full_name='HS_HkPacket_t_pb.SpareBytes', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UtilCpuPeak', full_name='HS_HkPacket_t_pb.UtilCpuPeak', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppMonEnables', full_name='HS_HkPacket_t_pb.AppMonEnables', index=6,
      number=7, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CurrentCPUHogState', full_name='HS_HkPacket_t_pb.CurrentCPUHogState', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MsgActExec', full_name='HS_HkPacket_t_pb.MsgActExec', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ResetsPerformed', full_name='HS_HkPacket_t_pb.ResetsPerformed', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='HS_HkPacket_t_pb.TlmHeader', index=10,
      number=11, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UtilCpuAvg', full_name='HS_HkPacket_t_pb.UtilCpuAvg', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ExeCounts', full_name='HS_HkPacket_t_pb.ExeCounts', index=12,
      number=13, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='InvalidEventMonCount', full_name='HS_HkPacket_t_pb.InvalidEventMonCount', index=13,
      number=14, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StatusFlags', full_name='HS_HkPacket_t_pb.StatusFlags', index=14,
      number=15, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MaxResets', full_name='HS_HkPacket_t_pb.MaxResets', index=15,
      number=16, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdCount', full_name='HS_HkPacket_t_pb.CmdCount', index=16,
      number=17, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CurrentAlivenessState', full_name='HS_HkPacket_t_pb.CurrentAlivenessState', index=17,
      number=18, type=13, cpp_type=3, label=2,
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
  serialized_start=28,
  serialized_end=469,
)

DESCRIPTOR.message_types_by_name['HS_HkPacket_t_pb'] = _HS_HKPACKET_T_PB

HS_HkPacket_t_pb = _reflection.GeneratedProtocolMessageType('HS_HkPacket_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _HS_HKPACKET_T_PB,
  __module__ = '_py_HS_HkPacket_t_pb2'
  # @@protoc_insertion_point(class_scope:HS_HkPacket_t_pb)
  ))
_sym_db.RegisterMessage(HS_HkPacket_t_pb)


# @@protoc_insertion_point(module_scope)