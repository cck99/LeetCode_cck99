class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x:x[0])

        merged_intervals= []
        currect_interval = intervals[0]

        for i in range(1,len(intervals)):
            if currect_interval[1] >= intervals[i][0]:
                currect_interval[1] = max(currect_interval[1],intervals[i][1])
            else:
                merged_intervals.append(currect_interval)
                currect_interval = intervals[i]

        merged_intervals.append(currect_interval)
        return merged_intervals