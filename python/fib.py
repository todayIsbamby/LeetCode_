class Solution(object):
    def fib(self, n):
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)
inp=int(input('n = '))
s=Solution()
print(s.fib(inp))