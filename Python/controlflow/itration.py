#for string
data="hellopython"
for d in data:
    print(d)
    
    
#for tuple
data1=1,2,3,"hello"
for d1 in data1:
    print(d1)
    
    
#for list
data2=[4,5,6]
for d2 in data2:
    print(d2)
    
    
    
#for set
data3={"hello","hi","namaste"}
for d1 in data3:
    print(d1)
    
    
    
#for dict
s1={
'fname':"sachin",
'lname':"tendulkar"
}
for d1 in s1.values():
    print(d1)
 


#range from 0 to 10  
disc=range(10)
print(type(d))
for d in disc:
    print(d)

 
 #range from 100 to 200 with 5 as diff   
disc=range(100,200,5)
print(type(d))
for d in disc:
    print(d)
    
    
    
#prime number
num=int(input("eneter the number"))
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break   
else:
    print("prime")