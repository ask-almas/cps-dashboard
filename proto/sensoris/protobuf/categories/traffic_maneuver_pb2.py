# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensoris/protobuf/categories/traffic_maneuver.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sensoris.protobuf.types import base_pb2 as sensoris_dot_protobuf_dot_types_dot_base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensoris/protobuf/categories/traffic_maneuver.proto',
  package='sensoris.protobuf.categories.trafficmaneuver',
  syntax='proto3',
  serialized_options=b'\n\'org.sensoris.categories.trafficmaneuverB\037SensorisTrafficManeuverCategoryP\001\370\001\001',
  serialized_pb=b'\n3sensoris/protobuf/categories/traffic_maneuver.proto\x12,sensoris.protobuf.categories.trafficmaneuver\x1a\"sensoris/protobuf/types/base.proto\"\xf1\x04\n\x08Maneuver\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12\x65\n\x13type_and_confidence\x18\x02 \x01(\x0b\x32H.sensoris.protobuf.categories.trafficmaneuver.Maneuver.TypeAndConfidence\x1a\xbe\x03\n\x11TypeAndConfidence\x12[\n\x04type\x18\x01 \x01(\x0e\x32M.sensoris.protobuf.categories.trafficmaneuver.Maneuver.TypeAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"\x8d\x02\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0b\n\x07\x45VASIVE\x10\x01\x12\x0f\n\x0bLANE_CHANGE\x10\x02\x12\x15\n\x11LANE_CHANGE_RIGHT\x10\x03\x12\x14\n\x10LANE_CHANGE_LEFT\x10\x04\x12\x0e\n\nOVERTAKING\x10\x05\x12\x15\n\x11INTERSECTION_STOP\x10\x06\x12\x0b\n\x07TURNING\x10\x07\x12\x11\n\rTURNING_RIGHT\x10\x08\x12\x10\n\x0cTURNING_LEFT\x10\t\x12\x17\n\x13SHARP_TURNING_RIGHT\x10\n\x12\x16\n\x12SHARP_TURNING_LEFT\x10\x0b\x12\x10\n\x0c\x41\x43\x43\x45LERATING\x10\x0c\x12\x0c\n\x08\x42REAKING\x10\r\"\xb4\x03\n\x08\x43harging\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12I\n\x04type\x18\x02 \x01(\x0e\x32;.sensoris.protobuf.categories.trafficmaneuver.Charging.Type\x12W\n\x14voltage_and_accuracy\x18\x03 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x00\x12W\n\x14\x63urrent_and_accuracy\x18\x04 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x01\"l\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0e\n\nPORT_J1772\x10\x01\x12\x0b\n\x07\x43HADEMO\x10\x02\x12\r\n\tSAE_COMBO\x10\x03\x12\x0e\n\nTESLA_HPWC\x10\x04\x12\x16\n\x12TESLA_SUPERCHARGER\x10\x05\"\x86\x03\n\tRefueling\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12J\n\x04type\x18\x02 \x01(\x0e\x32<.sensoris.protobuf.categories.trafficmaneuver.Refueling.Type\x12`\n\x1dquantity_to_full_and_accuracy\x18\x03 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x01\"\x8b\x01\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x12\n\x0ePETROL_PREMIUM\x10\x01\x12\x10\n\x0cPETROL_SUPER\x10\x02\x12\n\n\x06\x44IESEL\x10\x03\x12\x07\n\x03LPG\x10\x04\x12\x07\n\x03\x43NG\x10\x05\x12\x0e\n\nBIO_DIESEL\x10\x06\x12\x0f\n\x0b\x42IO_ETHANOL\x10\x07\x12\x0c\n\x08HYDROGEN\x10\x08\"\xbb\x02\n\x17TrafficManeuverCategory\x12@\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32..sensoris.protobuf.types.base.CategoryEnvelope\x12H\n\x08maneuver\x18\x02 \x03(\x0b\x32\x36.sensoris.protobuf.categories.trafficmaneuver.Maneuver\x12H\n\x08\x63harging\x18\x03 \x03(\x0b\x32\x36.sensoris.protobuf.categories.trafficmaneuver.Charging\x12J\n\trefueling\x18\x04 \x03(\x0b\x32\x37.sensoris.protobuf.categories.trafficmaneuver.RefuelingBO\n\'org.sensoris.categories.trafficmaneuverB\x1fSensorisTrafficManeuverCategoryP\x01\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[sensoris_dot_protobuf_dot_types_dot_base__pb2.DESCRIPTOR,])



