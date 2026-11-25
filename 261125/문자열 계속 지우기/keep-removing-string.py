A = input()
B = input()

# Please write your code here.

while True:
    if A.find(B) == -1:
        break
    t = A.find(B)
    A = list(A)
    for i in range(len(B)):
        A.pop(t)
    A = "".join(A)
print(A)