class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k=k%len(s)
        s2=s+s
        ans=""
        for a in range(len(s)):ans+=s2[a+k]
        return ans
            
        
