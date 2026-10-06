class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # [index, temperature]
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackInd = stack.pop()
                output[stackInd] = i - stackInd
            stack.append((t, i))
        return output
        