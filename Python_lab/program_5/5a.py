import re
def ischkphoneno(num):
    if len(num)!=12:
        return False
    for i in range(len(num)):
        if i==3 or i==7:
            if num[i]!="-":
                return False
        else:
            if num[i].isdigit()==False:
                return False
    return True

def validatephone(num):
    res=re.findall("\d{3}-\d{3}-\d{4}",num)
    if res:
        return True
    else:
        return False
    
num=input("enter a string:")
if ischkphoneno(num):
    print("valid phone number")
else:
    print("Invalid phone number")
if validatephone(num):
    print("valid phone number")
else:
    print("Invalid phone number")
    
    