#validating phone number
"""
import re
pattern='^[0-9]{10}$'
phone=input("enter the number")
if re.match(pattern,phone):
    print("correct number")
else:
    print("wrong")
    
 """
    
    
    
#validating email id
import re
pattern='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email=input("enter the emalid")
if re.match(pattern,email):
    print("correct email")
else:
    print("wrong")

    
    


