class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime  = sorted(processorTime)
        tasks  =  sorted(tasks,reverse=True)
        total =0
        j=0
        max_ =0
        for i in range(len(processorTime)):
            mx  =  max(tasks[j:j+4])

            max_ =  max(max_,mx+processorTime[i])
            j+=4

        

        return max_




