class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq.keys():
                freq[num] = 1
            else:
                freq[num] += 1
        
        group_freq = [[] for i in range(len(nums))]
        for key, val in freq.items():
            group_freq[val-1].append(key)

        ans = []
        for i in range(len(group_freq)-1, -1, -1):
            for num in group_freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans