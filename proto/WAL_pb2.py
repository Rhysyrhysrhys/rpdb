# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WAL.proto
"""Generated protocol buffer code."""
# mypy: ignore-errors
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\tWAL.proto\x12\x04rpdb"\xa5\x01\n\x08WALEntry\x12\x11\n\ttimestamp\x18\x01 \x01(\x05\x12&\n\x07op_type\x18\x02 \x01(\x0e\x32\x15.rpdb.WALEntry.OpType\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x12\n\x05value\x18\x04 \x01(\tH\x00\x88\x01\x01"3\n\x06OpType\x12\t\n\x05\x42\x45GIN\x10\x00\x12\x07\n\x03SET\x10\x01\x12\t\n\x05UNSET\x10\x02\x12\n\n\x06\x43OMMIT\x10\x03\x42\x08\n\x06_value"&\n\x03WAL\x12\x1f\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x0e.rpdb.WALEntryb\x06proto3'
)


_WALENTRY = DESCRIPTOR.message_types_by_name["WALEntry"]
_WAL = DESCRIPTOR.message_types_by_name["WAL"]
_WALENTRY_OPTYPE = _WALENTRY.enum_types_by_name["OpType"]
WALEntry = _reflection.GeneratedProtocolMessageType(
    "WALEntry",
    (_message.Message,),
    {
        "DESCRIPTOR": _WALENTRY,
        "__module__": "WAL_pb2"
        # @@protoc_insertion_point(class_scope:rpdb.WALEntry)
    },
)
_sym_db.RegisterMessage(WALEntry)

WAL = _reflection.GeneratedProtocolMessageType(
    "WAL",
    (_message.Message,),
    {
        "DESCRIPTOR": _WAL,
        "__module__": "WAL_pb2"
        # @@protoc_insertion_point(class_scope:rpdb.WAL)
    },
)
_sym_db.RegisterMessage(WAL)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _WALENTRY._serialized_start = 20
    _WALENTRY._serialized_end = 185
    _WALENTRY_OPTYPE._serialized_start = 124
    _WALENTRY_OPTYPE._serialized_end = 175
    _WAL._serialized_start = 187
    _WAL._serialized_end = 225
# @@protoc_insertion_point(module_scope)
