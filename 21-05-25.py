'''Searching an element from a matrix'''
a=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target=5
found=False
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==target:
            print(f"Element found at position:({i},{j})")
            found=True
            break
    if found:
        break
if not found:
    print("Element not found.")
    
'''using binary search to search an element in matrix''' 
a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,22,25],
    [28,30,33,37]
]
target=12
rows=len(a)
cols=len(a[0])
l=0
r=rows*cols-1
found=False
while l<=r:
    mid=(l+r)//2
    row=mid//cols
    col=mid%cols
    if a[row][col]==target:
        print("Element found")
        found=True
        break
    elif a[row][col]<target:
        l=mid+1
    else:
        r=mid-1
if not found:
    print("Element not found.")

'''rectangular matrix also same'''
a = [
    [2,5,8,10],
    [13,15,17,22],
    [23,26,28,33]
]
target=8
rows=len(a)
cols=len(a[0])
l=0
r=rows*cols-1
found=False
while l<=r:
    mid=(l+r)//2
    row=mid//cols
    col=mid%cols
    if a[row][col]==target:
        print("Element found")
        found=True
        break
    elif a[row][col]<target:
        l=mid+1
    else:
        r=mid-1
if not found:
    print("Element not found.")
    
'''given array of weights in a ship and capacity how many days it can travel w.r.to capacity'''
a=[1,2,3,4,5,6,7,8,9,10]
c=12
d=1
s=0
if c<max(a):
    print("Not possible")
else:
    for i in range(1,len(a)):
        if s+a[i]>c:
            d+=1
            s=0
        s+=a[i]
    print(d)
    
'''given an row and col increasing matrix'''
a=[
    [3,4,6,8],
    [5,7,9,10],
    [8,12,13,15],
    [20,23,26,28],
    [30,36,40,45]
    ]
k=23
row=len(a)
col=len(a[0])
r=0
c=col-1
while r<row and c>=0:
    if a[r][c]==k:
        print("found")
        break
    elif a[r][c]>k:
        c-=1
    elif a[r][c]<k:
        r+=1
else:
    print("not found")
    
    
'''2sum in two pionter'''
a=[2,7,11,15]
k=22
f=1
for i in range(len(a)):
    for j in range(len(a)-1,i,-1):
        if a[i]+a[j]==k:
            print(i,j)
            f=0
            break
if f==1:
    print('no')
'''another approach'''
a=[2,7,11,15]
target=9
i=0
j=len(a)-1
while i<j:
    if a[i]+a[j]==target:
        print(i,j)
        break
    elif a[i]+a[j]>target:
        j-=1
    else:
        i+=1
else:
    print("no")