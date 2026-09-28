class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r >= l:
            c = l + ((r - l) // 2)
            if nums[c] == target:
                return c
            elif nums[c] > target:
                r = c - 1
            else:
                l = c + 1
        return -1
