
#alone number
n = [2, 2, 4, 4, 6, 6, 7, 8, 8, 9, 9]

i = 0
while i < len(n):
    if i < len(n) - 1 and n[i] == n[i+1]:
        
        i += 2
    else:
        print(f'{n[i]} is alone')
        i += 1
        
#number of chars       
a="aaabbbcccvvhh"
c=1
s=' '
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        c=c+1
    else:
        s=s+a[i]+str(c)
        c=1
s=s+a[-1]+str(c)
print(s)

#&even
n=int(input())
if n&1==0:
    print('even no')
else:
    print('odd')
    
#without&%
n=int(input())
if n&1==0:
    print('even no')
else:
    print('odd')

#longest subsequence
arr=[2,3,4,6,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9]
def longest_consecutive_in_place(arr):
    maxi = 1
    curr= 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            curr += 1
            maxi= max(maxi, curr)
        else:
            curr= 1  
    return maxi
print(longest_consecutive_in_place(arr))

#powe2

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


num = int(input("Enter a number: "))


if is_power_of_two(num):
    print(f"{num} is a power of 2.")
else:
    print(f"{num} is NOT a power of 2.")

if(num//2!=num/2):
    print('power 2')
else:
    print(' not power 2')


#xor
#O(1) time comlexity
def xor_up_to_n(n):
    
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0
n = int(input())
print(f"XOR from 0 to {n} is: {xor_up_to_n(n)}")


#O(n) comlexity
s=0
for i in range(0,n+1):
    s=s^i
print(s)


#xor range
def xor_up_to_n(n):
    
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0



m = int(input())
n = int(input())
print((xor_up_to_n(n))^(xor_up_to_n(m-1)))
#print(f"XOR from {m} to {n} is: {xor_range(m, n)}")



    
    

       

        


