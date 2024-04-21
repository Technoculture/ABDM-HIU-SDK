from pydantic import BaseModel, Field


class AbhaNumber(BaseModel):
    abha_number: str = Field(
        ..., description="ABHA number", min_length=1, max_length=50
    )
