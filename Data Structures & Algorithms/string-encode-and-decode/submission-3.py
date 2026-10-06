class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for word in strs:
            length = len(word)
            result += str(length)+'#'+word
        return result

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        result = []
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            word = s[start: end]
            result.append(word)
            i = end
        return result

