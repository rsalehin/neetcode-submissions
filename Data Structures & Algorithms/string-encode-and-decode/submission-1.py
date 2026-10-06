class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_parts = []
        for s in strs:
            length = len(s)
            encoded_parts.append(f"{length}#{s}")
        
        return "".join(encoded_parts)

    def decode(self, s: str) -> List[str]:
        decoded_parts = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= '#':
                j+=1
            length = int(s[i:j])
            start = j + 1
            end = start + length 
            original_str = s[start: end]
            decoded_parts.append(original_str)
            i = end
        return decoded_parts

