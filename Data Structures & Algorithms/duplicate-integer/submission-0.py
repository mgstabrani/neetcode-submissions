class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occ = {}
        for num in nums:
            occ[num] = True
        return len(occ.items()) != len(nums)
        