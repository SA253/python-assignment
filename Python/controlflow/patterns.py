n=int(input("enter the number"))
k = 2*n - 2

#pattern1
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end=" ")
    print("\r")

    
#pattern2
for i in range(n,0,-1):
    print("*"*i)
print("\r")    
    
#pattern3
for i in range(n,0,-1):
    print((n-i)*' '+i*"*")
print("\r")
    
    
#pattern4
for i in range(0, n): 
    for j in range(0, k): 
        print(end=" ") 
    k = k - 2
    for j in range(0, i+1): 
        print("* ", end="") 
    print("\r")