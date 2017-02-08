from pymongo import MongoClient
import csv
import pprint

server = MongoClient("149.89.150.100")
db = server.DatWay
students_coll = db.students
teachers_coll = db.teachers

def get_ids(class_name):
    ret = list()
    results = students_coll.find({ class_name: {'$exists': True} })
    for result in results:
        del result['_id']
        ret.append(result)
    return ret

with open('teachers.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        teachers_coll.insert_many( get_ids(row['code']) )
