#freq of countnumbers
def count_no(a,n):
    if not a:
        return 0
    return (1 if a[0]==n else 0) + count_no(a[1:],n)
a = [2, 4, 6, 3, 3, 2, 6, 1, 2, 3, 6, 6, 5]
x = int(input("Enter number to count: "))
print(count_no(a, x))


#freq to number
def count(x,a):
    if not a:
        return 0
    return (a[0] == x)+count(x,a[1:])
def print_freq(a,n,d=None):
    if d is None:
        d=[]
    if not a:
        return
    current = a[0]
    if current not in d:
        if count(current,a)==n:
            print(current)
        d.append(current)
    print_freq(a[1:], n, d)
a = [2,4,6,3,3,2,6,1,2,3,6,6,5]
n = int(input("Enter frequency: "))
print_freq(a,n)

#using dict
def value(x,f,d,i=0):
    if(i==len(x)):
        return "not found"
    if(d[x[i]]==f):
        return x[i]
    return value(x,f,d,i+1)
def freq_d(x,f,d={},i=0):
    if(i==len(x)):
        return value(list(d.keys()),f,d)
    if(x[i] not in d):
        d[x[i]]=1
    else:
        d[x[i]]+=1
    return freq_d(x,f,d,i+1)
a = [2,4,6,3,3,2,6,1,2,3,6,6,5]
f=int(input())
print(freq_d(a,f))


#subset
def subsets(lst):
    if not lst:
        return [[]]  
    rest=subsets(lst[1:])  
    return rest + [[lst[0]]+s for s in rest]  
a = [2,3,4]
result=subsets(a)
print("Subsets:")
for s in result:
    print(s)
    
#2
def subset(x,s=[],i=0):
    if(i==len(x)):
        print(s)
        return
    subset(x,s+[x[i]],i+1)
    subset(x,s,i+1)
a=[2,3,4]
subset(a)


#subset sum
def subset_exists(x, s=[], i=0, k=6):
    if i == len(x):
        return sum(s)==k
    if subset_exists(x, s+[x[i]],i+1,k):
        return True
    if subset_exists(x,s,i+1,k):
        return True
    return False
a = [2,4,6]
k = 5
print(subset_exists(a, k=k)) 

#another approach
def sub_set(x,k,i=0):
    if(k==0):
        return True
    if(i==0):
        return False
    if(x[i-1]>k):
        return sub_set(x,k,i-1) 
    return sub_set(x,k-x[i-1],i-1) or sub_set(x,k,i-1)
a = [1,4,5,8]
k = 9
print(sub_set(a, k,len(a)))


# subset sum
def sub_set(x,k,s=[],i=0):
    if(i==len(x)):
        if(k==0):
            print(s)  
        return 
    if(x[i]<=k):
        sub_set(x,k-x[i],s+[x[i]],i+1)
    sub_set(x,k,s,i+1)
a=[1,4,5,8]
k=9
sub_set(a,k)


#subset_coin change
def min_coins(coins, k):
    if k==0:
        return 0
    if k<0:
        return float('inf')
    min_count = float('inf')
    for coin in coins:
        count = min_coins(coins,k-coin)
        if count != float('inf'):
            min_count=min(min_count,1+count)
    return min_count
coins=[2,4,6,8]
k=13
res = min_coins(coins, k)
print(res if res != float('inf') else -1)

#another approach
def sub_set(x,k,s=0,i=0,m=999999):
    if(i==len(x)):
        if(k==0):
            if(s<m):
                m=s  
        return m
    if(x[i]<=k):
        m=sub_set(x,k-x[i],s+1,i+1,m)
    m=sub_set(x,k,s,i+1,m)
    return m
a=[2,3,5]
k=8
sub_set(a,k)


def leso(a):
    le,so=0,0
    for i in a:
        if i%2==0:
            if le==0 or i>le:
                le=i
        else:
            if so==0 or i<so:
                so=i
    return le,so
a=list(map(int,input().split()))
print(leso(a))

#largest_greedy
a=[4,5,6,2,13,7,1,8]
m=0
for i in a:
    if(i>m):
        m=i
print(i)

#second_largest
a = [4,5,6,2,13,7,1,8]
m=0
n=0
for i in a:
    if i>m:
        n=m
        m=i
    elif i>n and i!=m:
        n=i
print(i)

#largesteven_smallest odd
a = [4,5,6,2,13,7,1,8]
even=0
odd=999999
for i in a:
        if i%2==0 and i>even:
            even=i
        elif i%2!=0 and i<odd:
                odd=i
print("largest even:",even,"\nsmallest odd:",odd)