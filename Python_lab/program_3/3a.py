sentence=input("enter a sentence:")
wordcnt=upcnt=lowcnt=digcnt=0
wordcnt=sentence.split()
for ch in sentence:
    if ch>='A' and ch<='Z':
        upcnt+=1
    if ch>='a' and ch<='z':
        lowcnt+=1
    if ch>='0' and ch<='9':
        digcnt+=1
print("Number of Words:",len(wordcnt))
print("Number of Uppercase letters:",upcnt)
print("Number of Lowercase letters:",lowcnt)
print("Number of Digits:",digcnt)