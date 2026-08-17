word1 = input()
word2 = input()

word1 = sorted(word1)
word2 = sorted(word2)

def check(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return "No"
    return "Yes"

if len(word1) != len(word2):
    print("No")
else:
    print(check(word1, word2))