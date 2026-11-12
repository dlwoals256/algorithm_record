A = input()

cnt = 1
res = A[0]

if len(A) == 1:
    print(2, A+"1", sep="\n")
else:
    for i in range(1, len(A)):
        if A[i] == A[i-1]:
            cnt += 1
        else:
            res += str(cnt)
            res += A[i]
            cnt = 1
        if i == len(A)-1:
            res += str(cnt)
    print(len(res), res, sep="\n")