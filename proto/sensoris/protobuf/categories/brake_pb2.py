# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensoris/protobuf/categories/brake.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sensoris.protobuf.types import base_pb2 as sensoris_dot_protobuf_dot_types_dot_base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensoris/protobuf/categories/brake.proto',
  package='sensoris.protobuf.categories.brake',
  syntax='proto3',
  serialized_options=b'\n\035org.sensoris.categories.brakeB\025SensorisBrakeCategoryP\001\370\001\001',
  serialized_pb=b'\n(sensoris/protobuf/categories/brake.proto\x12\"sensoris.protobuf.categories.brake\x1a\"sensoris/protobuf/types/base.proto\"\x93\x03\n\x12\x42rakeSystemsStatus\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12>\n\nabs_status\x18\x02 \x01(\x0e\x32*.sensoris.protobuf.types.base.SystemStatus\x12>\n\nesc_status\x18\x03 \x01(\x0e\x32*.sensoris.protobuf.types.base.SystemStatus\x12>\n\ntcs_status\x18\x04 \x01(\x0e\x32*.sensoris.protobuf.types.base.SystemStatus\x12>\n\nebd_status\x18\x05 \x01(\x0e\x32*.sensoris.protobuf.types.base.SystemStatus\x12>\n\neba_status\x18\x06 \x01(\x0e\x32*.sensoris.protobuf.types.base.SystemStatus\"\xa7\x01\n\rBrakeCategory\x12@\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32..sensoris.protobuf.types.base.CategoryEnvelope\x12T\n\x14\x62rake_systems_status\x18\x02 \x03(\x0b\x32\x36.sensoris.protobuf.categories.brake.BrakeSystemsStatusB;\n\x1dorg.sensoris.categories.brakeB\x15SensorisBrakeCategoryP\x01\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[sensoris_dot_protobuf_dot_types_dot_base__pb2.DESCRIPTOR,])




_BRAKESYSTEMSSTATUS = _descriptor.Descriptor(
  name='BrakeSystemsStatus',
  full_name='sensoris.protobuf.categories.brake.BrakeSystemsStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.brake.BrakeSystemsStatus.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abs_status', full_name='sensoris.protobuf.categories.brake.BrakeSystemsStatus.abs_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='esc_status', full_name='sensoris.protobuf.categories.brake.BrakeSystemsStatus.esc_status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcs_status', full_name='sensoris.protobuf.categories.brake.BrakeSystemsStatus.tcs_status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ebd_status', full_name='sensoris.protobuf.categories.brake.BrakeSystemsStatus.ebd_status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eba_status', full_name='sensoris.protobuf.categories.brake.BrakeSystemsStatus.eba_status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=117,
  serialized_end=520,
)


_BRAKECATEGORY = _descriptor.Descriptor(
  name='BrakeCategory',
  full_name='sensoris.protobuf.categories.brake.BrakeCategory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envelope', full_name='sensoris.protobuf.categories.brake.BrakeCategory.envelope', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brake_systems_status', full_name='sensoris.protobuf.categories.brake.BrakeCategory.brake_systems_status', index=1,
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
  serialized_start=523,
  serialized_end=690,
)

_BRAKESYSTEMSSTATUS.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._EVENTENVELOPE
_BRAKESYSTEMSSTATUS.fields_by_name['abs_status'].enum_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._SYSTEMSTATUS
_BRAKESYSTEMSSTATUS.fields_by_name['esc_status'].enum_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._SYSTEMSTATUS
_BRAKESYSTEMSSTATUS.fields_by_name['tcs_status'].enum_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._SYSTEMSTATUS
_BRAKESYSTEMSSTATUS.fields_by_name['ebd_status'].enum_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._SYSTEMSTATUS
_BRAKESYSTEMSSTATUS.fields_by_name['eba_status'].enum_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._SYSTEMSTATUS
_BRAKECATEGORY.fields_by_name['envelope'].message_type = sensoris_dot_protobuf_dot_types_dot_base__pb2._CATEGORYENVELOPE
_BRAKECATEGORY.fields_by_name['brake_systems_status'].message_type = _BRAKESYSTEMSSTATUS
DESCRIPTOR.message_types_by_name['BrakeSystemsStatus'] = _BRAKESYSTEMSSTATUS
DESCRIPTOR.message_types_by_name['BrakeCategory'] = _BRAKECATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BrakeSystemsStatus = _reflection.GeneratedProtocolMessageType('BrakeSystemsStatus', (_message.Message,), {
  'DESCRIPTOR' : _BRAKESYSTEMSSTATUS,
  '__module__' : 'sensoris.protobuf.categories.brake_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.brake.BrakeSystemsStatus)
  })
_sym_db.RegisterMessage(BrakeSystemsStatus)

BrakeCategory = _reflection.GeneratedProtocolMessageType('BrakeCategory', (_message.Message,), {
  'DESCRIPTOR' : _BRAKECATEGORY,
  '__module__' : 'sensoris.protobuf.categories.brake_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.brake.BrakeCategory)
  })
_sym_db.RegisterMessage(BrakeCategory)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
