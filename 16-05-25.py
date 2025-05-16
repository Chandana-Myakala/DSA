#greedy problem-profit
a = [13,14,2,5,8,1,4]
b=a[0]
max_profit=0
for i in a:
    if i<b:
        b=i
    profit=i-b
    if profit>max_profit:
        max_profit=profit
print(max_profit)


#sum of matrix and list acc to index.
a = [
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]
l=[8,7,6,5,2]
for i in range(len(a)):
    sum=0
    for j in range(len(a[0])):
        if a[i][j]==1:
            sum+=l[j]
    print(sum)
            

#finding paths-rat in maze
def rat_path(a,i=0,j=0,n=5,c=[0]):
    if i>=n or j>=n or a[i][j] == 0:
        return
    if i==n-1 and j==n-1 and a[i][j]==1:
        c[0]+=1
        return 1
    rat_path(a,i,j+1,n,c)
    rat_path(a,i+1,j,n,c)
a = [
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1]
]
count=[0]
rat_path(a,0,0,len(a),count)
print("Number of paths:", count[0])



#distinct island-1's are land and 0's are water find islands.
def land(a,i,j,n):
    if i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2:
        return 0
    if a[i][j]==1:
        a[i][j]=2
    land(a,i-1,j,n)
    land(a,i,j-1,n)
    land(a,i+1,j,n)
    land(a,i,j+1,n)
a = [
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]
n=5
c=0
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            land(a,i,j,n)
            c=c+1            
print(c)


#In given matrix 1's are trees and 0's are bareland in 3row and 6 col tree burnt it can go top,bottom,left,right.how many trees are not burnt.
def burn(a,i,j,n):
    if i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2:
        return 0
    if a[i][j]==1:
        a[i][j]=2
    burn(a,i-1,j,n)
    burn(a,i,j-1,n)
    burn(a,i+1,j,n)
    burn(a,i,j+1,n)
a = [[1,0,0,1,1,1],
     [1,1,1,0,0,0],
     [0,0,1,1,1,1],
     [1,1,1,0,0,0],
     [0,0,0,0,0,1],
     [1,0,0,1,0,0]]
n=6
unburn=0
i=3
j=6
burn(a,i-1,j-1,n)
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            unburn=unburn+1            
print(unburn)


#given 5rowcol box.In that frog is at pos 2,3 and frog cant jump to[(2,1),(4,1),(5,2),(3,5)].Frog can go right and bottom.How many paths frog can go last box.
def frog(n,i,j,blocked):
    if i>=n or j>=n or (i-1,j-1) in blocked:
        return 0
    if i==n-1 and j==n-1:
        return 1
    return frog(n,i+1,j,blocked) + frog(n,i,j+1,blocked)
n=5
i,j=(2,3)
blocked=[(2,1),(4,1),(5,2),(3,5)]
print(frog(n,i-1,j-1,blocked))


#given ip='' print from 0 to '' binary numbers.
import math
def binary(a,n,s=''):
    if a==-1:
        return a
    if len(s)==n:
        print(s)
        a=a-1
        return a
    a=binary(a,n,s+'0')
    a=binary(a,n,s+'1')
    return a
a=int(input())
n=int(math.log(a,2))+1
binary(a,n)

#if ip=3 ((())),()()(),(())(),()(())....
def brackets(n,open=0,close=0,cur=""):
    if len(cur)==2*n:
        print(cur)
        return
    if open < n:
        brackets(n, open + 1, close, cur + "(")
    if close < open:
        brackets(n, open, close + 1, cur + ")")
n=3
brackets(n)