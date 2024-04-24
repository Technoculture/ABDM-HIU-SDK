# AccessTokenValidityModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | [**PatientAuthPurposeModelModel**](PatientAuthPurposeModel.md) |  | 
**requester** | [**PatientAuthRequesterModelModel**](PatientAuthRequesterModel.md) |  | 
**expiry** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**limit** | **int** | number of times, the token can be used | 

## Example

```python
from abdm.abdm.model.access_token_validity_model import AccessTokenValidityModel

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenValidityModel from a JSON string
access_token_validity_model_instance = AccessTokenValidityModel.from_json(json)
# print the JSON string representation of the object
print(AccessTokenValidityModel.to_json())

# convert the object into a dict
access_token_validity_model_dict = access_token_validity_model_instance.to_dict()
# create an instance of AccessTokenValidityModel from a dict
access_token_validity_model_from_dict = AccessTokenValidityModel.from_dict(access_token_validity_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


