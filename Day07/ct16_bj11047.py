# 백준 11047 동전 0
N, K = map(int, input().split())
A= [0] * N

for i in range(N):
    A[i] = int(input())

A.sort()

count = 0

for i in range(N - 1, -1, -1): # 역순으로
    if A[i] <= K: # 현재 동전의 가치가 K보다 작거나 같으면 구성에 추가
        count += K // A[i]
        K = K % A[i] # K를 현재 동전을 사용하고 남은 금액으로 갱신

print(count)