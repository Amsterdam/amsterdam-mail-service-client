# coding: utf-8

# flake8: noqa

"""
    Amsterdam Mail Service API.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "DefaultApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "PreviewRequest",
    "Send200Response",
    "SendRequest",
]

# import apis into sdk package
from amsterdam_mail_service_client.api.default_api import DefaultApi as DefaultApi

# import ApiClient
from amsterdam_mail_service_client.api_response import ApiResponse as ApiResponse
from amsterdam_mail_service_client.api_client import ApiClient as ApiClient
from amsterdam_mail_service_client.configuration import Configuration as Configuration
from amsterdam_mail_service_client.exceptions import OpenApiException as OpenApiException
from amsterdam_mail_service_client.exceptions import ApiTypeError as ApiTypeError
from amsterdam_mail_service_client.exceptions import ApiValueError as ApiValueError
from amsterdam_mail_service_client.exceptions import ApiKeyError as ApiKeyError
from amsterdam_mail_service_client.exceptions import ApiAttributeError as ApiAttributeError
from amsterdam_mail_service_client.exceptions import ApiException as ApiException

# import models into sdk package
from amsterdam_mail_service_client.models.preview_request import PreviewRequest as PreviewRequest
from amsterdam_mail_service_client.models.send200_response import Send200Response as Send200Response
from amsterdam_mail_service_client.models.send_request import SendRequest as SendRequest
