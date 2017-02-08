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
    return [result['id'] for result in results]

with open('teachers.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        new_doc = dict()
        new_doc['name'] = row['teacher']
        new_doc['class'] = row['code']
        new_doc['period'] = row['period']
        new_doc['students'] = get_ids(row['code'])

        teachers_coll.insert_one(new_doc)
