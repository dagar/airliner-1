# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_PX4_VehicleControlModeMsg_t.proto

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
  name='_py_PX4_VehicleControlModeMsg_t.proto',
  package='',
  serialized_pb=_b('\n%_py_PX4_VehicleControlModeMsg_t.proto\"\xce\x04\n\x1ePX4_VehicleControlModeMsg_t_pb\x12 \n\x18\x45xternalManualOverrideOk\x18\x01 \x02(\x08\x12\x1e\n\x16\x43ontrolAltitudeEnabled\x18\x02 \x02(\x08\x12\x1a\n\x12\x43ontrolAutoEnabled\x18\x03 \x02(\x08\x12\x1e\n\x16\x43ontrolFixedHdgEnabled\x18\x04 \x02(\x08\x12\"\n\x1a\x43ontrolAccelerationEnabled\x18\x05 \x02(\x08\x12\x18\n\x10SystemHilEnabled\x18\x06 \x02(\x08\x12\x1b\n\x13\x43ontrolRatesEnabled\x18\x07 \x02(\x08\x12\x1c\n\x14\x43ontrolManualEnabled\x18\x08 \x02(\x08\x12!\n\x19\x43ontrolTerminationEnabled\x18\t \x02(\x08\x12\x1e\n\x16\x43ontrolVelocityEnabled\x18\n \x02(\x08\x12\x1b\n\x13\x43ontrolForceEnabled\x18\x0b \x02(\x08\x12\x11\n\tTimestamp\x18\x0c \x02(\x04\x12\x1f\n\x17\x43ontrolRattitudeEnabled\x18\r \x02(\x08\x12\x1f\n\x17\x43ontrolClimbRateEnabled\x18\x0e \x02(\x08\x12\x1e\n\x16\x43ontrolAttitudeEnabled\x18\x0f \x02(\x08\x12\x1e\n\x16\x43ontrolOffboardEnabled\x18\x10 \x02(\x08\x12\r\n\x05\x41rmed\x18\x11 \x02(\x08\x12\x11\n\tTlmHeader\x18\x12 \x03(\r\x12\x1e\n\x16\x43ontrolPositionEnabled\x18\x13 \x02(\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PX4_VEHICLECONTROLMODEMSG_T_PB = _descriptor.Descriptor(
  name='PX4_VehicleControlModeMsg_t_pb',
  full_name='PX4_VehicleControlModeMsg_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ExternalManualOverrideOk', full_name='PX4_VehicleControlModeMsg_t_pb.ExternalManualOverrideOk', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlAltitudeEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlAltitudeEnabled', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlAutoEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlAutoEnabled', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlFixedHdgEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlFixedHdgEnabled', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlAccelerationEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlAccelerationEnabled', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SystemHilEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.SystemHilEnabled', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlRatesEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlRatesEnabled', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlManualEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlManualEnabled', index=7,
      number=8, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlTerminationEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlTerminationEnabled', index=8,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlVelocityEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlVelocityEnabled', index=9,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlForceEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlForceEnabled', index=10,
      number=11, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='PX4_VehicleControlModeMsg_t_pb.Timestamp', index=11,
      number=12, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlRattitudeEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlRattitudeEnabled', index=12,
      number=13, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlClimbRateEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlClimbRateEnabled', index=13,
      number=14, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlAttitudeEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlAttitudeEnabled', index=14,
      number=15, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlOffboardEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlOffboardEnabled', index=15,
      number=16, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Armed', full_name='PX4_VehicleControlModeMsg_t_pb.Armed', index=16,
      number=17, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='PX4_VehicleControlModeMsg_t_pb.TlmHeader', index=17,
      number=18, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlPositionEnabled', full_name='PX4_VehicleControlModeMsg_t_pb.ControlPositionEnabled', index=18,
      number=19, type=8, cpp_type=7, label=2,
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
  serialized_start=42,
  serialized_end=632,
)

DESCRIPTOR.message_types_by_name['PX4_VehicleControlModeMsg_t_pb'] = _PX4_VEHICLECONTROLMODEMSG_T_PB

PX4_VehicleControlModeMsg_t_pb = _reflection.GeneratedProtocolMessageType('PX4_VehicleControlModeMsg_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _PX4_VEHICLECONTROLMODEMSG_T_PB,
  __module__ = '_py_PX4_VehicleControlModeMsg_t_pb2'
  # @@protoc_insertion_point(class_scope:PX4_VehicleControlModeMsg_t_pb)
  ))
_sym_db.RegisterMessage(PX4_VehicleControlModeMsg_t_pb)


# @@protoc_insertion_point(module_scope)