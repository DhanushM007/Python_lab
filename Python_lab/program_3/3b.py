def compare(s,p):
    count=0
    n=min(len(s),len(p))
    for i in range(n):
        if s[i]==p[i]:
            count+=1
    return count

s1=input("enter string 1:")
s2=input("enter string 2:")
mx=max(len(s1),len(s2))
count=compare(s1,s2)
similarity=(count/mx)*100
print("No of letters matched:",count)
print("similarity between two strings:",similarity)
            
    