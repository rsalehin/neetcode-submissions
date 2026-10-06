class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            '1': '',         # Often reserved for voicemail or special characters
            '2': 'abc',      # 2 maps to 'a', 'b', 'c'
            '3': 'def',      # 3 maps to 'd', 'e', 'f'
            '4': 'ghi',      # 4 maps to 'g', 'h', 'i'
            '5': 'jkl',      # 5 maps to 'j', 'k', 'l'
            '6': 'mno',      # 6 maps to 'm', 'n', 'o'
            '7': 'pqrs',     # 7 maps to 'p', 'q', 'r', 's'
            '8': 'tuv',      # 8 maps to 't', 'u', 'v'
            '9': 'wxyz',     # 9 maps to 'w', 'x', 'y', 'z'
            '0': ' '         # 0 maps to a space (usually)
            }
        result = []
        if not digits:  # Edge case for empty string
            return []
        def dfs(i, path):
            if i == len(digits):
                result.append("".join(path))
                return
            current_number = digits[i]
            for letter in keyboard[current_number]:
                path.append(letter)
                dfs(i + 1, path)
                path.pop()
        dfs(0, [])
        return result
        


        