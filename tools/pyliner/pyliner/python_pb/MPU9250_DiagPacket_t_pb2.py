# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_MPU9250_DiagPacket_t.proto

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
  name='_py_MPU9250_DiagPacket_t.proto',
  package='',
  serialized_pb=_b('\n\x1e_py_MPU9250_DiagPacket_t.proto\"\xbe\x01\n\x1aMPU9250_ConversionMsg_t_pb\x12\x17\n\x0fTempSensitivity\x18\x01 \x02(\x02\x12\x11\n\tGyroScale\x18\x02 \x02(\r\x12\x0f\n\x07\x41\x63\x63Unit\x18\x03 \x02(\x02\x12\x13\n\x0bGyroDivider\x18\x04 \x02(\x02\x12\x12\n\nAccDivider\x18\x05 \x02(\x02\x12\x16\n\x0eRoomTempOffset\x18\x06 \x02(\x02\x12\x10\n\x08\x41\x63\x63Scale\x18\x07 \x02(\r\x12\x10\n\x08GyroUnit\x18\x08 \x02(\x02\"\x9f\x02\n\x1bMPU9250_CalibrationMsg_t_pb\x12\x11\n\tAccZScale\x18\x01 \x02(\x02\x12\x12\n\nGyroXScale\x18\x02 \x02(\x02\x12\x12\n\nGyroYScale\x18\x03 \x02(\x02\x12\x12\n\nAccYOffset\x18\x04 \x02(\x02\x12\x11\n\tAccXScale\x18\x05 \x02(\x02\x12\x13\n\x0bGyroYOffset\x18\x06 \x02(\x02\x12\x12\n\nAccXOffset\x18\x07 \x02(\x02\x12\x12\n\nGyroZScale\x18\x08 \x02(\x02\x12\x12\n\nAccZOffset\x18\t \x02(\x02\x12\x10\n\x08Rotation\x18\n \x02(\r\x12\x13\n\x0bGyroZOffset\x18\x0b \x02(\x02\x12\x13\n\x0bGyroXOffset\x18\x0c \x02(\x02\x12\x11\n\tAccYScale\x18\r \x02(\x02\"\x90\x01\n\x17MPU9250_DiagPacket_t_pb\x12/\n\nConversion\x18\x01 \x02(\x0b\x32\x1b.MPU9250_ConversionMsg_t_pb\x12\x11\n\tTlmHeader\x18\x02 \x03(\r\x12\x31\n\x0b\x43\x61libration\x18\x03 \x02(\x0b\x32\x1c.MPU9250_CalibrationMsg_t_pb')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MPU9250_CONVERSIONMSG_T_PB = _descriptor.Descriptor(
  name='MPU9250_ConversionMsg_t_pb',
  full_name='MPU9250_ConversionMsg_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TempSensitivity', full_name='MPU9250_ConversionMsg_t_pb.TempSensitivity', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GyroScale', full_name='MPU9250_ConversionMsg_t_pb.GyroScale', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccUnit', full_name='MPU9250_ConversionMsg_t_pb.AccUnit', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GyroDivider', full_name='MPU9250_ConversionMsg_t_pb.GyroDivider', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccDivider', full_name='MPU9250_ConversionMsg_t_pb.AccDivider', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RoomTempOffset', full_name='MPU9250_ConversionMsg_t_pb.RoomTempOffset', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccScale', full_name='MPU9250_ConversionMsg_t_pb.AccScale', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GyroUnit', full_name='MPU9250_ConversionMsg_t_pb.GyroUnit', index=7,
      number=8, type=2, cpp_type=6, label=2,
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
  serialized_start=35,
  serialized_end=225,
)


