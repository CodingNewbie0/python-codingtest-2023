# 백준 1717 집합 표현하기
# Union-Find 문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split()) # 원소 개수, 질의 개수
parent = [0] * (N + 1)

def find(a): # find 연산
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 재귀호출 -> 경로압축
        return parent[a]

def union(a, b): # union 연산 대표 노드끼리 합치기
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b): # 두 원소가 같은 집합에 속해 있는지 확인하는 함수
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else: return False

for i in range(0, N + 1):
    parent[i] = i # 1,1 2,2 3,3 4,4 5,5 6,6 7,7

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print('YES')
        else:
            print('NO')
