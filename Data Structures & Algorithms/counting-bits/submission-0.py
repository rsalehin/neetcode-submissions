class Solution:
    def countBits(self, n: int) -> List[int]:
        res_list = []
        list1 = [i for i in range(n+1)]

        def num_one_bit(val):
            res = 0
            for i in range(32):
                if val & (1 << i):
                    res+=1
            return res

        for num in list1:
            res_list.append(num_one_bit(num))
        return res_list

            

        