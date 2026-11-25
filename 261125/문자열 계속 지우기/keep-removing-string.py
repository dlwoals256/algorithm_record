A = input()
B = input()

# Please write your code here.

while B in A:
    A = A.replace(B, "", 1)
print(A)