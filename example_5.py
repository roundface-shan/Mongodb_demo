# coding:utf-8

from mongo_db import client


students = client.school.student.find({}).skip(0).limit(10)
for i in students:
    print(i["name"])

names = client.school.student.distinct("name")

students = client.school.student.find({}).sort([("name", -1)])
