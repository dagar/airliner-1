# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_LC_OperData_t.proto

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
  name='_py_LC_OperData_t.proto',
  package='',
  serialized_pb=_b('\n\x17_py_LC_OperData_t.proto\"F\n\x13LC_WatchPtList_t_pb\x12\x12\n\nWatchIndex\x18\x01 \x02(\r\x12\r\n\x05Spare\x18\x02 \x02(\r\x12\x0c\n\x04Next\x18\x03 \x02(\r\"\xb1\x02\n\x10LC_HkPacket_t_pb\x12\x13\n\x0b\x43mdErrCount\x18\x01 \x02(\r\x12\x11\n\tAPResults\x18\x02 \x03(\r\x12\x11\n\tActiveAPs\x18\x03 \x02(\r\x12\x10\n\x08WPsInUse\x18\x04 \x02(\r\x12\x15\n\rAPSampleCount\x18\x05 \x02(\r\x12\r\n\x05Pad16\x18\x06 \x02(\r\x12\x16\n\x0e\x43urrentLCState\x18\x07 \x02(\r\x12\x11\n\tTlmHeader\x18\x08 \x03(\r\x12\x19\n\x11MonitoredMsgCount\x18\t \x02(\r\x12\x10\n\x08\x43mdCount\x18\n \x02(\r\x12\x1b\n\x13PassiveRTSExecCount\x18\x0b \x02(\r\x12\x0c\n\x04Pad8\x18\x0c \x02(\r\x12\x14\n\x0cRTSExecCount\x18\r \x02(\r\x12\x11\n\tWPResults\x18\x0e \x03(\r\"Z\n\x13LC_MessageList_t_pb\x12\x11\n\tMessageID\x18\x01 \x02(\r\x12\r\n\x05Spare\x18\x02 \x02(\r\x12\x13\n\x0bWatchPtList\x18\x03 \x02(\r\x12\x0c\n\x04Next\x18\x04 \x02(\r\"\xfc\x03\n\x10LC_OperData_t_pb\x12\x18\n\x10WRTDataCDSHandle\x18\x01 \x02(\r\x12\x0e\n\x06WRTPtr\x18\x02 \x02(\r\x12\x0e\n\x06\x41RTPtr\x18\x03 \x02(\r\x12\x0e\n\x06MsgPtr\x18\x04 \x02(\r\x12\x18\n\x10\x41RTDataCDSHandle\x18\x05 \x02(\r\x12\x11\n\tARTHandle\x18\x06 \x02(\x05\x12\x17\n\x0fWatchpointCount\x18\x07 \x02(\r\x12\x0f\n\x07\x43mdPipe\x18\x08 \x02(\t\x12*\n\x0cWatchPtLinks\x18\t \x03(\x0b\x32\x14.LC_WatchPtList_t_pb\x12\x11\n\tWRTHandle\x18\n \x02(\x05\x12\x17\n\x0fMessageIDsCount\x18\x0b \x02(\r\x12\x14\n\x0cTableResults\x18\x0c \x02(\r\x12\x0e\n\x06\x41\x44TPtr\x18\r \x02(\r\x12*\n\x0cMessageLinks\x18\x0e \x03(\x0b\x32\x14.LC_MessageList_t_pb\x12\x11\n\tHashTable\x18\x0f \x03(\r\x12\x15\n\rHaveActiveCDS\x18\x10 \x02(\x08\x12\x11\n\tWDTHandle\x18\x11 \x02(\x05\x12\x18\n\x10\x41ppDataCDSHandle\x18\x12 \x02(\r\x12\x0e\n\x06WDTPtr\x18\x13 \x02(\r\x12\x11\n\tADTHandle\x18\x14 \x02(\x05\x12#\n\x08HkPacket\x18\x15 \x02(\x0b\x32\x11.LC_HkPacket_t_pb')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LC_WATCHPTLIST_T_PB = _descriptor.Descriptor(
  name='LC_WatchPtList_t_pb',
  full_name='LC_WatchPtList_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='WatchIndex', full_name='LC_WatchPtList_t_pb.WatchIndex', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Spare', full_name='LC_WatchPtList_t_pb.Spare', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Next', full_name='LC_WatchPtList_t_pb.Next', index=2,
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
  serialized_start=27,
  serialized_end=97,
)


_LC_HKPACKET_T_PB = _descriptor.Descriptor(
  name='LC_HkPacket_t_pb',
  full_name='LC_HkPacket_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='CmdErrCount', full_name='LC_HkPacket_t_pb.CmdErrCount', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='APResults', full_name='LC_HkPacket_t_pb.APResults', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ActiveAPs', full_name='LC_HkPacket_t_pb.ActiveAPs', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WPsInUse', full_name='LC_HkPacket_t_pb.WPsInUse', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='APSampleCount', full_name='LC_HkPacket_t_pb.APSampleCount', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pad16', full_name='LC_HkPacket_t_pb.Pad16', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CurrentLCState', full_name='LC_HkPacket_t_pb.CurrentLCState', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='LC_HkPacket_t_pb.TlmHeader', index=7,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MonitoredMsgCount', full_name='LC_HkPacket_t_pb.MonitoredMsgCount', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdCount', full_name='LC_HkPacket_t_pb.CmdCount', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PassiveRTSExecCount', full_name='LC_HkPacket_t_pb.PassiveRTSExecCount', index=10,
      number=11, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pad8', full_name='LC_HkPacket_t_pb.Pad8', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RTSExecCount', full_name='LC_HkPacket_t_pb.RTSExecCount', index=12,
      number=13, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WPResults', full_name='LC_HkPacket_t_pb.WPResults', index=13,
      number=14, type=13, cpp_type=3, label=3,
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
  serialized_start=100,
  serialized_end=405,
)


