s, q = input().split()
s = list(s)
queries = [input().split() for _ in range(int(q))]

for query in queries:
    q, a, b = query
    if q == "1":
        a = int(a)-1
        b = int(b)-1
        tmp = s[a]
        s[a] = s[b]
        s[b] = tmp
        print("".join(s))
    else:
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        print("".join(s))
    