# ConsentAcknowledgementModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**consent_id** | **str** |  | 

## Example

```python
from abdm.abdm.model.consent_acknowledgement_model import ConsentAcknowledgementModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentAcknowledgementModel from a JSON string
consent_acknowledgement_model_instance = ConsentAcknowledgementModel.from_json(json)
# print the JSON string representation of the object
print(ConsentAcknowledgementModel.to_json())

# convert the object into a dict
consent_acknowledgement_model_dict = consent_acknowledgement_model_instance.to_dict()
# create an instance of ConsentAcknowledgementModel from a dict
consent_acknowledgement_model_from_dict = ConsentAcknowledgementModel.from_dict(consent_acknowledgement_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


