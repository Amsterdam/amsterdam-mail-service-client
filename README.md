# amsterdam-mail-service-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Generator version: 7.14.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Amsterdam/amsterdam-mail-service-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Amsterdam/amsterdam-mail-service-client.git`)

Then import the package:
```python
import amsterdam_mail_service_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import amsterdam_mail_service_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import amsterdam_mail_service_client
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
    except ApiException as e:
        print("Exception when calling DefaultApi->preview: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**preview**](docs/DefaultApi.md#preview) | **POST** /preview/ | Renders a preview of the mail that would be sent.
*DefaultApi* | [**send**](docs/DefaultApi.md#send) | **POST** /send/ | Sends mail using the provided input and the template on the server.


## Documentation For Models

 - [PreviewRequest](docs/PreviewRequest.md)
 - [Send200Response](docs/Send200Response.md)
 - [SendRequest](docs/SendRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




