#https://www.acmicpc.net/problem/2750
#시간복잡도는 O(N^2) 
#단 이미 정렬된 경우 best case는 O(N)

import sys

N = int(sys.stdin.readline())
M = []

for _ in range(N):
    M.append(int(sys.stdin.readline()))
    
for i in range(1,len(M)):
    for j in range(i,0,-1):
        if M[j-1] > M[j]:
            M[j-1],M[j] = M[j],M[j-1]

for i in M:
    print(i)