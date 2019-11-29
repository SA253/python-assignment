#sorting
obj=[
    {"id":"1","name":"chocos","cost":50,"brand":"nestle","rating":"5","discount":"10%","category":"food"},
    {"id":"2","name":"laptop","cost":50000,"brand":"hp","rating":"5","discount":"15%","category":"electronics"},
    {"id":"3","name":"washinmachine","cost":10000,"brand":"bosch","rating":"4.5","discount":"20%","category":"electronics"},
    {"id":"4","name":"mobile","cost":6000,"brand":"mi","rating":"4","discount":"10%","category":"electronics"},
    {"id":"5","name":"trolly","cost":8000,"brand":"skybags","rating":"4","discount":"15%","category":"goods"},
    {"id":"6","name":"dress","cost":5000,"brand":"pantaloons","rating":"5","discount":"30%","category":"clothes"}
    ]
l=[["cost",True],["cost",False],["rating",True],["rating",False],["discount",True],["discount",False]]

n=int(input("enter the number"))
obj.sort(key=lambda el:el[l[n-1][0]],reverse=l[n-1][1])  #sorting in asc and desc
print(obj)

   
    
    
#filtering
newobj=filter(lambda el:el["brand"]=="electronics",obj)
for i in newobj:
    print("hello")
    print('{brand}'.format(**i))