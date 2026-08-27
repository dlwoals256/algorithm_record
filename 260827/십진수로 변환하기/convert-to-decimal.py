binary = input()

binary = list(binary)
num = 0

for d in binary:
    num = num * 2 + int(d)

print(num)
