# 백준 1541 잃어버린 괄호
answer = 0
A = list(map(str, input().split('-'))) # 100-40+50+74-30+29-45+43+11

def mySum(i): # -로 나뉜 그룹들의 합을 구하는 함수
    sum = 0
    temp = str(i).split('+') # + 기준으로 수식 자름 '78+45'
    for k in temp:
        sum += int(k) # '78' rkxdms answkdufdlamfh ㅑㅜㅅ()
    return sum

for s in range(len(A)):
    temp = mySum(A[s])
    if s == 0:
        answer += temp # 가장 앞에 있는 값만 더하기
    else:
        answer -= temp # 뒷부분의 값은 합쳐서 빼기

print(answer) # -222