#bfs
from collections import deque
def bfs_simple(x, p, q):
    queue = deque()
    queue.append((x, [x]))    
    total_ways = 0
    shortest_path = None
    while queue:
        current, path = queue.popleft()
        if current == 1:
            total_ways += 1
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = path
            continue
        if current < 1:
            continue
        queue.append((current - p, path + [current - p]))
        queue.append((current - q, path + [current - q]))
    return total_ways, shortest_path
start = 20
p = 3
q = 5
ways, shortest = bfs_simple(start, p, q)
if ways > 0:
    print(f"Total ways to reach 1: {ways}")
    print(f"Shortest way ({len(shortest) - 1} steps): {' -> '.join(map(str, shortest))}")
else:
    print("Not possible to reach 1.")
    
    
    
#even_sum recursion  
def even_sum(x,i):
    if i==len(x):
        return 0
    if x[i] % 2 == 0:  
        return x[i] + even_sum(x, i + 1)
    else:
        return even_sum(x,i +1)   
a=[2,5,6,7,2,1,4,3,6]
print(even_sum(a,0))

#factorial_recursion
def qwer(x):
    if(x==1):
        return 1
    return x*qwer(x-1)
b=qwer(5)
print(b)

#prime count recursion
def is_prime(n, i=2):
    if n<2:
        return False
   
    if i>n// 2:
        return True
    if n % i == 0:
        return False
    
    return is_prime(n, i + 1)

def count_primes(lst, s=0):
    if s == len(lst):
        return 0
    if is_prime(lst[s]):
        return 1 + count_primes(lst, s + 1)
    else:
        return count_primes(lst, s+ 1)

n = [13, 17, 21, 23, 27, 7, 29]
print(count_primes(n))

#reverse_recursion
def reverse_num(n, re=0):
    if n == 0:
        return re
    else:
        b = n % 10
        re = re * 10 + b
        return reverse_num(n // 10,re)

n = 54227
print(reverse_num(n))

def reach_one_paths(x, n, m, path=[], all_paths=[]):
    if x == 1:
        all_paths.append(path + [1])
        return
    if x < 1:
        return
   
    reach_one_paths(x - n, n, m, path + [x], all_paths)
    
    reach_one_paths(x - m, n, m, path + [x], all_paths)


#shortestpath recursion
def main():
    x = 20
    n = 3
    m = 5
    all_paths = []

    reach_one_paths(x, n, m, [], all_paths)

    if all_paths:
        print(f"Total ways to reach 1 from {x} using {n} or {m}: {len(all_paths)}\n")

        
        for i, path in enumerate(all_paths, 1):
            print(f"Way {i}: {' -> '.join(map(str, path))}")

        
        shortest_path = min(all_paths, key=len)
        print("\nShortest path:")
        print(" -> ".join(map(str, shortest_path)))
    else:
        print("No way to reach 1 using these steps.")

main()









    
    
    
