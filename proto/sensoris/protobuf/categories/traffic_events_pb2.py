# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensoris/protobuf/categories/traffic_events.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from sensoris.protobuf.types import base_pb2 as sensoris_dot_protobuf_dot_types_dot_base__pb2
from sensoris.protobuf.types import spatial_pb2 as sensoris_dot_protobuf_dot_types_dot_spatial__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensoris/protobuf/categories/traffic_events.proto',
  package='sensoris.protobuf.categories.trafficevents',
  syntax='proto3',
  serialized_options=b'\n%org.sensoris.categories.trafficeventsB\035SensorisTrafficEventsCategoryP\001\370\001\001',
  serialized_pb=b'\n1sensoris/protobuf/categories/traffic_events.proto\x12*sensoris.protobuf.categories.trafficevents\x1a\x1egoogle/protobuf/wrappers.proto\x1a\"sensoris/protobuf/types/base.proto\x1a%sensoris/protobuf/types/spatial.proto\"\xda\x05\n\x06Hazard\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12L\n\x10\x64\x65tection_status\x18\x02 \x01(\x0b\x32\x32.sensoris.protobuf.types.base.EventDetectionStatus\x12\x61\n\x13type_and_confidence\x18\x03 \x01(\x0b\x32\x44.sensoris.protobuf.categories.trafficevents.Hazard.TypeAndConfidence\x12O\n\tdirection\x18\x04 \x01(\x0e\x32<.sensoris.protobuf.categories.trafficevents.Hazard.Direction\x1a\xb5\x02\n\x11TypeAndConfidence\x12W\n\x04type\x18\x01 \x01(\x0e\x32I.sensoris.protobuf.categories.trafficevents.Hazard.TypeAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"\x88\x01\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0f\n\x0bOBSTRUCTION\x10\x01\x12\x0c\n\x08\x41\x43\x43IDENT\x10\x02\x12\x17\n\x13\x42ROKEN_DOWN_VEHICLE\x10\x03\x12\x10\n\x0cSLOW_VEHICLE\x10\x04\x12\x15\n\x11WRONG_WAY_VEHICLE\x10\x05\x12\r\n\tROADWORKS\x10\x06\"W\n\tDirection\x12\x15\n\x11UNKNOWN_DIRECTION\x10\x00\x12\x11\n\rEGO_DIRECTION\x10\x01\x12\x16\n\x12OPPOSITE_DIRECTION\x10\x02\x12\x08\n\x04\x42OTH\x10\x03\"\xed\x01\n\x11\x44\x61ngerousSlowDown\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12\x61\n\x1cspeed_reduction_and_accuracy\x18\x02 \x01(\x0b\x32\x35.sensoris.protobuf.types.spatial.XyzVectorAndAccuracyB\x04\x88\xb5\x18\x01\x12\x36\n\x0btime_period\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x04\x88\xb5\x18\x00\"\x9e\x04\n\x10TrafficCondition\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12L\n\x10\x64\x65tection_status\x18\x02 \x01(\x0b\x32\x32.sensoris.protobuf.types.base.EventDetectionStatus\x12k\n\x13type_and_confidence\x18\x03 \x01(\x0b\x32N.sensoris.protobuf.categories.trafficevents.TrafficCondition.TypeAndConfidence\x1a\x8f\x02\n\x11TypeAndConfidence\x12\x61\n\x04type\x18\x01 \x01(\x0e\x32S.sensoris.protobuf.categories.trafficevents.TrafficCondition.TypeAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"Y\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\r\n\tFREE_FLOW\x10\x01\x12\t\n\x05HEAVY\x10\x02\x12\x08\n\x04SLOW\x10\x03\x12\x0b\n\x07QUEUING\x10\x04\x12\x0e\n\nSTATIONARY\x10\x05\"\xb3\x04\n\tRoadWorks\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12L\n\x10\x64\x65tection_status\x18\x02 \x01(\x0b\x32\x32.sensoris.protobuf.types.base.EventDetectionStatus\x12\x64\n\x13type_and_confidence\x18\x03 \x01(\x0b\x32G.sensoris.protobuf.categories.trafficevents.RoadWorks.TypeAndConfidence\x12U\n\x1blanes_closed_and_confidence\x18\x05 \x01(\x0b\x32\x30.sensoris.protobuf.types.base.CountAndConfidence\x1a\xdb\x01\n\x11TypeAndConfidence\x12Z\n\x04type\x18\x01 \x01(\x0e\x32L.sensoris.protobuf.categories.trafficevents.RoadWorks.TypeAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\",\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\t\n\x05START\x10\x01\x12\x07\n\x03\x45ND\x10\x02\"\x91\x05\n\x14RoadWeatherCondition\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12L\n\x10\x64\x65tection_status\x18\x02 \x01(\x0b\x32\x32.sensoris.protobuf.types.base.EventDetectionStatus\x12o\n\x13type_and_confidence\x18\x03 \x01(\x0b\x32R.sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.TypeAndConfidence\x12U\n\x12\x64\x65pth_and_accuracy\x18\x04 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x00\x1a\xa3\x02\n\x11TypeAndConfidence\x12\x65\n\x04type\x18\x01 \x01(\x0e\x32W.sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.TypeAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"i\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x08\n\x04SNOW\x10\x01\x12\x07\n\x03ICE\x10\x02\x12\x11\n\rFREEZING_RAIN\x10\x03\x12\t\n\x05\x46ROST\x10\x04\x12\x10\n\x0cHYDROPLANING\x10\x05\x12\x0c\n\x08\x46LOODING\x10\x06\"\xfe\x03\n\x15TrafficEventsCategory\x12@\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32..sensoris.protobuf.types.base.CategoryEnvelope\x12\x42\n\x06hazard\x18\x02 \x03(\x0b\x32\x32.sensoris.protobuf.categories.trafficevents.Hazard\x12Z\n\x13\x64\x61ngerous_slow_down\x18\x03 \x03(\x0b\x32=.sensoris.protobuf.categories.trafficevents.DangerousSlowDown\x12W\n\x11traffic_condition\x18\x04 \x03(\x0b\x32<.sensoris.protobuf.categories.trafficevents.TrafficCondition\x12H\n\troadworks\x18\x05 \x03(\x0b\x32\x35.sensoris.protobuf.categories.trafficevents.RoadWorks\x12`\n\x16road_weather_condition\x18\x06 \x03(\x0b\x32@.sensoris.protobuf.categories.trafficevents.RoadWeatherConditionBK\n%org.sensoris.categories.trafficeventsB\x1dSensorisTrafficEventsCategoryP\x01\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,sensoris_dot_protobuf_dot_types_dot_base__pb2.DESCRIPTOR,sensoris_dot_protobuf_dot_types_dot_spatial__pb2.DESCRIPTOR,])



