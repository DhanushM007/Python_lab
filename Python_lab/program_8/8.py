class palistr:
    def __init__(self):
        self.ispali=False

    def chkpali(self,mystr):
        if mystr==mystr[::-1]:
            self.ispali=True
        else:
            self.ispali=False
        return self.ispali
    
class paliInt(palistr):
    def __init__(self):
        self.ispali=False
        
    def chkpali(self,val):
        dig=val
        rev=0
        while dig!=0:
            rem=dig%10
            rev=rev*10+rem
            dig=dig//10
        
        if val==rev:
            self.ispali=True
        else:
            self.ispali=False
        return self.ispali
            
    
    
st=input("enter a string:")
stobj=palistr()
if stobj.chkpali(st):
    print("given string is a Palindrome")
else:
    print("given string is not a Palindrome")
    
val=int(input("enter a integer:"))
intobj=paliInt()
if intobj.chkpali(val):
    print("given integer is a Palindrome")
else:
    print("given integer is not a Palindrome")