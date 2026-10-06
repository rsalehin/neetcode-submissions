class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        setT, setS = {}, {}

        for i in range(len(s)):
            setT[t[i]] = 1+ setT.get(t[i], 0)
            setS[s[i]] = 1 + setS.get(s[i], 0)
        return setT == setS
        