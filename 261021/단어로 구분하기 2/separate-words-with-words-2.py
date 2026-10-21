strs = input().split()
for i in range(len(strs)):
    # 홀수 - 1(인덱스 변환) == 짝수
    if i % 2 == 0:
        print(strs[i])