_MPU9250_CALIBRATIONMSG_T_PB = _descriptor.Descriptor(
  name='MPU9250_CalibrationMsg_t_pb',
  full_name='MPU9250_CalibrationMsg_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='AccZScale', full_name='MPU9250_CalibrationMsg_t_pb.AccZScale', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GyroXScale', full_name='MPU9250_CalibrationMsg_t_pb.GyroXScale', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GyroYScale', full_name='MPU9250_CalibrationMsg_t_pb.GyroYScale', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccYOffset', full_name='MPU9250_CalibrationMsg_t_pb.AccYOffset', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccXScale', full_name='MPU9250_CalibrationMsg_t_pb.AccXScale', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GyroYOffset', full_name='MPU9250_CalibrationMsg_t_pb.GyroYOffset', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccXOffset', full_name='MPU9250_CalibrationMsg_t_pb.AccXOffset', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GyroZScale', full_name='MPU9250_CalibrationMsg_t_pb.GyroZScale', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccZOffset', full_name='MPU9250_CalibrationMsg_t_pb.AccZOffset', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Rotation', full_name='MPU9250_CalibrationMsg_t_pb.Rotation', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GyroZOffset', full_name='MPU9250_CalibrationMsg_t_pb.GyroZOffset', index=10,
      number=11, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GyroXOffset', full_name='MPU9250_CalibrationMsg_t_pb.GyroXOffset', index=11,
      number=12, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccYScale', full_name='MPU9250_CalibrationMsg_t_pb.AccYScale', index=12,
      number=13, type=2, cpp_type=6, label=2,
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
  serialized_start=228,
  serialized_end=515,
)


_MPU9250_DIAGPACKET_T_PB = _descriptor.Descriptor(
  name='MPU9250_DiagPacket_t_pb',
  full_name='MPU9250_DiagPacket_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Conversion', full_name='MPU9250_DiagPacket_t_pb.Conversion', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='MPU9250_DiagPacket_t_pb.TlmHeader', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Calibration', full_name='MPU9250_DiagPacket_t_pb.Calibration', index=2,
      number=3, type=11, cpp_type=10, label=2,
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
  serialized_start=518,
  serialized_end=662,
)

_MPU9250_DIAGPACKET_T_PB.fields_by_name['Conversion'].message_type = _MPU9250_CONVERSIONMSG_T_PB
_MPU9250_DIAGPACKET_T_PB.fields_by_name['Calibration'].message_type = _MPU9250_CALIBRATIONMSG_T_PB
DESCRIPTOR.message_types_by_name['MPU9250_ConversionMsg_t_pb'] = _MPU9250_CONVERSIONMSG_T_PB
DESCRIPTOR.message_types_by_name['MPU9250_CalibrationMsg_t_pb'] = _MPU9250_CALIBRATIONMSG_T_PB
DESCRIPTOR.message_types_by_name['MPU9250_DiagPacket_t_pb'] = _MPU9250_DIAGPACKET_T_PB

MPU9250_ConversionMsg_t_pb = _reflection.GeneratedProtocolMessageType('MPU9250_ConversionMsg_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _MPU9250_CONVERSIONMSG_T_PB,
  __module__ = '_py_MPU9250_DiagPacket_t_pb2'
  # @@protoc_insertion_point(class_scope:MPU9250_ConversionMsg_t_pb)
  ))
_sym_db.RegisterMessage(MPU9250_ConversionMsg_t_pb)

MPU9250_CalibrationMsg_t_pb = _reflection.GeneratedProtocolMessageType('MPU9250_CalibrationMsg_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _MPU9250_CALIBRATIONMSG_T_PB,
  __module__ = '_py_MPU9250_DiagPacket_t_pb2'
  # @@protoc_insertion_point(class_scope:MPU9250_CalibrationMsg_t_pb)
  ))
_sym_db.RegisterMessage(MPU9250_CalibrationMsg_t_pb)

MPU9250_DiagPacket_t_pb = _reflection.GeneratedProtocolMessageType('MPU9250_DiagPacket_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _MPU9250_DIAGPACKET_T_PB,
  __module__ = '_py_MPU9250_DiagPacket_t_pb2'
  # @@protoc_insertion_point(class_scope:MPU9250_DiagPacket_t_pb)
  ))
_sym_db.RegisterMessage(MPU9250_DiagPacket_t_pb)


# @@protoc_insertion_point(module_scope)