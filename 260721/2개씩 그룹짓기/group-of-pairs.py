n = int(input())
nums = list(map(int, input().split()))

nums.sort()

left = 0
right = len(nums) - 1
max_sum = 0

while left < right:
    pair_sum = nums[left] + nums[right]
    if pair_sum > max_sum:
        max_sum = pair_sum

    left += 1
    right -= 1

print(max_sum)