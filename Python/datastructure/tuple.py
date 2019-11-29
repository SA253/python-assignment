#tuple of tuple
t=(
       (1,2),
       (3,4),
       (5,6)
       )
       
print(t[0])
print(t[0][0])
print(t[0][1])

print(t[1])
print(t[1][0])
print(t[1][1])
       
print(t[2])
print(t[2][0])
print(t[2][1])


#tuple of list
t=(
       [1,2],
       [3,4],
       [5,6]
       )
       
print(t[0])
print(t[0][0])
print(t[0][1])

print(t[1])
print(t[1][0])
print(t[1][1])
       
print(t[2])
print(t[2][0])
print(t[2][1])
       
t[0][0]=100
print(t)

#tuple of set
t=(
       {1,2},
       {3,4},
       {5,6},
       )
       
print(t[0])
print(t[1])       
print(t[2])

#tuple of dictonary
t=(
       {
'fname':"sachin",
'lname':"tendulkar"
},
       {
'fname':"dhoni",
'lname':"MS"
},
       {
'fname':"virat",
'lname':"kohli"
},
       )
       
print(t[0])
print(t[1])       
print(t[2])