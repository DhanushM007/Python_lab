def insertion_sort(L,n):
    for i in range(1,n):
        current=L[i]
        j=i-1
        while j>=0 and L[j]>current:
            L[j+1]=L[j]
            j-=1
        L[j+1]=current
L=[]  
print("Sorting using Insertion sort:")
n=int(input("enter the no of elements:"))
for i in range(n):
    elem=int(input())
    L.append(elem)
print("Before sorting:")
print(L)
insertion_sort(L,n)
print("After sorting:")
print(L)


def mergesort(lst):
    if len(lst)>1:
        mid=len(lst)//2
        lefthalf=lst[:mid]
        righthalf=lst[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k]=lefthalf[i]
                i+=1
                k+=1
            else:
                lst[k]=righthalf[j]
                j+=1
                k+=1
        while i<len(lefthalf):
            lst[k]=lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            lst[k]=righthalf[j]
            j+=1
            k+=1
mylist=[]  
print("Sorting using Merge sort:")
n=int(input("enter the no of elements:"))
for i in range(n):
    elem=int(input())
    mylist.append(elem)
print("Before sorting:")
print(mylist)
mergesort(mylist)
print("After sorting:")
print(mylist)
