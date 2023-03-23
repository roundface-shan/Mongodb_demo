# coding:utf-8

from mongo_db import client
from gridfs import GridFS

db = client.school
gfs = GridFS(db, collection="book")

file = open("/Users/lice/downloads/Linux_Probe.pdf", "rb")
args = {"type": "PDF", "keyword": "Linux"}
gfs.put(file, filename="Linux_Probe.pdf", **args)
file.close()