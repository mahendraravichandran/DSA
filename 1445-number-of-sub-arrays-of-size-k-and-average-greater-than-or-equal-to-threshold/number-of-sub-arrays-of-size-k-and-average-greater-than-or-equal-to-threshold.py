class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur_sum = 0
        output = 0
        n = len(arr)
        for i in range(k):
            cur_sum += arr[i]
        average = round(cur_sum / k) 
        if average >= threshold:
            output += 1
        for i in range(k,n):
            cur_sum += arr[i]
            cur_sum -= arr[i - k]
            average = cur_sum / k 
            if average >= threshold:
                output += 1
        return output
