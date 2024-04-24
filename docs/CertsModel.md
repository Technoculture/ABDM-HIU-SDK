# CertsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[CertificateOrKeyGetSchemaModelModel]**](CertificateOrKeyGetSchemaModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.certs_model import CertsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CertsModel from a JSON string
certs_model_instance = CertsModel.from_json(json)
# print the JSON string representation of the object
print(CertsModel.to_json())

# convert the object into a dict
certs_model_dict = certs_model_instance.to_dict()
# create an instance of CertsModel from a dict
certs_model_from_dict = CertsModel.from_dict(certs_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


