class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_hash = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            anagram_hash[tuple(count)].append(word)
        return list(anagram_hash.values())

        