#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
<<<<<<< HEAD
my_model.name = "Holberton"
=======
my_model.name = "My First Model"
>>>>>>> 87bf94b12d55c91041ceb97c65a2d0e8f07f554d
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
<<<<<<< HEAD
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                   my_model_json[key]))

=======
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
>>>>>>> 87bf94b12d55c91041ceb97c65a2d0e8f07f554d
