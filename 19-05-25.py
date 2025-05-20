'''ip:Given two sorted lists[2,4,5,8,9] and [3,5,6,9,11,12,13] merge to single list. op:[2,3,4,5,5,6,8,9,11,12,13]'''
a=[2,4,5,8,9]
b=[3,5,6,9,11,12,13]
c=[]
i=j=0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
while i<len(a):
    c.append(a[i])
    i+=1
while j<len(b):
    c.append(b[j])
    j+=1
print(c)

'''ip:[5,1,3,7,8,11,13,4].do the merge sort'''
def merge_sort(a):
    if len(a)<=1:
        return a
    mid = len(a)//2
    left= merge_sort(a[:mid])
    right= merge_sort(a[mid:])
    merge=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merge.append(left[i])
            i+=1
        else:
            merge.append(right[j])
            j+=1
    while i<len(left):
        merge.append(left[i])
        i+=1
    while j<len(right):
        merge.append(right[j])
        j+=1
    return merge
a=[5, 1, 3, 7, 8, 11, 13, 4]
print(merge_sort(a))


'''ip:[2,13,4,2,9,9,5,8,7,13,3],k=3 print kth largest element.'''
'''1.without duplicates  kth largest element'''
a=[2,13,4,2,9,9,5,8,7,13,3]
k=3
b=[0 for i in range(max(a)+1)]
print(b)
for i in a:
    b[i]=1
for i in range(len(b)-1,-1,-1):
    if b[i]==1:
        k=k-1
    if k==0:
        print(i)
        break
    
'''2.with duplicates kth largest element'''
a=[2,13,4,2,9,9,5,8,7,13,3]
k=3
b=[0 for i in range(max(a)+1)]
print(b)
for i in a:
    b[i]+=1
for i in range(len(b)-1,-1,-1):
    if b[i]!=1:
        k=k-b[i]
    if k<=0:
        print(i)
        break

'''print the element with highest frequency'''   
a=[3,6,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
d={}
k=3
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
m=0
for i in d:
    if d[i]>m:
        m=d[i]
        res=i
print(res)

'''kth largest element acc to freq'''
a=[3,6,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
d={}
k=3
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
m=max(d.values())
b=[0 for i in range(m+1)]
for i in d:
    b[d[i]] = max(b[d[i]], i)  
print(b[-k])

'''ip:[2,1,1,2,3,1,1] find the num freq is >(n/2) of the list.op:1'''
a = [2, 1, 1, 2, 3, 1, 1]
c=1
res=a[0]
for i in range(1,len(a)):
    if res==a[i]:
        c=c+1
    else:
        c=c-1
        if c==0:
            res=a[i]
            c=1
print(res)

'''ip:[2,4,3,1,4,2,3,4,5] x=4 if element found print the index of last occurence of array.if not found print -1'''
a= [2, 4, 3, 1, 4, 2, 3, 4, 5]
x=4
last_index=-1  
for i in range(len(a)):
    if a[i]==x:
        last_index=i
print(last_index)

'''ip:[2,3,5,6,7,7,8,9,10,10,10,13,15] search element 7 using binary search'''
a=[2,3,5,6,7,7,8,9,10,10,10,13,15]
k=7
def binarySearch(a,k,low,high):
    result=-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==k:
            result=mid         
            low=mid+1        
        elif k<a[mid]:
            high=mid-1
        else:
            low=mid+1
    return result
low=0
high=len(a)-1
result=binarySearch(a,k,low,high)
if result != -1:
    print('Element found at :',result)
else:
    print('Element not found:',result)
    
    
'''ip:[2,4,6,7,8,10,13,15] x=3,if x is found then print the index,if x is not found then print the index where we should insert'''
a=[2,4,6,7,8,10,13,15]
x=5
def searchInsert(a,x):
    low=0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid  
        elif x<a[mid]:
            high=mid-1
        else:
            low=mid+1
    return low  
index = searchInsert(a, x)
print("Index:", index)
