# coding:utf-8

from mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId

db = client.school
gfs = GridFS(db, collection="book")
doc = gfs.get(ObjectId("63aef3017e0b75054fa65cf1"))
file = open("/Users/lice/downloads/Linux手册.pdf", "wb")
file.write(doc.read())
file.close()