_HAZARD_TYPEANDCONFIDENCE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensoris.protobuf.categories.trafficevents.Hazard.TypeAndConfidence.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OBSTRUCTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCIDENT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROKEN_DOWN_VEHICLE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLOW_VEHICLE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRONG_WAY_VEHICLE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROADWORKS', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=710,
  serialized_end=846,
)
_sym_db.RegisterEnumDescriptor(_HAZARD_TYPEANDCONFIDENCE_TYPE)

_HAZARD_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='sensoris.protobuf.categories.trafficevents.Hazard.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_DIRECTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGO_DIRECTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPPOSITE_DIRECTION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOTH', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=848,
  serialized_end=935,
)
_sym_db.RegisterEnumDescriptor(_HAZARD_DIRECTION)

_TRAFFICCONDITION_TYPEANDCONFIDENCE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensoris.protobuf.categories.trafficevents.TrafficCondition.TypeAndConfidence.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FREE_FLOW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEAVY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLOW', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEUING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATIONARY', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1631,
  serialized_end=1720,
)
_sym_db.RegisterEnumDescriptor(_TRAFFICCONDITION_TYPEANDCONFIDENCE_TYPE)

_ROADWORKS_TYPEANDCONFIDENCE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensoris.protobuf.categories.trafficevents.RoadWorks.TypeAndConfidence.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2242,
  serialized_end=2286,
)
_sym_db.RegisterEnumDescriptor(_ROADWORKS_TYPEANDCONFIDENCE_TYPE)

