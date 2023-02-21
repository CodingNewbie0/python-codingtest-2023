# 백준 1920 원하는 정수찾기
N = int(input()) # 데이터 개수, 5
A = list(map(int, input().split())) # 4 1 5 2 3
A.sort() # 정렬
M = int(input()) # 찾아야 할 숫자 개수, 4
target_list = list(map(int, input().split())) # 1 3 7 9 5

for i in range(M):
    find = False
    target = target_list[i]
    # 이진 탐색 시작
    start = 0
    end = len(A) - 1
    while start <= end:
        midi = (start + end) // 2 # 중앙 인덱스
        midv = A[midi] # 중앙에 있는 값
        if midv > target: # 오른쪽 날림
            end = midi - 1
        elif midv < target: # 왼쪽 날림
            start = midi + 1
        else: # 값 찾음
            find = True
            break
        
    if find:
        print(1)
    else:
        print(0)