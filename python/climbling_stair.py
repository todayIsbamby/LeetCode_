class Solution(object):
    mem={}
    def climbStairs(self, n):
        
        if n in self.mem:
            return self.mem[n]
        if n==0 or n==1:
            return 1
        result=self.climbStairs(n-1)+self.climbStairs(n-2)
        self.mem[n]=result
        return result
        
inp=int(input("n = "))
S=Solution()
print(S.climbStairs(inp))
