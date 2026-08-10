class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        freq = Counter(nums)
        for key, v in freq.items():
            bucket[v].append(key)

        # print(bucket)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for it in bucket[i]:
                res.append(it)
                # print(len(res), k)
                if len(res) == k:
                    return res
        return res
