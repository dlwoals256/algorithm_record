input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
s = input_str
for query in queries:
    if query == 1:
        s = s[1:] + s[0]
        print(s)
    elif query == 2:
        s = s[-1] + s[:-1]
        print(s)
    else:
        s = s[::-1]
        print(s)