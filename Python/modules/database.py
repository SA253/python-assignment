#!/usr/bin/python
import xml.dom.minidom

# Open XML document using minidom parser
root = xml.dom.minidom.parse("users.xml")
users = root.documentElement
if users.hasAttribute("org"):  #it checks whether it has org or not
   print("Root element : %s" % users.getAttribute("org"))
mlis=[]
for user in users.getElementsByTagName('user'):
        lis=[]
        fname=user.getElementsByTagName('fname')[0]  # it returns list so we gave indexno as it has only 1 fname
        f = fname.childNodes[0].data  #.data is for text node
        lis.append(f)
        lname=user.getElementsByTagName('lname')[0]
        l = lname.childNodes[0].data
        lis.append(l)
        print(f,l)
        lis=tuple(lis)
        mlis.append(lis)
print(mlis)        
import pymysql
db = pymysql.connect("localhost","root","","test" )
cursor = db.cursor(pymysql.cursors.DictCursor)
data = cursor.executemany("""INSERT INTO User(FIRST_NAME ,LAST_NAME) VALUES (%s,%s) """,mlis )
db.commit()
db.close()