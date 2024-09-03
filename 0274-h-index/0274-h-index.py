class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #citations[i] >= i + 1
        citations.sort(reverse = True)
        h = 0
        for i,t in enumerate(citations):
            if t >= i + 1:
                h = i + 1
            else:
                break
        return h



        