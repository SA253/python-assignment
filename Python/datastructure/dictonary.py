#dict of tuple
t={
       (1,2):"sachin",
       (3,4):"saurav",
       (5,6):"virat"
       
       }
       
print(t[(1,2)])
print(t[(3,4)])
print(t[(5,6)])

#dict of list
t={
       "a":[1,2],
       "b":[3,4],
       "c":[5,6]
       }
       
print(t["a"])
print(t["b"])
print(t["c"])
#dict of set
t={
       "a":{1,2},
       "b":{3,4},
       "c":{5,6},
       }
       
print(t["a"])
print(t["b"])
print(t["c"])


#dict of dictonary
t={
      
'fname':"sachin",
'lname':"tendulkar",
'address':{
'houseno':17,
'area':"worli",
'city':"mumbai",
'pincode':"220022"
}
       }
       
print(t['address']['pincode'])
print(t['address']['city'])