# coding:utf-8

from mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId
import math
import datetime


db = client.school
gfs = GridFS(db, collection="book")
book = gfs.find_one({"filename": "Linux_Probe.pdf"})
print(book.filename)
print(book.type)
print(book.keyword)
print("%dM" % math.ceil(book.length/1024/1024))
print(type(book))
print("----------------------------")
books = gfs.find({"type": "PDF"})
for i in books:
    uploaddate = i.uploadDate + datetime.timedelta(hours=8)
    uploaddate = uploaddate.strftime("%Y-%m-%d %H:%M:%S")
    print(i._id, i.filename, uploaddate)
print("----------------------------")
rs = gfs.exists(ObjectId("63aef3017e0b75054fa65cf1"))
print(rs)
rs = gfs.exists(**{"filename": "123.html"})
print(rs)
