# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experiment_progress.proto

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
  name='experiment_progress.proto',
  package='harmonyServer',
  syntax='proto2',
  serialized_pb=_b('\n\x19\x65xperiment_progress.proto\x12\rharmonyServer\"2\n\x12\x45xperimentProgress\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08progress\x18\x02 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EXPERIMENTPROGRESS = _descriptor.Descriptor(
  name='ExperimentProgress',
  full_name='harmonyServer.ExperimentProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='harmonyServer.ExperimentProgress.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='progress', full_name='harmonyServer.ExperimentProgress.progress', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['ExperimentProgress'] = _EXPERIMENTPROGRESS

ExperimentProgress = _reflection.GeneratedProtocolMessageType('ExperimentProgress', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENTPROGRESS,
  __module__ = 'experiment_progress_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.ExperimentProgress)
  ))
_sym_db.RegisterMessage(ExperimentProgress)


# @@protoc_insertion_point(module_scope)
