class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        for i in range(len(strs)):
            sortedStr = "".join(sorted(list(strs[i])))
            if sortedStr not in sortedMap.keys():
                sortedMap[sortedStr] = [strs[i]]
            else:
                sortedMap[sortedStr].append(strs[i])
        return list(sortedMap.values())
