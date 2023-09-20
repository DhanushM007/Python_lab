fname=input("enter the filename:")
infile=open(fname,"r")
line=int(input("enter the first N lines to display:"))
for x in range(line):
    a=infile.readline()
    print(x+1,":",a)
word=input("enter the word to check the no of occurances:")
cnt=0
for line in infile:
    r=line.split()
    cnt+=r.count(word)
print("The word",word,"appears",cnt,"times in the file")