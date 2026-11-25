n = int(input())
strs = input().replace(" ", "")

for i in range(0, len(strs), 5):
    print(strs[i:i+5])