import _json
#Json
#API Response -JSON Strings 
json_data_str={'name':'Aakansha','age':'24','city':'Pune'}
#json to dict
import json

json_data_str = '{"key": "value", "number": 42}'
py_dict = json.loads(json_data_str)

print(py_dict)
print(type(py_dict))
print(py_dict["age"])       

