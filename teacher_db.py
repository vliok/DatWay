from pymongo import MongoClient
import csv
import pprint

server = MongoClient("149.89.150.100")
db = server.DatWay
students_coll = db.students

c = students_coll.find({})
for doc in c:
    pprint.pprint(doc)

with open('teachers.csv', 'r') as f:
    reader = csv.DictReader(f)