_MANEUVER_TYPEANDCONFIDENCE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensoris.protobuf.categories.trafficmaneuver.Maneuver.TypeAndConfidence.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVASIVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_RIGHT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_LEFT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERTAKING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERSECTION_STOP', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TURNING', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TURNING_RIGHT', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TURNING_LEFT', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARP_TURNING_RIGHT', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARP_TURNING_LEFT', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCELERATING', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BREAKING', index=13, number=13,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=494,
  serialized_end=763,
)
_sym_db.RegisterEnumDescriptor(_MANEUVER_TYPEANDCONFIDENCE_TYPE)

_CHARGING_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensoris.protobuf.categories.trafficmaneuver.Charging.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PORT_J1772', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHADEMO', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAE_COMBO', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TESLA_HPWC', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TESLA_SUPERCHARGER', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1094,
  serialized_end=1202,
)
_sym_db.RegisterEnumDescriptor(_CHARGING_TYPE)

_REFUELING_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensoris.protobuf.categories.trafficmaneuver.Refueling.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PETROL_PREMIUM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PETROL_SUPER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIESEL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LPG', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CNG', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIO_DIESEL', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIO_ETHANOL', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYDROGEN', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1456,
  serialized_end=1595,
)
_sym_db.RegisterEnumDescriptor(_REFUELING_TYPE)


_MANEUVER_TYPEANDCONFIDENCE = _descriptor.Descriptor(
  name='TypeAndConfidence',
  full_name='sensoris.protobuf.categories.trafficmaneuver.Maneuver.TypeAndConfidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sensoris.protobuf.categories.trafficmaneuver.Maneuver.TypeAndConfidence.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='sensoris.protobuf.categories.trafficmaneuver.Maneuver.TypeAndConfidence.confidence', index=1,
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
    _MANEUVER_TYPEANDCONFIDENCE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=763,
)

_MANEUVER = _descriptor.Descriptor(
  name='Maneuver',
  full_name='sensoris.protobuf.categories.trafficmaneuver.Maneuver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.trafficmaneuver.Maneuver.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_and_confidence', full_name='sensoris.protobuf.categories.trafficmaneuver.Maneuver.type_and_confidence', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MANEUVER_TYPEANDCONFIDENCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=763,
)


_CHARGING = _descriptor.Descriptor(
  name='Charging',
  full_name='sensoris.protobuf.categories.trafficmaneuver.Charging',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.trafficmaneuver.Charging.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='sensoris.protobuf.categories.trafficmaneuver.Charging.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voltage_and_accuracy', full_name='sensoris.protobuf.categories.trafficmaneuver.Charging.voltage_and_accuracy', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_and_accuracy', full_name='sensoris.protobuf.categories.trafficmaneuver.Charging.current_and_accuracy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHARGING_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=766,
  serialized_end=1202,
)


_REFUELING = _descriptor.Descriptor(
  name='Refueling',
  full_name='sensoris.protobuf.categories.trafficmaneuver.Refueling',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.trafficmaneuver.Refueling.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='sensoris.protobuf.categories.trafficmaneuver.Refueling.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity_to_full_and_accuracy', full_name='sensoris.protobuf.categories.trafficmaneuver.Refueling.quantity_to_full_and_accuracy', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REFUELING_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1205,
  serialized_end=1595,
)


_TRAFFICMANEUVERCATEGORY = _descriptor.Descriptor(
  name='TrafficManeuverCategory',
  full_name='sensoris.protobuf.categories.trafficmaneuver.TrafficManeuverCategory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.trafficmaneuver.TrafficManeuverCategory.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maneuver', full_name='sensoris.protobuf.categories.trafficmaneuver.TrafficManeuverCategory.maneuver', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charging', full_name='sensoris.protobuf.categories.trafficmaneuver.TrafficManeuverCategory.charging', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refueling', full_name='sensoris.protobuf.categories.trafficmaneuver.TrafficManeuverCategory.refueling', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=1598,
  serialized_end=1913,
)

