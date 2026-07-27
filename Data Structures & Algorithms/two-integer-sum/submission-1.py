class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = sorted((val, i) for i, val in enumerate(nums))
        left = 0
        right = len(nums) - 1
        res = indexed_nums[left][0] + indexed_nums[right][0]
        while res != target:
            if res > target:
                right -= 1
            elif res < target:
                left += 1
            res = indexed_nums[left][0] + indexed_nums[right][0]
        result = [indexed_nums[left][1], indexed_nums[right][1]]
        return sorted(result)