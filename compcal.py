import json
from StringIO import StringIO
import requests
import pprint
import sys
import mysql.connector
import MySQLdb

#database connection

cnx = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="rajhack")

cursor = cnx.cursor()
count=0


cursor.execute("select * from compcal")
result = cursor.fetchall()
for r in result:
    bamid=r[5]
    #saurl = 'https://api.github.com/users/'+r[0]+'?access_token=c9896707dc4ee6a9b7494758afb407a07215c37b'
    saurl='https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/bahmashah/hofAndMembers/'+bamid+'?client_id=ad7288a4-7764-436d-a727-783a977f1fe1'
    resp = requests.get(saurl)
    contentJson = resp.json()         
    if resp.status_code == 200:
        wat=r[2]
        temp=r[3]
        ph=r[4]
        duration=r[6]
        comp= wat+temp+ph+duration
        pprint.pprint(contentJson)
        print "The approximate compensation is  "+comp
        
        