_ROADWEATHERCONDITION_TYPEANDCONFIDENCE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.TypeAndConfidence.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SNOW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FREEZING_RAIN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FROST', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYDROPLANING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOODING', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2841,
  serialized_end=2946,
)
_sym_db.RegisterEnumDescriptor(_ROADWEATHERCONDITION_TYPEANDCONFIDENCE_TYPE)


_HAZARD_TYPEANDCONFIDENCE = _descriptor.Descriptor(
  name='TypeAndConfidence',
  full_name='sensoris.protobuf.categories.trafficevents.Hazard.TypeAndConfidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sensoris.protobuf.categories.trafficevents.Hazard.TypeAndConfidence.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='sensoris.protobuf.categories.trafficevents.Hazard.TypeAndConfidence.confidence', index=1,
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
    _HAZARD_TYPEANDCONFIDENCE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=537,
  serialized_end=846,
)

_HAZARD = _descriptor.Descriptor(
  name='Hazard',
  full_name='sensoris.protobuf.categories.trafficevents.Hazard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.trafficevents.Hazard.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detection_status', full_name='sensoris.protobuf.categories.trafficevents.Hazard.detection_status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_and_confidence', full_name='sensoris.protobuf.categories.trafficevents.Hazard.type_and_confidence', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='sensoris.protobuf.categories.trafficevents.Hazard.direction', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HAZARD_TYPEANDCONFIDENCE, ],
  enum_types=[
    _HAZARD_DIRECTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=935,
)


_DANGEROUSSLOWDOWN = _descriptor.Descriptor(
  name='DangerousSlowDown',
  full_name='sensoris.protobuf.categories.trafficevents.DangerousSlowDown',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.trafficevents.DangerousSlowDown.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_reduction_and_accuracy', full_name='sensoris.protobuf.categories.trafficevents.DangerousSlowDown.speed_reduction_and_accuracy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_period', full_name='sensoris.protobuf.categories.trafficevents.DangerousSlowDown.time_period', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\000', file=DESCRIPTOR),
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
  serialized_start=938,
  serialized_end=1175,
)


_TRAFFICCONDITION_TYPEANDCONFIDENCE = _descriptor.Descriptor(
  name='TypeAndConfidence',
  full_name='sensoris.protobuf.categories.trafficevents.TrafficCondition.TypeAndConfidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sensoris.protobuf.categories.trafficevents.TrafficCondition.TypeAndConfidence.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='sensoris.protobuf.categories.trafficevents.TrafficCondition.TypeAndConfidence.confidence', index=1,
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
    _TRAFFICCONDITION_TYPEANDCONFIDENCE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1449,
  serialized_end=1720,
)

_TRAFFICCONDITION = _descriptor.Descriptor(
  name='TrafficCondition',
  full_name='sensoris.protobuf.categories.trafficevents.TrafficCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.trafficevents.TrafficCondition.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detection_status', full_name='sensoris.protobuf.categories.trafficevents.TrafficCondition.detection_status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_and_confidence', full_name='sensoris.protobuf.categories.trafficevents.TrafficCondition.type_and_confidence', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRAFFICCONDITION_TYPEANDCONFIDENCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1178,
  serialized_end=1720,
)


_ROADWORKS_TYPEANDCONFIDENCE = _descriptor.Descriptor(
  name='TypeAndConfidence',
  full_name='sensoris.protobuf.categories.trafficevents.RoadWorks.TypeAndConfidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sensoris.protobuf.categories.trafficevents.RoadWorks.TypeAndConfidence.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='sensoris.protobuf.categories.trafficevents.RoadWorks.TypeAndConfidence.confidence', index=1,
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
    _ROADWORKS_TYPEANDCONFIDENCE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2067,
  serialized_end=2286,
)

