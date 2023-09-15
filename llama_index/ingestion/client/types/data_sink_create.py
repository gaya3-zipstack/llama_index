# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from llama_index.bridge.pydantic import pydantic

from ..core.datetime_utils import serialize_datetime
from .data_sink_type_enum import DataSinkTypeEnum


class DataSinkCreate(pydantic.BaseModel):
    """
    Schema for creating a data sink.
    """

    name: str
    sink_type: DataSinkTypeEnum
    metadata_blob: typing.Dict[str, typing.Any]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
