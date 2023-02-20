import sys
input = sys.stdin.readline
input = sys.stdout.write

N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N+1)

for i in range(1, N+1):
    A[i] = int(input())

A.sort()

for i in range(1, N+1):
    print(A[i])