_ROADWORKS = _descriptor.Descriptor(
  name='RoadWorks',
  full_name='sensoris.protobuf.categories.trafficevents.RoadWorks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.trafficevents.RoadWorks.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detection_status', full_name='sensoris.protobuf.categories.trafficevents.RoadWorks.detection_status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_and_confidence', full_name='sensoris.protobuf.categories.trafficevents.RoadWorks.type_and_confidence', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lanes_closed_and_confidence', full_name='sensoris.protobuf.categories.trafficevents.RoadWorks.lanes_closed_and_confidence', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ROADWORKS_TYPEANDCONFIDENCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1723,
  serialized_end=2286,
)


_ROADWEATHERCONDITION_TYPEANDCONFIDENCE = _descriptor.Descriptor(
  name='TypeAndConfidence',
  full_name='sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.TypeAndConfidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.TypeAndConfidence.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.TypeAndConfidence.confidence', index=1,
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
    _ROADWEATHERCONDITION_TYPEANDCONFIDENCE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2655,
  serialized_end=2946,
)

_ROADWEATHERCONDITION = _descriptor.Descriptor(
  name='RoadWeatherCondition',
  full_name='sensoris.protobuf.categories.trafficevents.RoadWeatherCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detection_status', full_name='sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.detection_status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_and_confidence', full_name='sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.type_and_confidence', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth_and_accuracy', full_name='sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.depth_and_accuracy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\000', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ROADWEATHERCONDITION_TYPEANDCONFIDENCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2289,
  serialized_end=2946,
)


_TRAFFICEVENTSCATEGORY = _descriptor.Descriptor(
  name='TrafficEventsCategory',
  full_name='sensoris.protobuf.categories.trafficevents.TrafficEventsCategory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.trafficevents.TrafficEventsCategory.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hazard', full_name='sensoris.protobuf.categories.trafficevents.TrafficEventsCategory.hazard', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dangerous_slow_down', full_name='sensoris.protobuf.categories.trafficevents.TrafficEventsCategory.dangerous_slow_down', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traffic_condition', full_name='sensoris.protobuf.categories.trafficevents.TrafficEventsCategory.traffic_condition', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roadworks', full_name='sensoris.protobuf.categories.trafficevents.TrafficEventsCategory.roadworks', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road_weather_condition', full_name='sensoris.protobuf.categories.trafficevents.TrafficEventsCategory.road_weather_condition', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=2949,
  serialized_end=3459,
)

