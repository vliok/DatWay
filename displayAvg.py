from pymongo import MongoClient

server = MongoClient("149.89.150.100")
db = server.DatWay
s = db.students

def findAvg( id ):
    dic = s.find_one( {"id":id} )
    div = 0
    total = 0
    retVal = 0
    for field in dic:
        if field in ["systems", "softdev", "ceramics", "greatbooks"]:
            total += int(dic[field])
            div += 1
    if div > 0:
        retVal = total / div
    return retVal

data = s.find()
for student in data:
    print "name = " + student["name"] + " id = " + student["id"] + " avg = " + str( findAvg(student["id"]) )
