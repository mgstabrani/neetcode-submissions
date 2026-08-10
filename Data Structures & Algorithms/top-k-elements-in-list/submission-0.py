class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq.keys():
                freq[num] = 1
            else:
                freq[num] += 1
        
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        ans = []
        for key, _ in freq.items():
            if k == 0:
                break
            ans.append(key)
            k -= 1
        return ans