#write ,read and append to file
fo=open('demo.txt','w')  #w=write
fo.write("hello sachin \n")
fo.write("hello saurav \n")
fo.write("hello rahul \n")
fo.close()

#convert to byte
fo=open('demo.txt','w')  #w=write
fo.write("hello sachin \n".encode())
fo.write("hello saurav \n".encode())
fo.write("hello rahul \n".encode())
fo.close()

fo=open('demo.txt','a')  #a=append
fo.write("hello superman \n")
fo.write("hello spiderrman \n")
fo.write("hello batman \n")
fo.close()

fo=open('demo.txt','rb')  #read
data=fo.read()
print(data)
fo.close()


#to read only required data
fo=open('demo.txt','r')
print(type(fo))  # ans: <class '_io.TextIOWrapper'>
print("first:",fo.read(3))  #first 3 character ans: hel
print("second:",fo.read(3))  #next 3 character ans:lo 
fo.close()

fo=open('demo.txt','r')
print("first:",fo.readline())  #first line ans: hello sachin
print("second:",fo.readline())  #next line ans: hello saurav 
fo.close()

#itrating through the file
fo=open('demo.txt','r')   
for line in fo:
    print(line)  # ans: all lines in the file demo is printed
fo.close()

fo=open('demo.txt','rb')   #for binary we put rb similarly for w and a  ans:  b'hello sachin \r\n'(data is in bytes)
for line in fo:
    print(line)  # ans: all lines in the file demo is printed
fo.close()

#to repeat again
fo=open('demo.txt','r')   
for line in fo:
    print(line)  # ans: all lines in the file demo is printed
fo.close()

#convert bytes to string
fo=open('demo.txt','rb')   #for binary we put rb similarly for w and a  ans:  hello sachin 
for line in fo:
    print(line.decode(),end="")  # ans: all lines in the file demo is printed
fo.close()

#another way of writing without using open and close
with open('demo.txt','a') as fo:
    fo.write("hello superman \n")
    fo.write("hello spiderrman \n")
    fo.write("hello batman \n") 