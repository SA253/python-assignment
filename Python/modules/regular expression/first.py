import re
pattern="zomato"
#text="does this text match the pattern?"   #ans:none ,not found
text="zomatonn"    # ans: <re.Match object; span=(0, 6), match='zomato'> , found match
print(re.search(pattern,text))
if re.search(pattern,text):
    print("found match")
else:
    print("not found")
    
    
    
    
#type2 (gives only first occurance of the word) ans: 5 9 this
pattern="t[a-z]*"
text="does this text match the pattern?"   
match=re.search(pattern,text)
if match:
    print("found match")
    print(match.start(),match.end(),text[match.start():match.end()])
else:
    print("not found")
    
    
#type3 (gives all the occurances of the word) 
"""ans: 5 9 this
5 9 this
10 14 text
17 20 tch
21 24 the
27 32 ttern"""
pattern="t[a-z]*"
text="does this text match the pattern?"   
matches=re.finditer(pattern,text)
for match in matches:
    print(match.start(),match.end(),text[match.start():match.end()])
    
    
#combining two patterns  
"""ans:
0 3 tom
8 13  this
13 18  text
24 28  the""" 
pattern="\st[a-z]*|^t[a-z]*" #\s is space before t only will be considered ,
text="Tom,does this text match the pattern?"   
matches=re.findall(pattern,text,re.I)    # re.I --ignores casesensitivity so here we can use T or t
print(matches)

