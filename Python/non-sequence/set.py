
#set
s1={1,None,"hello",False,1.5}
print(type(s1))
print(s1)

s1={1,2,3,4}
s2={3,4,5,6}
s3={1,2}
print(s1|s2)#union
print(s1&s2)#intersection
print(s1-s2)#subraction s1 from s2
print(s2-s1)#subraction s2 from s1&s2
print(s3<s1)#is subset