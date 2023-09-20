print("enter 3 test marks:")
test1=int(input())
test2=int(input())
test3=int(input())
if test1 < test2 and test1 < test3:
    avg=(test2+test3)/2
elif test2 < test3 and test2 < test1 :
    avg=(test3+test1)/2
else:
    avg=(test1+test2)/2
print("Average of Two best marks out of Three test's marks:",avg)