class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        for a in range(len(nums)):
            flag=True
            for b in nums[a+1:]+nums[:a+1]:
                if b > nums[a]:
                    ans.append(b)
                    flag=False
                    
                    break
            
            if flag:ans.append(-1)
        return ans
                        
            
            
