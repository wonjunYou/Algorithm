#https://www.acmicpc.net/problem/2750

import sys

N = int(sys.stdin.readline())
M = []

for _ in range(N):
    M.append(int(sys.stdin.readline()))
 
for i in range(len(M)):
    for j in range(len(M)):
        if M[i] < M[j]:
            M[i],M[j] = M[j],M[i]

for i in M:
    print(i)

# Why unequality direction is right?
# 결국 기준이 오른쪽으로 옮겨지면서 좌측에 있던 큰 수가 오른쪽으로 이동하게 된다. 기준은 i, 바꿀 수는 j