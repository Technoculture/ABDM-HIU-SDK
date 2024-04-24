# UsePurposeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**code** | **str** | From the fixed set, documented at refUri | 
**ref_uri** | **str** |  | [optional] 

## Example

```python
from abdm.abdm.model.use_purpose_model import UsePurposeModel

# TODO update the JSON string below
json = "{}"
# create an instance of UsePurposeModel from a JSON string
use_purpose_model_instance = UsePurposeModel.from_json(json)
# print the JSON string representation of the object
print(UsePurposeModel.to_json())

# convert the object into a dict
use_purpose_model_dict = use_purpose_model_instance.to_dict()
# create an instance of UsePurposeModel from a dict
use_purpose_model_from_dict = UsePurposeModel.from_dict(use_purpose_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


