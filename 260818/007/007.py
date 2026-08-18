secret_code, meeting_point, time = input().split()
time = int(time)

class Solution:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

solution = Solution(secret_code, meeting_point, time)

print("secret code :", solution.code)
print("meeting point :", solution.point)
print("time :", solution.time)