_HAZARD_TYPEANDCONFIDENCE.fields_by_name['type'].enum_type = _HAZARD_TYPEANDCONFIDENCE_TYPE
_HAZARD_TYPEANDCONFIDENCE.fields_by_name['confidence'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CONFIDENCE
_HAZARD_TYPEANDCONFIDENCE.containing_type = _HAZARD
_HAZARD_TYPEANDCONFIDENCE_TYPE.containing_type = _HAZARD_TYPEANDCONFIDENCE
_HAZARD.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_HAZARD.fields_by_name['detection_status'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTDETECTIONSTATUS
_HAZARD.fields_by_name['type_and_confidence'].message_type = _HAZARD_TYPEANDCONFIDENCE
_HAZARD.fields_by_name['direction'].enum_type = _HAZARD_DIRECTION
_HAZARD_DIRECTION.containing_type = _HAZARD
_DANGEROUSSLOWDOWN.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_DANGEROUSSLOWDOWN.fields_by_name['speed_reduction_and_accuracy'].message_type = sensoris_dot_protobuf_dot_types_dot_spatial__pb2._XYZVECTORANDACCURACY
_DANGEROUSSLOWDOWN.fields_by_name['time_period'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TRAFFICCONDITION_TYPEANDCONFIDENCE.fields_by_name['type'].enum_type = _TRAFFICCONDITION_TYPEANDCONFIDENCE_TYPE
_TRAFFICCONDITION_TYPEANDCONFIDENCE.fields_by_name['confidence'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CONFIDENCE
_TRAFFICCONDITION_TYPEANDCONFIDENCE.containing_type = _TRAFFICCONDITION
_TRAFFICCONDITION_TYPEANDCONFIDENCE_TYPE.containing_type = _TRAFFICCONDITION_TYPEANDCONFIDENCE
_TRAFFICCONDITION.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_TRAFFICCONDITION.fields_by_name['detection_status'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTDETECTIONSTATUS
_TRAFFICCONDITION.fields_by_name['type_and_confidence'].message_type = _TRAFFICCONDITION_TYPEANDCONFIDENCE
_ROADWORKS_TYPEANDCONFIDENCE.fields_by_name['type'].enum_type = _ROADWORKS_TYPEANDCONFIDENCE_TYPE
_ROADWORKS_TYPEANDCONFIDENCE.fields_by_name['confidence'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CONFIDENCE
_ROADWORKS_TYPEANDCONFIDENCE.containing_type = _ROADWORKS
_ROADWORKS_TYPEANDCONFIDENCE_TYPE.containing_type = _ROADWORKS_TYPEANDCONFIDENCE
_ROADWORKS.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_ROADWORKS.fields_by_name['detection_status'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTDETECTIONSTATUS
_ROADWORKS.fields_by_name['type_and_confidence'].message_type = _ROADWORKS_TYPEANDCONFIDENCE
_ROADWORKS.fields_by_name['lanes_closed_and_confidence'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._COUNTANDCONFIDENCE
_ROADWEATHERCONDITION_TYPEANDCONFIDENCE.fields_by_name['type'].enum_type = _ROADWEATHERCONDITION_TYPEANDCONFIDENCE_TYPE
_ROADWEATHERCONDITION_TYPEANDCONFIDENCE.fields_by_name['confidence'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CONFIDENCE
_ROADWEATHERCONDITION_TYPEANDCONFIDENCE.containing_type = _ROADWEATHERCONDITION
_ROADWEATHERCONDITION_TYPEANDCONFIDENCE_TYPE.containing_type = _ROADWEATHERCONDITION_TYPEANDCONFIDENCE
_ROADWEATHERCONDITION.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_ROADWEATHERCONDITION.fields_by_name['detection_status'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTDETECTIONSTATUS
_ROADWEATHERCONDITION.fields_by_name['type_and_confidence'].message_type = _ROADWEATHERCONDITION_TYPEANDCONFIDENCE
_ROADWEATHERCONDITION.fields_by_name['depth_and_accuracy'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._INT64VALUEANDACCURACY
_TRAFFICEVENTSCATEGORY.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CATEGORYENVELOPE
_TRAFFICEVENTSCATEGORY.fields_by_name['hazard'].message_type = _HAZARD
_TRAFFICEVENTSCATEGORY.fields_by_name['dangerous_slow_down'].message_type = _DANGEROUSSLOWDOWN
_TRAFFICEVENTSCATEGORY.fields_by_name['traffic_condition'].message_type = _TRAFFICCONDITION
_TRAFFICEVENTSCATEGORY.fields_by_name['roadworks'].message_type = _ROADWORKS
_TRAFFICEVENTSCATEGORY.fields_by_name['road_weather_condition'].message_type = _ROADWEATHERCONDITION
DESCRIPTOR.message_types_by_name['Hazard'] = _HAZARD
DESCRIPTOR.message_types_by_name['DangerousSlowDown'] = _DANGEROUSSLOWDOWN
DESCRIPTOR.message_types_by_name['TrafficCondition'] = _TRAFFICCONDITION
DESCRIPTOR.message_types_by_name['RoadWorks'] = _ROADWORKS
DESCRIPTOR.message_types_by_name['RoadWeatherCondition'] = _ROADWEATHERCONDITION
DESCRIPTOR.message_types_by_name['TrafficEventsCategory'] = _TRAFFICEVENTSCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Hazard = _reflection.GeneratedProtocolMessageType('Hazard', (_message.Message,), {

  'TypeAndConfidence' : _reflection.GeneratedProtocolMessageType('TypeAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _HAZARD_TYPEANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.traffic_events_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficevents.Hazard.TypeAndConfidence)
    })
  ,
  'DESCRIPTOR' : _HAZARD,
  '__module__' : 'sensoris.protobuf.categories.traffic_events_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficevents.Hazard)
  })
_sym_db.RegisterMessage(Hazard)
_sym_db.RegisterMessage(Hazard.TypeAndConfidence)

DangerousSlowDown = _reflection.GeneratedProtocolMessageType('DangerousSlowDown', (_message.Message,), {
  'DESCRIPTOR' : _DANGEROUSSLOWDOWN,
  '__module__' : 'sensoris.protobuf.categories.traffic_events_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficevents.DangerousSlowDown)
  })
_sym_db.RegisterMessage(DangerousSlowDown)

TrafficCondition = _reflection.GeneratedProtocolMessageType('TrafficCondition', (_message.Message,), {

  'TypeAndConfidence' : _reflection.GeneratedProtocolMessageType('TypeAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _TRAFFICCONDITION_TYPEANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.traffic_events_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficevents.TrafficCondition.TypeAndConfidence)
    })
  ,
  'DESCRIPTOR' : _TRAFFICCONDITION,
  '__module__' : 'sensoris.protobuf.categories.traffic_events_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficevents.TrafficCondition)
  })
_sym_db.RegisterMessage(TrafficCondition)
_sym_db.RegisterMessage(TrafficCondition.TypeAndConfidence)

RoadWorks = _reflection.GeneratedProtocolMessageType('RoadWorks', (_message.Message,), {

  'TypeAndConfidence' : _reflection.GeneratedProtocolMessageType('TypeAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _ROADWORKS_TYPEANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.traffic_events_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficevents.RoadWorks.TypeAndConfidence)
    })
  ,
  'DESCRIPTOR' : _ROADWORKS,
  '__module__' : 'sensoris.protobuf.categories.traffic_events_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficevents.RoadWorks)
  })
_sym_db.RegisterMessage(RoadWorks)
_sym_db.RegisterMessage(RoadWorks.TypeAndConfidence)

RoadWeatherCondition = _reflection.GeneratedProtocolMessageType('RoadWeatherCondition', (_message.Message,), {

  'TypeAndConfidence' : _reflection.GeneratedProtocolMessageType('TypeAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _ROADWEATHERCONDITION_TYPEANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.traffic_events_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficevents.RoadWeatherCondition.TypeAndConfidence)
    })
  ,
  'DESCRIPTOR' : _ROADWEATHERCONDITION,
  '__module__' : 'sensoris.protobuf.categories.traffic_events_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficevents.RoadWeatherCondition)
  })
_sym_db.RegisterMessage(RoadWeatherCondition)
_sym_db.RegisterMessage(RoadWeatherCondition.TypeAndConfidence)

TrafficEventsCategory = _reflection.GeneratedProtocolMessageType('TrafficEventsCategory', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICEVENTSCATEGORY,
  '__module__' : 'sensoris.protobuf.categories.traffic_events_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficevents.TrafficEventsCategory)
  })
_sym_db.RegisterMessage(TrafficEventsCategory)


DESCRIPTOR._options = None
_DANGEROUSSLOWDOWN.fields_by_name['speed_reduction_and_accuracy']._options = None
_DANGEROUSSLOWDOWN.fields_by_name['time_period']._options = None
_ROADWEATHERCONDITION.fields_by_name['depth_and_accuracy']._options = None
# @@protoc_insertion_point(module_scope)
