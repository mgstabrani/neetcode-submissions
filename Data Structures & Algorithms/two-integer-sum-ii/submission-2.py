class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            if numbers[i] not in hashmap.keys():
                hashmap[target - numbers[i]] = i+1
            else:
                return [hashmap[numbers[i]], i+1]

        