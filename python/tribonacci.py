class Solution(object):
    def tribonacci(self, n):
        if n==0:
            return 0
        if n<=2:
            return 1
        #temp=[0,1,1]
        # for i in range(2,n):
        #     t_next=sum(temp)
        #     temp[0]=temp[1]
        #     temp[1]=temp[2]
        #     temp[2]=t_next
        # return temp[2]
        temp=[0,1,1]
        i=3
        while (i<n+1):
            result=temp[-1]+temp[-2]+temp[-3]
            temp.append(result)
            i+=1
        return temp[n]   
    
s=Solution()
inp=int(input('n = '))
print(s.tribonacci(inp))

