def binarySearch(a,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if a[mid]==x:
            return mid
        elif a[mid]>x:
            binarySearch(a,low,mid-1,x)
        else:
            binarySearch(a,mid+1,high,x)
    return-1
a=list()
n=int(input("enter the number of elements you need to do:"))
for i in range(n):
    e=int(input("enter the elements:"))
    a.append(e)
print(a)
x=int(input("enter the elments you need to search:"))
found=binarySearch(a,0,len(a),x)
if found!=-1:
    print(result)
    print("Element id not found",found)
else:
    print("Element is found in yhe index:")
