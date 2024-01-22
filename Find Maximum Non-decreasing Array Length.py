class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        last_val = [0] * n
        sums = [0] * n
        f[0] = 1
        S = 0
        for j in range(n):
            sums[j] = S = S + nums[j]
            _, i = max(((f[i], i) for i in range(j) if last_val[i] <= sums[j] - sums[i]), default=(0, -1))
            if i == -1:
                f[j] = 1
                last_val[j] = sums[j]
            else:
                f[j] = f[i] + 1
                last_val[j] = sums[j] - sums[i]
        return f[n-1]