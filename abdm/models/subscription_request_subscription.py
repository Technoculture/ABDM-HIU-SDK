# coding: utf-8

"""
Health Repository Provider Specifications for HIU

The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from abdm.models.consent_manager_patient_id import ConsentManagerPatientID
from abdm.models.organization_representation import OrganizationRepresentation
from abdm.models.subscription_category import SubscriptionCategory
from abdm.models.subscription_period import SubscriptionPeriod
from abdm.models.use_purpose import UsePurpose
from typing import Set
from typing_extensions import Self


class SubscriptionRequestSubscription(BaseModel):
    """
    SubscriptionRequestSubscription
    """  # noqa: E501

    purpose: UsePurpose
    patient: ConsentManagerPatientID
    hiu: OrganizationRepresentation
    hips: Optional[List[OrganizationRepresentation]] = None
    categories: List[SubscriptionCategory]
    period: SubscriptionPeriod
    __properties: ClassVar[List[str]] = [
        "purpose",
        "patient",
        "hiu",
        "hips",
        "categories",
        "period",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SubscriptionRequestSubscription from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of purpose
        if self.purpose:
            _dict["purpose"] = self.purpose.to_dict()
        # override the default output from pydantic by calling `to_dict()` of patient
        if self.patient:
            _dict["patient"] = self.patient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hiu
        if self.hiu:
            _dict["hiu"] = self.hiu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in hips (list)
        _items = []
        if self.hips:
            for _item in self.hips:
                if _item:
                    _items.append(_item.to_dict())
            _dict["hips"] = _items
        # override the default output from pydantic by calling `to_dict()` of period
        if self.period:
            _dict["period"] = self.period.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionRequestSubscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "purpose": UsePurpose.from_dict(obj["purpose"])
                if obj.get("purpose") is not None
                else None,
                "patient": ConsentManagerPatientID.from_dict(obj["patient"])
                if obj.get("patient") is not None
                else None,
                "hiu": OrganizationRepresentation.from_dict(obj["hiu"])
                if obj.get("hiu") is not None
                else None,
                "hips": [
                    OrganizationRepresentation.from_dict(_item) for _item in obj["hips"]
                ]
                if obj.get("hips") is not None
                else None,
                "categories": obj.get("categories"),
                "period": SubscriptionPeriod.from_dict(obj["period"])
                if obj.get("period") is not None
                else None,
            }
        )
        return _obj
