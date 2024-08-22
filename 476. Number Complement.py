class Solution:
    def findComplement(self, num: int) -> int:
        num=bin(num)[2::]
        num=num.replace("0","*")
        num=num.replace("1","0").replace("*","1")
        return int(num,2)
        
        
