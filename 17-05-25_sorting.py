#bubble sort
a=[5,2,3,8,1,6,7]
#c=0
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        #c=c+1
        if a[i]>a[i+1]:
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a)
#print(c)
  
'''k value first,last elements remain same middle elements sort.'''
a=[5,2,3,8,1,6,7]
k=2
for j in range(len(a)-2*k-1):
    f=False
    for i in range(k,len(a)-k-1-j):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            f=True
    if f==False:
        break
print(a)


'''Kth largest element'''
a=[5,2,3,8,1,6,7]
k=2
for j in range(k):
    f=False
    for i in range(len(a)-1-j):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            f=True
    if f==False:
        break
print(a[-k])


'''ip=['c','e','a','b','f'] op;[a,b,c,e,f] using bubble sort'''
a=['d','c','e','a','b','f']
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        if a[i]>a[i+1]:
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a)

'''ip:[[2,3],[5,1],[1,4],[2,7],[1,3]] op:[[5,1],[2,3],[1,3],[1,4],[2,7]]'''
a=[[2, 3],[5, 1],[1, 4],[2, 7],[1, 3]]
for j in range(len(a)-1):
    f = False
    for i in range(len(a)-1-j):
        if a[i][1]>a[i+1][1]:  
            a[i],a[i+1] = a[i+1],a[i]
            f=True
    if not f:
        break
print(a)


'''ip:['zebra','car','apple','cat'] the output should be ['apple','car','cat','zebra'] by lexographical order-
if first letter of two strings same then do with second letter.if second letter also same then print in same order where input order given.'''
a=["zebra","cat","apples","car",'ball']
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        if a[i][0]>a[i+1][0]:
            f=True
            a[i],a[i+1]=a[i+1],a[i]
        elif a[i][0]==a[i+1][0] and a[i][1]>a[i+1][1]:
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a)


'''ip:[[4,13,12],[8,10,5],[7,9,20],[14,8,3]] op:[[14,8,3],[8,10,5],[7,9,20],[4,13,12]] sort acc to prime numbers in each row'''
def prime(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            return i
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
b=[]
for i in a:
    b.append(prime(i))
for i in range(len(b)-1):
    f=0
    for j in range(len(b)-1-i):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
            f=1
    if(f==0):
        break
print(a)


'''ip:"an apple a  day keeps doctor away".op:a an day away apple keeps doctor.Print acc to wordlength and as a sentence(spaces as sentence).'''
a="an apple a  day keeps doctor away"
l=a.split()
b=[]
for i in l:
    b.append(len(i))
for i in range(len(b)):
    f=False
    for j in range(len(b)-1-i):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
            l[j],l[j+1]=l[j+1],l[j]
            f=True
    if not f:
        break
print(" ".join(l))


'''ip:[7,2,6,3,6,7,7,2,2,2] and op:[3,6,6,7,7,7,2,2,2,2] print acc to frequency'''
a=[3,5,4,4,5,6,7,7,8,8,7,6,4,1,1,2,8,8]
d={}
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
print(d)
n=max(d.values())
b=[]
for i in range(n+1):
    b.append([])
print(b)
for i in d.items():
    b[i[1]].append(i[0])
print(b)
c=[]
for i in range(len(b)):
    for j in b[i]:
        c.extend([j]*i)
print(c)


'''using key -sort method'''
def qwe(x):
    return x[1]
a=[[2, 3],[5, 1],[1, 4],[2, 7],[1, 3]]
a.sort(key=qwe)
print(a)

def qwe(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            return i
    return 0
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3],[10]]
a.sort(key=qwe)
print(a)