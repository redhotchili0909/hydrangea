from datetime import datetime
from typing import Optional, Union
from .id import PyObjectId
from bson import ObjectId
from dotenv import load_dotenv
from pydantic import BaseModel, Field, root_validator


load_dotenv()


class SensorModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    garden_id: Union[PyObjectId, None] = Field(default=None, alias="garden_id")

    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        validate_assignment = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {"name": "Temperature", "garden_id": "6359d55bff77b777dd5c92e8"}
        }

        @root_validator
        def number_validator(cls, values):
            values["updated_at"] = datetime.now()
            return values


class UpdateSensorModel(BaseModel):
    name: Optional[str]
    garden_id: Optional[PyObjectId]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"name": "Humidity"}}
