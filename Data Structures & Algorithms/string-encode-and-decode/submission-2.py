class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            length = len(s)
            result += str(length)
            result += '#'
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        n = len(s)

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            result.append(s[start:end])
            i = end
        return result
            
