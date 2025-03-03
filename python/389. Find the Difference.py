class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

S=Solution()
s = input()
t = input()
the_differance = S.findTheDifference(s,t)
print("output : ",the_differance)