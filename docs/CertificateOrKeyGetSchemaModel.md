# CertificateOrKeyGetSchemaModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e** | **str** |  | [optional] 
**kid** | **str** |  | [optional] 
**kty** | **str** |  | [optional] 
**n** | **str** |  | [optional] 
**use** | **str** |  | [optional] 
**x5c** | **List[str]** |  | [optional] 
**x5t** | **str** |  | [optional] 
**x5t_s256** | **str** |  | [optional] 
**alg** | **str** |  | [optional] 

## Example

```python
from abdm.abdm.model.certificate_or_key_get_schema_model import CertificateOrKeyGetSchemaModel

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateOrKeyGetSchemaModel from a JSON string
certificate_or_key_get_schema_model_instance = CertificateOrKeyGetSchemaModel.from_json(json)
# print the JSON string representation of the object
print(CertificateOrKeyGetSchemaModel.to_json())

# convert the object into a dict
certificate_or_key_get_schema_model_dict = certificate_or_key_get_schema_model_instance.to_dict()
# create an instance of CertificateOrKeyGetSchemaModel from a dict
certificate_or_key_get_schema_model_from_dict = CertificateOrKeyGetSchemaModel.from_dict(certificate_or_key_get_schema_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


