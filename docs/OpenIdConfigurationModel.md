# OpenIdConfigurationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwks_uri** | **str** |  | [optional] 

## Example

```python
from abdm.abdm.model.open_id_configuration_model import OpenIdConfigurationModel

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConfigurationModel from a JSON string
open_id_configuration_model_instance = OpenIdConfigurationModel.from_json(json)
# print the JSON string representation of the object
print(OpenIdConfigurationModel.to_json())

# convert the object into a dict
open_id_configuration_model_dict = open_id_configuration_model_instance.to_dict()
# create an instance of OpenIdConfigurationModel from a dict
open_id_configuration_model_from_dict = OpenIdConfigurationModel.from_dict(open_id_configuration_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


