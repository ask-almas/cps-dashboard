# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensoris/protobuf/categories/driving_behavior.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sensoris.protobuf.types import base_pb2 as sensoris_dot_protobuf_dot_types_dot_base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensoris/protobuf/categories/driving_behavior.proto',
  package='sensoris.protobuf.categories.drivingbehavior',
  syntax='proto3',
  serialized_options=b'\n\'org.sensoris.categories.drivingbehaviorB\037SensorisDrivingBehaviorCategoryP\001\370\001\001',
  serialized_pb=b'\n3sensoris/protobuf/categories/driving_behavior.proto\x12,sensoris.protobuf.categories.drivingbehavior\x1a\"sensoris/protobuf/types/base.proto\"\x84\x07\n\rParkingStatus\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12n\n\x15status_and_confidence\x18\x02 \x01(\x0b\x32O.sensoris.protobuf.categories.drivingbehavior.ParkingStatus.StatusAndConfidence\x12t\n\x18\x64irection_and_confidence\x18\x03 \x01(\x0b\x32R.sensoris.protobuf.categories.drivingbehavior.ParkingStatus.DirectionAndConfidence\x12X\n\x15\x64uration_and_accuracy\x18\x04 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x00\x1a\xec\x01\n\x13StatusAndConfidence\x12\x62\n\x04type\x18\x01 \x01(\x0e\x32T.sensoris.protobuf.categories.drivingbehavior.ParkingStatus.StatusAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"3\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0b\n\x07PARK_IN\x10\x01\x12\x0c\n\x08PARK_OUT\x10\x02\x1a\x84\x02\n\x16\x44irectionAndConfidence\x12\x65\n\x04type\x18\x01 \x01(\x0e\x32W.sensoris.protobuf.categories.drivingbehavior.ParkingStatus.DirectionAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"E\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x10\n\x0cLONGITUDINAL\x10\x01\x12\x0b\n\x07LATERAL\x10\x02\x12\x0c\n\x08\x44IAGONAL\x10\x03\"\xb0\x01\n\x17\x44rivingBehaviorCategory\x12@\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32..sensoris.protobuf.types.base.CategoryEnvelope\x12S\n\x0eparking_status\x18\x02 \x03(\x0b\x32;.sensoris.protobuf.categories.drivingbehavior.ParkingStatusBO\n\'org.sensoris.categories.drivingbehaviorB\x1fSensorisDrivingBehaviorCategoryP\x01\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[sensoris_dot_protobuf_dot_types_dot_base__pb2.DESCRIPTOR,])



_PARKINGSTATUS_STATUSANDCONFIDENCE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.StatusAndConfidence.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARK_IN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARK_OUT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=724,
  serialized_end=775,
)
_sym_db.RegisterEnumDescriptor(_PARKINGSTATUS_STATUSANDCONFIDENCE_TYPE)

_PARKINGSTATUS_DIRECTIONANDCONFIDENCE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.DirectionAndConfidence.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LONGITUDINAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LATERAL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIAGONAL', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=969,
  serialized_end=1038,
)
_sym_db.RegisterEnumDescriptor(_PARKINGSTATUS_DIRECTIONANDCONFIDENCE_TYPE)


_PARKINGSTATUS_STATUSANDCONFIDENCE = _descriptor.Descriptor(
  name='StatusAndConfidence',
  full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.StatusAndConfidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.StatusAndConfidence.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.StatusAndConfidence.confidence', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PARKINGSTATUS_STATUSANDCONFIDENCE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=775,
)

_PARKINGSTATUS_DIRECTIONANDCONFIDENCE = _descriptor.Descriptor(
  name='DirectionAndConfidence',
  full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.DirectionAndConfidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.DirectionAndConfidence.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.DirectionAndConfidence.confidence', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PARKINGSTATUS_DIRECTIONANDCONFIDENCE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=1038,
)

_PARKINGSTATUS = _descriptor.Descriptor(
  name='ParkingStatus',
  full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_and_confidence', full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.status_and_confidence', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction_and_confidence', full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.direction_and_confidence', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_and_accuracy', full_name='sensoris.protobuf.categories.drivingbehavior.ParkingStatus.duration_and_accuracy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\000', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PARKINGSTATUS_STATUSANDCONFIDENCE, _PARKINGSTATUS_DIRECTIONANDCONFIDENCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=1038,
)


