# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: register.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='register.proto',
  package='register',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0eregister.proto\x12\x08register\"\x07\n\x05\x45mpty\"7\n\x04\x44\x61ta\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\",\n\x0c\x44\x61taResponse\x12\x1c\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0e.register.Data2\xda\x01\n\rDataProcessor\x12-\n\x07GetData\x12\x0f.register.Empty\x1a\x0f.register.Empty\"\x00\x12\x34\n\x08PostData\x12\x0e.register.Data\x1a\x16.register.DataResponse\"\x00\x12\x33\n\x07PutData\x12\x0e.register.Data\x1a\x16.register.DataResponse\"\x00\x12/\n\nDeleteData\x12\x0e.register.Data\x1a\x0f.register.Empty\"\x00\x62\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='register.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=28,
  serialized_end=35,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='register.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='register.Data._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='register.Data.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='register.Data.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=37,
  serialized_end=92,
)


_DATARESPONSE = _descriptor.Descriptor(
  name='DataResponse',
  full_name='register.DataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='register.DataResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=94,
  serialized_end=138,
)

_DATARESPONSE.fields_by_name['data'].message_type = _DATA
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['DataResponse'] = _DATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:register.Empty)
  })
_sym_db.RegisterMessage(Empty)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:register.Data)
  })
_sym_db.RegisterMessage(Data)

DataResponse = _reflection.GeneratedProtocolMessageType('DataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATARESPONSE,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:register.DataResponse)
  })
_sym_db.RegisterMessage(DataResponse)



_DATAPROCESSOR = _descriptor.ServiceDescriptor(
  name='DataProcessor',
  full_name='register.DataProcessor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=141,
  serialized_end=359,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetData',
    full_name='register.DataProcessor.GetData',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PostData',
    full_name='register.DataProcessor.PostData',
    index=1,
    containing_service=None,
    input_type=_DATA,
    output_type=_DATARESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PutData',
    full_name='register.DataProcessor.PutData',
    index=2,
    containing_service=None,
    input_type=_DATA,
    output_type=_DATARESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteData',
    full_name='register.DataProcessor.DeleteData',
    index=3,
    containing_service=None,
    input_type=_DATA,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAPROCESSOR)

DESCRIPTOR.services_by_name['DataProcessor'] = _DATAPROCESSOR

# @@protoc_insertion_point(module_scope)
