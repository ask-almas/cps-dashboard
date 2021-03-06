# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensoris/protobuf/categories/weather.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sensoris.protobuf.types import base_pb2 as sensoris_dot_protobuf_dot_types_dot_base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensoris/protobuf/categories/weather.proto',
  package='sensoris.protobuf.categories.weather',
  syntax='proto3',
  serialized_options=b'\n\037org.sensoris.categories.weatherB\027SensorisWeatherCategoryP\001\370\001\001',
  serialized_pb=b'\n*sensoris/protobuf/categories/weather.proto\x12$sensoris.protobuf.categories.weather\x1a\"sensoris/protobuf/types/base.proto\"\xde\x05\n\rPrecipitation\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12L\n\x10\x64\x65tection_status\x18\x02 \x01(\x0b\x32\x32.sensoris.protobuf.types.base.EventDetectionStatus\x12\x62\n\x13type_and_confidence\x18\x03 \x01(\x0b\x32\x45.sensoris.protobuf.categories.weather.Precipitation.TypeAndConfidence\x12\x64\n\x1frelative_intensity_and_accuracy\x18\x04 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x00H\x00\x12\x64\n\x1f\x61\x62solute_intensity_and_accuracy\x18\x05 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x01H\x00\x1a\x82\x02\n\x11TypeAndConfidence\x12X\n\x04type\x18\x01 \x01(\x0e\x32J.sensoris.protobuf.categories.weather.Precipitation.TypeAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"U\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x08\n\x04RAIN\x10\x02\x12\x13\n\x0fMIXED_RAIN_SNOW\x10\x03\x12\x08\n\x04SNOW\x10\x04\x12\x08\n\x04HAIL\x10\x05\x42\x0b\n\tintensity\"\x9f\x01\n\x0fWeatherCategory\x12@\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32..sensoris.protobuf.types.base.CategoryEnvelope\x12J\n\rprecipitation\x18\x02 \x03(\x0b\x32\x33.sensoris.protobuf.categories.weather.PrecipitationB?\n\x1forg.sensoris.categories.weatherB\x17SensorisWeatherCategoryP\x01\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[sensoris_dot_protobuf_dot_types_dot_base__pb2.DESCRIPTOR,])



_PRECIPITATION_TYPEANDCONFIDENCE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensoris.protobuf.categories.weather.Precipitation.TypeAndConfidence.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAIN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIXED_RAIN_SNOW', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SNOW', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HAIL', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=757,
  serialized_end=842,
)
_sym_db.RegisterEnumDescriptor(_PRECIPITATION_TYPEANDCONFIDENCE_TYPE)


_PRECIPITATION_TYPEANDCONFIDENCE = _descriptor.Descriptor(
  name='TypeAndConfidence',
  full_name='sensoris.protobuf.categories.weather.Precipitation.TypeAndConfidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sensoris.protobuf.categories.weather.Precipitation.TypeAndConfidence.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='sensoris.protobuf.categories.weather.Precipitation.TypeAndConfidence.confidence', index=1,
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
    _PRECIPITATION_TYPEANDCONFIDENCE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=584,
  serialized_end=842,
)

_PRECIPITATION = _descriptor.Descriptor(
  name='Precipitation',
  full_name='sensoris.protobuf.categories.weather.Precipitation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.weather.Precipitation.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detection_status', full_name='sensoris.protobuf.categories.weather.Precipitation.detection_status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_and_confidence', full_name='sensoris.protobuf.categories.weather.Precipitation.type_and_confidence', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_intensity_and_accuracy', full_name='sensoris.protobuf.categories.weather.Precipitation.relative_intensity_and_accuracy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='absolute_intensity_and_accuracy', full_name='sensoris.protobuf.categories.weather.Precipitation.absolute_intensity_and_accuracy', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\210\265\030\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PRECIPITATION_TYPEANDCONFIDENCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='intensity', full_name='sensoris.protobuf.categories.weather.Precipitation.intensity',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=121,
  serialized_end=855,
)


_WEATHERCATEGORY = _descriptor.Descriptor(
  name='WeatherCategory',
  full_name='sensoris.protobuf.categories.weather.WeatherCategory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.weather.WeatherCategory.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='precipitation', full_name='sensoris.protobuf.categories.weather.WeatherCategory.precipitation', index=1,
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
  serialized_start=858,
  serialized_end=1017,
)

_PRECIPITATION_TYPEANDCONFIDENCE.fields_by_name['type'].enum_type = _PRECIPITATION_TYPEANDCONFIDENCE_TYPE
_PRECIPITATION_TYPEANDCONFIDENCE.fields_by_name['confidence'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CONFIDENCE
_PRECIPITATION_TYPEANDCONFIDENCE.containing_type = _PRECIPITATION
_PRECIPITATION_TYPEANDCONFIDENCE_TYPE.containing_type = _PRECIPITATION_TYPEANDCONFIDENCE
_PRECIPITATION.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_PRECIPITATION.fields_by_name['detection_status'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTDETECTIONSTATUS
_PRECIPITATION.fields_by_name['type_and_confidence'].message_type = _PRECIPITATION_TYPEANDCONFIDENCE
_PRECIPITATION.fields_by_name['relative_intensity_and_accuracy'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._INT64VALUEANDACCURACY
_PRECIPITATION.fields_by_name['absolute_intensity_and_accuracy'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._INT64VALUEANDACCURACY
_PRECIPITATION.oneofs_by_name['intensity'].fields.append(
  _PRECIPITATION.fields_by_name['relative_intensity_and_accuracy'])
_PRECIPITATION.fields_by_name['relative_intensity_and_accuracy'].containing_oneof = _PRECIPITATION.oneofs_by_name['intensity']
_PRECIPITATION.oneofs_by_name['intensity'].fields.append(
  _PRECIPITATION.fields_by_name['absolute_intensity_and_accuracy'])
_PRECIPITATION.fields_by_name['absolute_intensity_and_accuracy'].containing_oneof = _PRECIPITATION.oneofs_by_name['intensity']
_WEATHERCATEGORY.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CATEGORYENVELOPE
_WEATHERCATEGORY.fields_by_name['precipitation'].message_type = _PRECIPITATION
DESCRIPTOR.message_types_by_name['Precipitation'] = _PRECIPITATION
DESCRIPTOR.message_types_by_name['WeatherCategory'] = _WEATHERCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Precipitation = _reflection.GeneratedProtocolMessageType('Precipitation', (_message.Message,), {

  'TypeAndConfidence' : _reflection.GeneratedProtocolMessageType('TypeAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _PRECIPITATION_TYPEANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.weather_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.weather.Precipitation.TypeAndConfidence)
    })
  ,
  'DESCRIPTOR' : _PRECIPITATION,
  '__module__' : 'sensoris.protobuf.categories.weather_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.weather.Precipitation)
  })
_sym_db.RegisterMessage(Precipitation)
_sym_db.RegisterMessage(Precipitation.TypeAndConfidence)

WeatherCategory = _reflection.GeneratedProtocolMessageType('WeatherCategory', (_message.Message,), {
  'DESCRIPTOR' : _WEATHERCATEGORY,
  '__module__' : 'sensoris.protobuf.categories.weather_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.weather.WeatherCategory)
  })
_sym_db.RegisterMessage(WeatherCategory)


DESCRIPTOR._options = None
_PRECIPITATION.fields_by_name['relative_intensity_and_accuracy']._options = None
_PRECIPITATION.fields_by_name['absolute_intensity_and_accuracy']._options = None
# @@protoc_insertion_point(module_scope)