_MANEUVER_TYPEANDCONFIDENCE.fields_by_name['type'].enum_type = _MANEUVER_TYPEANDCONFIDENCE_TYPE
_MANEUVER_TYPEANDCONFIDENCE.fields_by_name['confidence'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CONFIDENCE
_MANEUVER_TYPEANDCONFIDENCE.containing_type = _MANEUVER
_MANEUVER_TYPEANDCONFIDENCE_TYPE.containing_type = _MANEUVER_TYPEANDCONFIDENCE
_MANEUVER.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_MANEUVER.fields_by_name['type_and_confidence'].message_type = _MANEUVER_TYPEANDCONFIDENCE
_CHARGING.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_CHARGING.fields_by_name['type'].enum_type = _CHARGING_TYPE
_CHARGING.fields_by_name['voltage_and_accuracy'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._INT64VALUEANDACCURACY
_CHARGING.fields_by_name['current_and_accuracy'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._INT64VALUEANDACCURACY
_CHARGING_TYPE.containing_type = _CHARGING
_REFUELING.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_REFUELING.fields_by_name['type'].enum_type = _REFUELING_TYPE
_REFUELING.fields_by_name['quantity_to_full_and_accuracy'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._INT64VALUEANDACCURACY
_REFUELING_TYPE.containing_type = _REFUELING
_TRAFFICMANEUVERCATEGORY.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CATEGORYENVELOPE
_TRAFFICMANEUVERCATEGORY.fields_by_name['maneuver'].message_type = _MANEUVER
_TRAFFICMANEUVERCATEGORY.fields_by_name['charging'].message_type = _CHARGING
_TRAFFICMANEUVERCATEGORY.fields_by_name['refueling'].message_type = _REFUELING
DESCRIPTOR.message_types_by_name['Maneuver'] = _MANEUVER
DESCRIPTOR.message_types_by_name['Charging'] = _CHARGING
DESCRIPTOR.message_types_by_name['Refueling'] = _REFUELING
DESCRIPTOR.message_types_by_name['TrafficManeuverCategory'] = _TRAFFICMANEUVERCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Maneuver = _reflection.GeneratedProtocolMessageType('Maneuver', (_message.Message,), {

  'TypeAndConfidence' : _reflection.GeneratedProtocolMessageType('TypeAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _MANEUVER_TYPEANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.traffic_maneuver_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficmaneuver.Maneuver.TypeAndConfidence)
    })
  ,
  'DESCRIPTOR' : _MANEUVER,
  '__module__' : 'sensoris.protobuf.categories.traffic_maneuver_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficmaneuver.Maneuver)
  })
_sym_db.RegisterMessage(Maneuver)
_sym_db.RegisterMessage(Maneuver.TypeAndConfidence)

Charging = _reflection.GeneratedProtocolMessageType('Charging', (_message.Message,), {
  'DESCRIPTOR' : _CHARGING,
  '__module__' : 'sensoris.protobuf.categories.traffic_maneuver_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficmaneuver.Charging)
  })
_sym_db.RegisterMessage(Charging)

Refueling = _reflection.GeneratedProtocolMessageType('Refueling', (_message.Message,), {
  'DESCRIPTOR' : _REFUELING,
  '__module__' : 'sensoris.protobuf.categories.traffic_maneuver_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficmaneuver.Refueling)
  })
_sym_db.RegisterMessage(Refueling)

TrafficManeuverCategory = _reflection.GeneratedProtocolMessageType('TrafficManeuverCategory', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICMANEUVERCATEGORY,
  '__module__' : 'sensoris.protobuf.categories.traffic_maneuver_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficmaneuver.TrafficManeuverCategory)
  })
_sym_db.RegisterMessage(TrafficManeuverCategory)


DESCRIPTOR._options = None
_CHARGING.fields_by_name['voltage_and_accuracy']._options = None
_CHARGING.fields_by_name['current_and_accuracy']._options = None
_REFUELING.fields_by_name['quantity_to_full_and_accuracy']._options = None
# @@protoc_insertion_point(module_scope)
