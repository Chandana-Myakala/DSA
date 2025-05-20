'''ip:38 find out the floor value of a number,use function not square root'''
def floor_sqrt(n):
    if n==0 or n==1:
        return n
    start=1
    end=n
    ans=0
    while start<=end:
        mid=(start+end)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            ans=mid
            start=mid+1
        else:
            end=mid-1
    return ans
print(floor_sqrt(38))

'''you are given a rotated array/partial array you did k=4 rotations [15,18,20,22,2,5,8,10,12,13] find out the
index of first element in the original array.'''
def find_rotation_index(a):
    start=0
    end=len(a)-1
    while start<end:
        mid=(start+end)//2
        if a[mid]>a[end]:
            start=mid+1
        else:
            end=mid
    return start  
a=[15,18,20,22,2,5,8,10,12,13]
print(find_rotation_index(a))


'''ip:[2,3,4,6,3,2,1,5,8,10,1,4,2] print the peak element in the array.peak=6,10,4(previous element of peak and next element of peak should
be prev>next).'''
a=[2,3,4,6,3,2,1,5,8,10,1,4,2]
l=0
r=len(a)-1
while l<r:
    m=(l+r)//2
    if (m==0 or a[m]>a[m-1] and  m==len(a) or a[m]>a[m+1] or a[m]>a[m+1]):
        print(a[m])
        break
    if(a[m+1]>a[m]):
        l=m+1
    else:
        r=m-1