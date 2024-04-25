# coding: utf-8

"""
Health Repository Provider Specifications for HIU

The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from abdm.models.hiu_patient_status_notification_model import (
    HiuPatientStatusNotificationModel,
)
from abdm.models.patient_status_notification_model import PatientStatusNotificationModel

from abdm.api_client import ApiClient, RequestSerialized
from abdm.api_response import ApiResponse
from abdm.rest import RESTResponseType


class PatientNotificationAPI:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def v05_patients_status_notify_post(
        self,
        authorization: Annotated[
            StrictStr,
            Field(
                description="Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge."
            ),
        ],
        x_hiu_id: Annotated[
            StrictStr,
            Field(
                description="Identifier of the health information user to which the request was intended."
            ),
        ],
        hiu_patient_status_notification_model: HiuPatientStatusNotificationModel,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Notification sent by Consent Manager

        This API is to send patient's status (ACTIVE/DEACTIVATED/DELETED) to the HIU.

        :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. (required)
        :type authorization: str
        :param x_hiu_id: Identifier of the health information user to which the request was intended. (required)
        :type x_hiu_id: str
        :param hiu_patient_status_notification_model: (required)
        :type hiu_patient_status_notification_model: HiuPatientStatusNotificationModel
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._v05_patients_status_notify_post_serialize(
            authorization=authorization,
            x_hiu_id=x_hiu_id,
            hiu_patient_status_notification_model=hiu_patient_status_notification_model,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "202": None,
            "500": "ErrorResponseModelModel",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def v05_patients_status_notify_post_with_http_info(
        self,
        authorization: Annotated[
            StrictStr,
            Field(
                description="Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge."
            ),
        ],
        x_hiu_id: Annotated[
            StrictStr,
            Field(
                description="Identifier of the health information user to which the request was intended."
            ),
        ],
        hiu_patient_status_notification_model: HiuPatientStatusNotificationModel,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Notification sent by Consent Manager

        This API is to send patient's status (ACTIVE/DEACTIVATED/DELETED) to the HIU.

        :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. (required)
        :type authorization: str
        :param x_hiu_id: Identifier of the health information user to which the request was intended. (required)
        :type x_hiu_id: str
        :param hiu_patient_status_notification_model: (required)
        :type hiu_patient_status_notification_model: HiuPatientStatusNotificationModel
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._v05_patients_status_notify_post_serialize(
            authorization=authorization,
            x_hiu_id=x_hiu_id,
            hiu_patient_status_notification_model=hiu_patient_status_notification_model,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "202": None,
            "500": "ErrorResponseModelModel",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def v05_patients_status_notify_post_without_preload_content(
        self,
        authorization: Annotated[
            StrictStr,
            Field(
                description="Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge."
            ),
        ],
        x_hiu_id: Annotated[
            StrictStr,
            Field(
                description="Identifier of the health information user to which the request was intended."
            ),
        ],
        hiu_patient_status_notification_model: HiuPatientStatusNotificationModel,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Notification sent by Consent Manager

        This API is to send patient's status (ACTIVE/DEACTIVATED/DELETED) to the HIU.

        :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. (required)
        :type authorization: str
        :param x_hiu_id: Identifier of the health information user to which the request was intended. (required)
        :type x_hiu_id: str
        :param hiu_patient_status_notification_model: (required)
        :type hiu_patient_status_notification_model: HiuPatientStatusNotificationModel
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._v05_patients_status_notify_post_serialize(
            authorization=authorization,
            x_hiu_id=x_hiu_id,
            hiu_patient_status_notification_model=hiu_patient_status_notification_model,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "202": None,
            "500": "ErrorResponseModelModel",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _v05_patients_status_notify_post_serialize(
        self,
        authorization,
        x_hiu_id,
        hiu_patient_status_notification_model,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if authorization is not None:
            _header_params["Authorization"] = authorization
        if x_hiu_id is not None:
            _header_params["X-HIU-ID"] = x_hiu_id
        # process the form parameters
        # process the body parameter
        if hiu_patient_status_notification_model is not None:
            _body_params = hiu_patient_status_notification_model

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "application/xml"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json", "application/xml"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/v0.5/patients/status/notify",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def v05_patients_status_on_notify_post(
        self,
        authorization: Annotated[
            StrictStr,
            Field(
                description="Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge."
            ),
        ],
        x_cm_id: Annotated[
            StrictStr,
            Field(
                description="Suffix of the consent manager to which the request was intended."
            ),
        ],
        patient_status_notification_model: PatientStatusNotificationModel,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Acknowledgment by HIU

        This  API is to check if the Status is successfully sent for patient (Active/Deactivate/DELETED) to HIU and then \"status\" will be \"OK\" with no error.

        :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. (required)
        :type authorization: str
        :param x_cm_id: Suffix of the consent manager to which the request was intended. (required)
        :type x_cm_id: str
        :param patient_status_notification_model: (required)
        :type patient_status_notification_model: PatientStatusNotificationModel
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._v05_patients_status_on_notify_post_serialize(
            authorization=authorization,
            x_cm_id=x_cm_id,
            patient_status_notification_model=patient_status_notification_model,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "202": None,
            "500": "ErrorResponseModelModel",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def v05_patients_status_on_notify_post_with_http_info(
        self,
        authorization: Annotated[
            StrictStr,
            Field(
                description="Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge."
            ),
        ],
        x_cm_id: Annotated[
            StrictStr,
            Field(
                description="Suffix of the consent manager to which the request was intended."
            ),
        ],
        patient_status_notification_model: PatientStatusNotificationModel,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Acknowledgment by HIU

        This  API is to check if the Status is successfully sent for patient (Active/Deactivate/DELETED) to HIU and then \"status\" will be \"OK\" with no error.

        :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. (required)
        :type authorization: str
        :param x_cm_id: Suffix of the consent manager to which the request was intended. (required)
        :type x_cm_id: str
        :param patient_status_notification_model: (required)
        :type patient_status_notification_model: PatientStatusNotificationModel
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._v05_patients_status_on_notify_post_serialize(
            authorization=authorization,
            x_cm_id=x_cm_id,
            patient_status_notification_model=patient_status_notification_model,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "202": None,
            "500": "ErrorResponseModelModel",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def v05_patients_status_on_notify_post_without_preload_content(
        self,
        authorization: Annotated[
            StrictStr,
            Field(
                description="Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge."
            ),
        ],
        x_cm_id: Annotated[
            StrictStr,
            Field(
                description="Suffix of the consent manager to which the request was intended."
            ),
        ],
        patient_status_notification_model: PatientStatusNotificationModel,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Acknowledgment by HIU

        This  API is to check if the Status is successfully sent for patient (Active/Deactivate/DELETED) to HIU and then \"status\" will be \"OK\" with no error.

        :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. (required)
        :type authorization: str
        :param x_cm_id: Suffix of the consent manager to which the request was intended. (required)
        :type x_cm_id: str
        :param patient_status_notification_model: (required)
        :type patient_status_notification_model: PatientStatusNotificationModel
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._v05_patients_status_on_notify_post_serialize(
            authorization=authorization,
            x_cm_id=x_cm_id,
            patient_status_notification_model=patient_status_notification_model,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "202": None,
            "500": "ErrorResponseModelModel",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _v05_patients_status_on_notify_post_serialize(
        self,
        authorization,
        x_cm_id,
        patient_status_notification_model,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if authorization is not None:
            _header_params["Authorization"] = authorization
        if x_cm_id is not None:
            _header_params["X-CM-ID"] = x_cm_id
        # process the form parameters
        # process the body parameter
        if patient_status_notification_model is not None:
            _body_params = patient_status_notification_model

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "application/xml"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json", "application/xml"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/v0.5/patients/status/on-notify",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
