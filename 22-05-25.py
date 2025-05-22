'''ip:[2,2,1,0,1,3,0] not possible
ip:[2,3,1,0,1,3,0] possible
ip:[2,3,1,0,1,3,1] possible here first car has 0 petrol it started from starting index it will get 2l petrol ,then after he travel  every next point 1l decrease
if he want to exchange he can ,if not he can be with same petrol.finally if he possible to come out of the array or not.'''
def can_exit(a):
    petrol=a[0]  
    n=len(a)
    for i in range(1,n):
        petrol-=1   
        if petrol<0:
            return 'not possible'
        if a[i]>petrol:
            petrol=a[i]
    return 'possible'
#a=[2,2,1,0,1,3,0]
#a=[2,3,1,0,1,3,0]
a=[2,3,1,0,1,3,1]
print(can_exit(a))

'''ip:[5,10,5,10,10,20]=false
ip:[5,5,10,20]=true
ip:[5,5,5,20,10]=false 5rs for each lemonade change'''
def can_sell(bills):
    five=0
    ten=0
    for bill in bills:
        if bill==5:
            five+=1
        elif bill==10:
            if five==0:
                return 'not possible'
            five-=1
            ten+=1
        elif bill==20:
            if ten>0 and five>0:
                ten-=1
                five-=1
            elif five>=3:
                five-=3
            else:
                return 'not possible'
    return 'possible'
bills=[5,10,5,10,10,20]
#bills=[5,5,10,20]
#bills=[5,5,5,20,10]
print(can_sell(bills))

'''ip:[4,3,7,1,6,2].find out the minimum waiting time'''
a=[4,3,7,1,6,2]
a.sort()
s=0
total=0
for i in range(len(a)-1):
    s+=a[i]
    total+=s
    #print(s)
print(total/(len(a)-1))


'''ppl=[1,6,2,3,4,5] and bundle=[4,2,3,1,1,2] print the maximum no of people satisfy by the bundle.the first person will take 4l and next 6l person don't
that much money in the bundle'''
def max_satisfied(ppl,b):
    ppl.sort()
    b.sort()
    i=j=c=0
    while i<len(ppl) and j<len(b):
        if b[j]>=ppl[i]:
            c+=1
            i+=1
            j+=1
        else:
            j+=1
    return c
ppl=[1,6,2,3,4,5]
b=[4,2,3,1,1,2]
print(max_satisfied(ppl,b))

'''minimum no of jumps'''
a= [2, 3, 1, 1, 4]
l=0
r=0
jump=0
while r<len(a)-1:
    m=0
    for i in range(l,r+1):
        if i+a[i]>m:
            m=i+a[i]
    l=r+1
    r=m
    jump+=1
print(jump)