class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalSum = 1
        zeroCnt = 0
        for num in nums:
            if num == 0:
                zeroCnt += 1
                continue
            totalSum *= num
        
        for idx, num in enumerate(nums):
            if zeroCnt == 0:
                nums[idx] = totalSum//num
            else:
                if zeroCnt > 1:
                    nums[idx] = 0
                elif zeroCnt == 1:
                    if num == 0:
                        nums[idx] = totalSum
                    else:
                        nums[idx] = 0
        return nums