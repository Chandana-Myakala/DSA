'''ip:"abcdecfbgce" find the longest non-repeating substring and print it'''
s="abcdecfbgce"
m=0
d={}
l=0
st=0
for r in range(len(s)):
    if s[r] not in d:
        d[s[r]]=r
    else:
        if d[s[r]]>=l:
            l=d[s[r]]+1
        d[s[r]]=r
    if(r-l+1>m):
        m=r-l+1
        st=l
print(m)
print(s[st:st+m])


'''ip:"abcedacefaebghd"
m='c',n='d' find the longest non-repeating substring with m and n in it'''
s="abcedachfaebghd"
m='c'
n='d'
ma=0              
st=0           
d={}     
l = 0               
for r in range(len(s)):
    if s[r] not in d:
        d[s[r]]=r
    else:
        if d[s[r]]>=l:
            l=d[s[r]]+1
    d[s[r]]=r  
    if m in d and n in d and d[m]>=l and d[n]>=l:
        if (r-l+1)>ma:
            ma=r-l+1
            st=l
print(ma)
print(s[st:st+ma])


'''ip:[4,2,7,20,8,6,4,1],k=3 deck of cards you have to remove k cards from list,you have to remove either from top or bottom,
you should not remove from middle.print the maximum profit also print the cards'''
a=[4,3,2,5,6,1,12,3]
n=len(a)
k=4
sl=0
for i in range(k):
    sl=sl+a[i]
sr=0
m=sl
#print(sl)
for i in range(k-1,-1,-1):
    sl=sl-a[i]
    sr=sr+a[n-1]
    m=max(m,sl+sr)
    n=n-1
    #print(sl,sr)
print(m)

'''Maximum consecutive Ones-return the maximum number of consecutive 1's in the array if you can flip at most k 0's.'''
a=[1,1,1,0,0,0,1,1,1,1,0]
l=0
z=0
k=2
m=0
for r in range(len(a)):
    if a[r]==0:
        z=z+1
    if z>k:
        if a[l]==0:
            z=z-1
        l=l+1
    if z<=k:
        m=max(m,r-l+1)
print(m)

'''fruits into baskets-904 leetcode'''
a=[1,2,3,2,2]
l=0
d={}
m=0
for r in range(len(a)):
    if a[r] not in d:
        d[a[r]]=1
    else:
        d[a[r]]+=1
    if(len(d)>2):
        d[a[l]]-=1
        if(d[a[l]]==0):
            del d[a[l]]
        l=l+1
    if(len(d)<=2):
        m=max(m,r-l+1)
print(m)


'''ip:[9:00,945,1110,1230,1235,1245,1340,1700]-starting tym
      [9:30,1130,1120,1245,1250,1415,1400,1730]-end tym patients are booked appointments,
      print maximum no of doctors require to treat everyone.O/P:3'''
st=[900,945,1110,1230,1235,1245,1340,1700]
et=[930,1130,1120,1245,1250,1415,1400,1730]
i=0
j=1
c=1
while i<len(st) and j<len(et):
    if et[i]>st[j]:
        c+=1
    else:
        i+=1
    j+=1
print(c)/