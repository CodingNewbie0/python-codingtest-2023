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
    - 코딩테스트 알고리즘
        - 백준
        - 프로그래머스

```python
# 백준 1253 좋다
import sys
input = sys.stdin.readline

N = int(input())
count = 0
A = list(map(int, input().split())) # 한줄에 입력을 다 받을때
A.sort(reverse=False) # 전체 정렬(리버스 트루하면 역순정렬)

for k in range(N):
    find = A[k]
    i =  0; j = N - 1 # i는 리스트 첫번째, j는 리스트 마지막번째 위치
    while i < j: # 두 인덱스가 결국 만나면 while문을 종료
        if A[i] + A[j] == find: # 두 수의 합이 찾는 수랑 일치
            if i != k and j != k: # i와 j는 k와 같은 위치가 되면 안된다.
                count += 1
                break
            elif i == k: i += 1
            elif j == k: j -= 1
        elif A[i] + A[j] < find: # i를 증가시켜야 합의 수가 커짐
            i += 1
        elif A[i] + A[j] > find: # j를 감소시켜야 합의 수가 작아짐
            j -= 1

print(count)
```

