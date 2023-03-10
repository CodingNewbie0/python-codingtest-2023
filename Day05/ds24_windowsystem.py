# C:\Windows\System32 파일 출력
# 내 컴퓨터 폴더 안에 어떤 파일이 있는지 알 수 있는 탐색기
import os

# print(dir(os))
def makeFileList(folder):
    fnameAry = []
    folderName = 'C:\Windows\System32'
    for _, _, fnames in os.walk(folderName):
        for fname in fnames:
            fnameAry.append(fname)

    return fnameAry

def insertionSort(ary):
    n = len(ary)
    for end in range(1, n): # 앞의 값 하나 빼고 끝까지 반복
        for cur in range(end, 0 , -1): # 반대로 돌면서
            if ary[cur-1] > ary[cur]: # 내림차순(역순정렬)
                ary[cur], ary[cur-1] = ary[cur], ary[cur-1] # 파이썬 swap(G.O.A.T)

    return ary

fileAry = makeFileList('C:/Program Files/Common Files')
fileAry = insertionSort(fileAry)
print('파일명 역순 --> ', fileAry)
