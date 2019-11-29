#to do both read and write
fo=open('demo1.txt','w+')  #w=write
fo.write("hello sachin \n")
fo.write("hello saurav \n")
fo.write("hello rahul \n")
for line in fo:
    print(line)
fo.close()

#to read image
fo=open('img.jpg','rb')
data=fo.read()

fo.close()
ff=open('img1.jpg','wb')

ff.write(data)
ff.close()
