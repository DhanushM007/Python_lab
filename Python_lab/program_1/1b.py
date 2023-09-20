num=input("Enter a number to check palindrome or not:")
rev=num
if rev==rev[::-1]:
    print("Given number is a palindrome")
else:
    print("Given number is not a palindrome")
for i in range(10):
    if(rev.count(str(i))>0):
        print(i,"appears",rev.count(str(i)),"times")