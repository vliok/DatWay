from pymongo import MongoClient
import csv

f = open("peeps.csv")
p = csv.DictReader(f)

f = open("courses.csv")
c = csv.DictReader(f)

def merge( thing1, thing2 ):
    list1 = []
    list2 = []
    for dic in thing1:
        list1.append(dic)
    for dic in thing2:
        list2.append(dic)
    for dic in list1:
        for dic2 in list2:
            if dic2["id"] == dic["id"]:
                index = list1.index(dic)
                code = dic2["code"]
                mark = dic2["mark"]
                list1[index][code] = mark
    return list1

'''                                                                                                                                 
test =  merge( p, c )                                                                                                              
                                                                                                                                    
for stuff in test:                                                                                                               
print stuff                                                                                                                      
'''

server = MongoClient("149.89.150.100")
db = server.DatWay
s = db.students
merged = merge( p, c )
s.insert_many( merged )
