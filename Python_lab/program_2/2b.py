def bin2dec(num):
    rev=num[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig)*2**i
        i+=1
    return dec
    
def oct2hex(num):
    num=str(num)
    rev=num[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig)*8**i 
        i+=1
    digits="0123456789ABCDEF"
    x=dec%16
    res=dec//16
    if(res==0):
        return digits[x]
    return oct2hex(res)+digits[x]
num=input("enter a binary number:")
res=bin2dec(num)
print("decimal equivalent of binary number is",res)
num=input("enter a octal number:")
res=oct2hex(num)
print("hexadecimal equivalent of octal number is",res)