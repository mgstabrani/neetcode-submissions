class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        allProducts = 1
        totalZero = 0
        for num in nums:
            allProducts *= num
            if num == 0:
                totalZero += 1
        if totalZero > 1:
            return [0 for i in range(len(nums))]
        elif totalZero == 1:
            allProducts = 1
            for num in nums:
                if num != 0:
                    allProducts *= num
            output = []
            for i in range(len(nums)):
                if nums[i] == 0:
                    output.append(allProducts)
                else:
                    output.append(0)
            return output
        output = []
        for i in range(len(nums)):
            output.append(int(allProducts/nums[i]))
        return output