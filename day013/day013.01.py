#JSON
#It is commonly used for transmitting data in web application 
#{
#    "username":"aakanshagawai123@gmail.com",
#    "password":"Aaku123",
#    "remember":false,
#    "recaptcha_response_field":""
#}
#json->dic
#hashmap-> json


#API-JSON-> dic in python if you want to work it 
#data from py dic-> json->transfer server

#json-English/networking 
#dic=hindi
#me JSON -> Dic (Englih- Hindi)
#dic->JSON->

my_dict={}
print(my_dict)
print(type(my_dict))

my_dict = {"name": "Alice", "age": 25}
print(my_dict)

# Accessing Values:

print(my_dict["name"])  # Output: Alice

# Updating Values:
my_dict["age"] = 26
print(my_dict)

my_dict = {"name": "Alice", "age": 25, "age2": 25}
print(my_dict)

#No duplicate keeys 
#duplicate values are allowed.
my_dict["city"]="New york"
print(my_dict)

#deleting key- value pairs 
del my_dict["age"]
del my_dict["age2"]
print(my_dict)

for key in my_dict:
      print(key)

if "name" in my_dict:
      print("Name is the key in a dictionary")

print(my_dict.get("name"))
print(my_dict["name"])

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

