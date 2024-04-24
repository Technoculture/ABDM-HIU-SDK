# PatientAddressModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**pincode** | **str** |  | [optional] 

## Example

```python
from abdm.abdm.model.patient_address_model import PatientAddressModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAddressModel from a JSON string
patient_address_model_instance = PatientAddressModel.from_json(json)
# print the JSON string representation of the object
print(PatientAddressModel.to_json())

# convert the object into a dict
patient_address_model_dict = patient_address_model_instance.to_dict()
# create an instance of PatientAddressModel from a dict
patient_address_model_from_dict = PatientAddressModel.from_dict(patient_address_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


