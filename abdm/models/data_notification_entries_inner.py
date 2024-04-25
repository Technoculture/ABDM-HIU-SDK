# coding: utf-8

"""
Health Repository Provider Specifications for HIU

The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from pydantic import (
    BaseModel,
    ValidationError,
    field_validator,
)
from typing import Optional
from abdm.models.entry_content import EntryContent
from abdm.models.entry_link import EntryLink
from typing import Union, Any, Set, TYPE_CHECKING, Dict
from typing_extensions import Self

DATANOTIFICATIONENTRIESINNER_ANY_OF_SCHEMAS = ["EntryContent", "EntryLink"]


class DataNotificationEntriesInner(BaseModel):
    """
    DataNotificationEntriesInner
    """

    # data type: EntryContent
    anyof_schema_1_validator: Optional[EntryContent] = None
    # data type: EntryLink
    anyof_schema_2_validator: Optional[EntryLink] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[EntryContent, EntryLink]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = {"EntryContent", "EntryLink"}

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`"
                )
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used."
                )
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator("actual_instance")
    def actual_instance_must_validate_anyof(cls, v):
        
        error_messages = []
        # validate data type: EntryContent
        if not isinstance(v, EntryContent):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `EntryContent`"
            )
        else:
            return v

        # validate data type: EntryLink
        if not isinstance(v, EntryLink):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EntryLink`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError(
                "No match found when setting the actual_instance in DataNotificationEntriesInner with anyOf schemas: EntryContent, EntryLink. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[EntryContent] = None
        try:
            instance.actual_instance = EntryContent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[EntryLink] = None
        try:
            instance.actual_instance = EntryLink.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into DataNotificationEntriesInner with anyOf schemas: EntryContent, EntryLink. Details: "
                + ", ".join(error_messages)
            )
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(
            self.actual_instance.to_json
        ):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], EntryContent, EntryLink]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(
            self.actual_instance.to_dict
        ):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
