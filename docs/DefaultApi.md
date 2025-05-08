# amsterdam_mail_service_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**preview**](DefaultApi.md#preview) | **POST** /preview/ | Renders a preview of the mail that would be sent.
[**send**](DefaultApi.md#send) | **POST** /send/ | Sends mail using the provided input and the template on the server.


# **preview**
> str preview(preview_request=preview_request)

Renders a preview of the mail that would be sent.

### Example


```python
import amsterdam_mail_service_client
from amsterdam_mail_service_client.models.preview_request import PreviewRequest
from amsterdam_mail_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = amsterdam_mail_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with amsterdam_mail_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amsterdam_mail_service_client.DefaultApi(api_client)
    preview_request = amsterdam_mail_service_client.PreviewRequest() # PreviewRequest | Input required for rendering a preview (optional)

    try:
        # Renders a preview of the mail that would be sent.
        api_response = await api_instance.preview(preview_request=preview_request)
        print("The response of DefaultApi->preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_request** | [**PreviewRequest**](PreviewRequest.md)| Input required for rendering a preview | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send**
> Send200Response send(send_request=send_request)

Sends mail using the provided input and the template on the server.

### Example


```python
import amsterdam_mail_service_client
from amsterdam_mail_service_client.models.send200_response import Send200Response
from amsterdam_mail_service_client.models.send_request import SendRequest
from amsterdam_mail_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = amsterdam_mail_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with amsterdam_mail_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amsterdam_mail_service_client.DefaultApi(api_client)
    send_request = amsterdam_mail_service_client.SendRequest() # SendRequest | Input required for sending mail (optional)

    try:
        # Sends mail using the provided input and the template on the server.
        api_response = await api_instance.send(send_request=send_request)
        print("The response of DefaultApi->send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_request** | [**SendRequest**](SendRequest.md)| Input required for sending mail | [optional] 

### Return type

[**Send200Response**](Send200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

