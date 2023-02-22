# 백준 18352 특정도시찾기
import sys
from collections import deque
input = sys.stdin.readline # 입력속도를 빠르게

N, M, K, X = map(int, input().split()) # 노드의 수, 에지의 수, 목표거리, 시작점
A = [[] for _ in range(N + 1)] # 초기화
answer = [] # 값 담을 리스트
visited = [-1] * (N + 1) # 방문리스트 초기화

def BFS(v): # BFS 탐색 함수 구현
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i] == -1: # 미방문이면
                visited[i] = visited[now_Node] + 1
                queue.append(i)

# 두번째 줄 부터 에지 입력
for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

BFS(X) # 시작점부터 BFS시작

for i in range(N + 1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)