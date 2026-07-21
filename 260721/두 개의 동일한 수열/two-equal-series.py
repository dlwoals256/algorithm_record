n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def solve(A:list[int], B:list[int]):
    for i in range(n):
        if A[i] != B[i]:
            return "No"
        
    return "Yes"

print(solve(A, B))