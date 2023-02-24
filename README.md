# python-codingtest-2023
파이썬 코딩테스트 리포지토리

# 1일차
1. 코딩테스트 소개
2. 코딩테스트 시작
    - [x] 자료구조 - 배열/리스트
    - [x] 구간합

# 2일차
파이썬 파일명에는 _만 사용할것
1. 코딩테스트 학습
    - [x] 구간합
    - [x] 자료구조
        - [x] pythonds 큐 확인

# 3일차
1. 코딩테스트 학습 
    - 자료구조
        - [x] 큐
        - [x] pythonds 큐 확인
        - [x] 이진 트리
            - 삭제는 연결리스트 삭제와 유사
        - [x] 그래프

# 4일차
1. 코딩테스트 학습
    - 자료구조
        - [x] 그래프 - DFS
        - [x] 재귀호출
        - [x] 정렬 소개

# 5일차
1. 코딩테스트 학습
    - 자료구조 / 알고리즘
        - [x] 정렬
![실행화면](https://github.com/CodingNewbie0/python-codingtest-2023/blob/main/Day05/%EA%B3%A0%EA%B8%89%EC%A0%95%EB%A0%AC.png?raw=true)
        - [x] 검색
        - [x] 다이나믹 프로그래밍 / 피보나치 실행시간 비교

# 6일차
1. 코딩테스트 학습
    - 코딩테스트 학습
        - 자료구조
            - [x] deque (덱)
        - 알고리즘
            - [x] 투포인터
            - [x] 슬라이딩윈도우
            - [x] 정렬

```python
# 백준 11003 최솟값찾기 1
from collections import deque
N, L = map(int, input().split()) # 12 3
mydeque = deque()
now = list(map(int, input().split())) # 1 5 2 3 6 2 3 7 3 5 2 6

# 새로운 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도를 줄임
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: # 인덱스가 현재값보다 크면
        mydeque.pop() # 빼버린다
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L: # 범위를 벗어난 값도 덱에서 제거
        mydeque.popleft() # 왼쪽에서 빼버린다
    print(mydeque[0][0], end=' ') # 무조건 최소값(min()과 동일) 1 1 1 2 2 2 2 2 3 3 2 2
```

# 7일차
1. 코딩테스트 학습
    - 자료구조
        - [x] 그래프
        - [x] PriorityQueue (우선순위 큐)
        - [x] heapq (힙큐) - 이진트리 구성으로 들어있는 값의 구조가 삭제시 변경될 수 있음.
    - 알고리즘
        - [x] 탐색 - DFS/BFS/이진함수
        - [ ] 그리디
        - [ ] 정수론

# 8일차
1. 코딩테스트 학습
    - 자료구조
    - 알고리즘
        - [ ] 정수론
        - [x] 그래프 활용

# 9일차
1. 코딩테스트 학습
    - 자료구조
    - 알고리즘
        - [x] 최단거리 알고리즘
        - [x] 최소신장트리 MST
        - [x] 트리순회

# 10일차
1. 코딩테스트 학습
    - 