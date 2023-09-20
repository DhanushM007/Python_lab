import re
phone_pat=re.compile(r'\+91\d{10}')
email_pat=re.compile(r'[0-9 A-Z a-z]+@gmail.com')

f=open("C:\\Users\\jaswa\\Desktop\\hii.txt","r")

for line in f:
    matches=phone_pat.findall(line)
    for match in matches:
        print(match)
f.seek(0)
for line in f:
    matches=email_pat.findall(line)
    for match in matches:
        print(match)