_DRIVINGBEHAVIORCATEGORY = _descriptor.Descriptor(
  name='DrivingBehaviorCategory',
  full_name='sensoris.protobuf.categories.drivingbehavior.DrivingBehaviorCategory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.drivingbehavior.DrivingBehaviorCategory.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parking_status', full_name='sensoris.protobuf.categories.drivingbehavior.DrivingBehaviorCategory.parking_status', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1041,
  serialized_end=1217,
)

_PARKINGSTATUS_STATUSANDCONFIDENCE.fields_by_name['type'].enum_type = _PARKINGSTATUS_STATUSANDCONFIDENCE_TYPE
_PARKINGSTATUS_STATUSANDCONFIDENCE.fields_by_name['confidence'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CONFIDENCE
_PARKINGSTATUS_STATUSANDCONFIDENCE.containing_type = _PARKINGSTATUS
_PARKINGSTATUS_STATUSANDCONFIDENCE_TYPE.containing_type = _PARKINGSTATUS_STATUSANDCONFIDENCE
_PARKINGSTATUS_DIRECTIONANDCONFIDENCE.fields_by_name['type'].enum_type = _PARKINGSTATUS_DIRECTIONANDCONFIDENCE_TYPE
_PARKINGSTATUS_DIRECTIONANDCONFIDENCE.fields_by_name['confidence'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CONFIDENCE
_PARKINGSTATUS_DIRECTIONANDCONFIDENCE.containing_type = _PARKINGSTATUS
_PARKINGSTATUS_DIRECTIONANDCONFIDENCE_TYPE.containing_type = _PARKINGSTATUS_DIRECTIONANDCONFIDENCE
_PARKINGSTATUS.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_PARKINGSTATUS.fields_by_name['status_and_confidence'].message_type = _PARKINGSTATUS_STATUSANDCONFIDENCE
_PARKINGSTATUS.fields_by_name['direction_and_confidence'].message_type = _PARKINGSTATUS_DIRECTIONANDCONFIDENCE
_PARKINGSTATUS.fields_by_name['duration_and_accuracy'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._INT64VALUEANDACCURACY
_DRIVINGBEHAVIORCATEGORY.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CATEGORYENVELOPE
_DRIVINGBEHAVIORCATEGORY.fields_by_name['parking_status'].message_type = _PARKINGSTATUS
DESCRIPTOR.message_types_by_name['ParkingStatus'] = _PARKINGSTATUS
DESCRIPTOR.message_types_by_name['DrivingBehaviorCategory'] = _DRIVINGBEHAVIORCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParkingStatus = _reflection.GeneratedProtocolMessageType('ParkingStatus', (_message.Message,), {

  'StatusAndConfidence' : _reflection.GeneratedProtocolMessageType('StatusAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _PARKINGSTATUS_STATUSANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.driving_behavior_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.drivingbehavior.ParkingStatus.StatusAndConfidence)
    })
  ,

  'DirectionAndConfidence' : _reflection.GeneratedProtocolMessageType('DirectionAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _PARKINGSTATUS_DIRECTIONANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.driving_behavior_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.drivingbehavior.ParkingStatus.DirectionAndConfidence)
    })
  ,
  'DESCRIPTOR' : _PARKINGSTATUS,
  '__module__' : 'sensoris.protobuf.categories.driving_behavior_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.drivingbehavior.ParkingStatus)
  })
_sym_db.RegisterMessage(ParkingStatus)
_sym_db.RegisterMessage(ParkingStatus.StatusAndConfidence)
_sym_db.RegisterMessage(ParkingStatus.DirectionAndConfidence)

DrivingBehaviorCategory = _reflection.GeneratedProtocolMessageType('DrivingBehaviorCategory', (_message.Message,), {
  'DESCRIPTOR' : _DRIVINGBEHAVIORCATEGORY,
  '__module__' : 'sensoris.protobuf.categories.driving_behavior_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.drivingbehavior.DrivingBehaviorCategory)
  })
_sym_db.RegisterMessage(DrivingBehaviorCategory)


DESCRIPTOR._options = None
_PARKINGSTATUS.fields_by_name['duration_and_accuracy']._options = None
# @@protoc_insertion_point(module_scope)