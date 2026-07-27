class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        occ_s = {}
        for _s in s:
            if _s not in occ_s.keys():
                occ_s[_s] = 1
            else:
                occ_s[_s] += 1
        
        occ_t = {}
        for _t in t:
            if _t not in occ_t.keys():
                occ_t[_t] = 1
            else:
                occ_t[_t] += 1
        
        for key, val in occ_s.items():
            if key not in occ_t.keys():
                return False
            else:
                if val != occ_t[key]:
                    return False
        return True

        
        