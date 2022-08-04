from typing import Optional

from pydantic import (
    BaseModel,
    Field,
    StrictInt,
    StrictStr,
    constr,
)

from framework.data.enums import PetStatus


class PetCategory(BaseModel):
    id_: Optional[StrictInt] = Field(alias='id')
    name: Optional[constr(regex='^[a-zA-Z0-9]+[a-zA-Z0-9\\.\\-_]*[a-zA-Z0-9]+$')]


class PetTag(BaseModel):
    id_: Optional[StrictInt] = Field(alias='id')
    name: Optional[StrictStr]


class Pet(BaseModel):
    id_: StrictInt = Field(alias='id')
    name: StrictStr
    photoUrls: list[str]
    category: Optional[PetCategory]
    tags: Optional[list[PetTag]]
    status: Optional[PetStatus]
