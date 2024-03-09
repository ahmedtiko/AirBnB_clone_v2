#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
<<<<<<< HEAD
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
print(my_model)

=======
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
>>>>>>> 87bf94b12d55c91041ceb97c65a2d0e8f07f554d