_LC_MESSAGELIST_T_PB = _descriptor.Descriptor(
  name='LC_MessageList_t_pb',
  full_name='LC_MessageList_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MessageID', full_name='LC_MessageList_t_pb.MessageID', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Spare', full_name='LC_MessageList_t_pb.Spare', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WatchPtList', full_name='LC_MessageList_t_pb.WatchPtList', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Next', full_name='LC_MessageList_t_pb.Next', index=3,
      number=4, type=13, cpp_type=3, label=2,
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
  serialized_start=407,
  serialized_end=497,
)


_LC_OPERDATA_T_PB = _descriptor.Descriptor(
  name='LC_OperData_t_pb',
  full_name='LC_OperData_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='WRTDataCDSHandle', full_name='LC_OperData_t_pb.WRTDataCDSHandle', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WRTPtr', full_name='LC_OperData_t_pb.WRTPtr', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ARTPtr', full_name='LC_OperData_t_pb.ARTPtr', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MsgPtr', full_name='LC_OperData_t_pb.MsgPtr', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ARTDataCDSHandle', full_name='LC_OperData_t_pb.ARTDataCDSHandle', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ARTHandle', full_name='LC_OperData_t_pb.ARTHandle', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WatchpointCount', full_name='LC_OperData_t_pb.WatchpointCount', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdPipe', full_name='LC_OperData_t_pb.CmdPipe', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WatchPtLinks', full_name='LC_OperData_t_pb.WatchPtLinks', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WRTHandle', full_name='LC_OperData_t_pb.WRTHandle', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MessageIDsCount', full_name='LC_OperData_t_pb.MessageIDsCount', index=10,
      number=11, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TableResults', full_name='LC_OperData_t_pb.TableResults', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ADTPtr', full_name='LC_OperData_t_pb.ADTPtr', index=12,
      number=13, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MessageLinks', full_name='LC_OperData_t_pb.MessageLinks', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HashTable', full_name='LC_OperData_t_pb.HashTable', index=14,
      number=15, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HaveActiveCDS', full_name='LC_OperData_t_pb.HaveActiveCDS', index=15,
      number=16, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WDTHandle', full_name='LC_OperData_t_pb.WDTHandle', index=16,
      number=17, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppDataCDSHandle', full_name='LC_OperData_t_pb.AppDataCDSHandle', index=17,
      number=18, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WDTPtr', full_name='LC_OperData_t_pb.WDTPtr', index=18,
      number=19, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ADTHandle', full_name='LC_OperData_t_pb.ADTHandle', index=19,
      number=20, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HkPacket', full_name='LC_OperData_t_pb.HkPacket', index=20,
      number=21, type=11, cpp_type=10, label=2,
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
  serialized_start=500,
  serialized_end=1008,
)

_LC_OPERDATA_T_PB.fields_by_name['WatchPtLinks'].message_type = _LC_WATCHPTLIST_T_PB
_LC_OPERDATA_T_PB.fields_by_name['MessageLinks'].message_type = _LC_MESSAGELIST_T_PB
_LC_OPERDATA_T_PB.fields_by_name['HkPacket'].message_type = _LC_HKPACKET_T_PB
DESCRIPTOR.message_types_by_name['LC_WatchPtList_t_pb'] = _LC_WATCHPTLIST_T_PB
DESCRIPTOR.message_types_by_name['LC_HkPacket_t_pb'] = _LC_HKPACKET_T_PB
DESCRIPTOR.message_types_by_name['LC_MessageList_t_pb'] = _LC_MESSAGELIST_T_PB
DESCRIPTOR.message_types_by_name['LC_OperData_t_pb'] = _LC_OPERDATA_T_PB

LC_WatchPtList_t_pb = _reflection.GeneratedProtocolMessageType('LC_WatchPtList_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _LC_WATCHPTLIST_T_PB,
  __module__ = '_py_LC_OperData_t_pb2'
  # @@protoc_insertion_point(class_scope:LC_WatchPtList_t_pb)
  ))
_sym_db.RegisterMessage(LC_WatchPtList_t_pb)

LC_HkPacket_t_pb = _reflection.GeneratedProtocolMessageType('LC_HkPacket_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _LC_HKPACKET_T_PB,
  __module__ = '_py_LC_OperData_t_pb2'
  # @@protoc_insertion_point(class_scope:LC_HkPacket_t_pb)
  ))
_sym_db.RegisterMessage(LC_HkPacket_t_pb)

LC_MessageList_t_pb = _reflection.GeneratedProtocolMessageType('LC_MessageList_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _LC_MESSAGELIST_T_PB,
  __module__ = '_py_LC_OperData_t_pb2'
  # @@protoc_insertion_point(class_scope:LC_MessageList_t_pb)
  ))
_sym_db.RegisterMessage(LC_MessageList_t_pb)

LC_OperData_t_pb = _reflection.GeneratedProtocolMessageType('LC_OperData_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _LC_OPERDATA_T_PB,
  __module__ = '_py_LC_OperData_t_pb2'
  # @@protoc_insertion_point(class_scope:LC_OperData_t_pb)
  ))
_sym_db.RegisterMessage(LC_OperData_t_pb)


# @@protoc_insertion_point(module_scope)