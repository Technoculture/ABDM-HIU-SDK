# AuthMetaModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hint** | **str** |  | [optional] 
**expiry** | **str** |  | [optional] 

## Example

```python
from abdm.abdm.model.auth_meta_model import AuthMetaModel

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMetaModel from a JSON string
auth_meta_model_instance = AuthMetaModel.from_json(json)
# print the JSON string representation of the object
print(AuthMetaModel.to_json())

# convert the object into a dict
auth_meta_model_dict = auth_meta_model_instance.to_dict()
# create an instance of AuthMetaModel from a dict
auth_meta_model_from_dict = AuthMetaModel.from_dict(auth_meta_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


