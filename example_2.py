# coding:utf-8

from mongo_db import client


try:
    teachers = client.school.teacher.find({})
    for i in teachers:
        print(i["_id"], i["name"])
    print("_________________________")
    teacher = client.school.teacher.find_one({"name": "李璐"})
    print(teacher["_id"], teacher["name"])
except Exception as e:
    print(e)
