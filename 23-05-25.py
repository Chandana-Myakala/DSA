'''ip:[0,3,8,1,5,7,9]-starting tym
ip2:[5,6,10,2,6,9,11]-ending tym,the max no of meeting able to conduct-3 output.condition:after one meeting the end time should not be same
with next meeting starting tym'''
m1=[0,3,8,1,5,7,9]
m2=[5,7,10,2,6,9,11]
meetings=list(zip(m1, m2))
def get_end(meeting):
    return meeting[1]
meetings.sort(key=get_end)
print(meetings)
count=0
last_end=-1
for s,e in meetings:
    if s>last_end:  
        count+=1
        last_end=e
print(count)

'''ip:"hippopotamus" reverse the string without changing the vowels position.output:"simtopopapuh"'''
def rev_string(s):
    v=set("aeiouAEIOU")
    c=[ch for ch in s if ch not in v][::-1]
    res=[]
    i=0  
    for ch in s:
        if ch in v:
            res.append(ch)
        else:
            res.append(c[i])
            i+=1
    return ''.join(res)
s= "hippopotamus"
print(rev_string(s))

'''two-pointer approach'''
def rev_string(s):
    vowels=set("aeiouAEIOU")
    b=list(s)
    i=0
    j=len(s)-1
    while i<j:
        if b[i] in vowels:
            i+=1
        elif b[j] in vowels:
            j-=1
        else:
            b[i],b[j]=b[j],b[i]
            i+=1
            j-=1
    return ''.join(b)
s= "hippopotamus"
print(rev_string(s))


'''ip:[2,1,6,4,2,3,1,1,4,2,6,7,3],k=5,pick the contiguous(5in row) books and print the maximum discount of the books.'''
def max_discount(a,k):
    n=len(a)
    if n<k:
        return sum(a)  
    cur_sum=0
    for i in range(k):
        cur_sum+=a[i]
    max_sum=cur_sum
    for i in range(k,n):
        cur_sum+=a[i]-a[i-k]
        if cur_sum>max_sum:
            max_sum=cur_sum
    return max_sum
a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=5
print(max_discount(a,k))


'''ip:[2,1,6,4,2,3,1,1,4,2,6,7,3] print len of longest subarray where sum<=k'''
def longest_subarray(a,k):
    n=len(a)
    i=0
    cur_sum=0
    max_len=0
    for j in range(n):
        cur_sum+=a[j]
        if cur_sum<=k:
            max_len=max(max_len,j-i+1)
        else:
            cur_sum-=a[i]
            i+=1
    return max_len
a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=6
print(longest_subarray(a,k))


'''ip:"ababba" ,length of longest palindrome substring.O/p: 4'''
s="ababba"
m=0
l=0
st=0
c=0
for i in range(len(s)):
    #odd length
    l=i
    r=i
    while l>=0 and r<len(s) and s[l]==s[r]:
        if(r-l+1>m):
            m=r-l+1
            st=l
        c+=1
        l=l-1
        r=r+1
    #even length
    l=i
    r=i+1
    while l>0 and r<len(s) and s[l]==s[r]:
        if(r-l+1>m):
            m=r-l+1
            st=l
        c+=1
        l=l-1
        r=r+1
print(m)
print(s[st:st+m],c)
 

'''ip:"abcdaecdb" length of longest substring without repeating characters'''
s="abcdecfbgce"
m=0
d={}
l=0
for r in range(len(s)):
    if s[r] in d and d[s[r]]>l:
        l=d[s[r]]+1
    d[s[r]]=r
    m=max(m,r-l+1)
print(m)

