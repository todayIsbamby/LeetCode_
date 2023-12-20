class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        min_price = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if i != j:
                    min_price.append((sum([prices[i], prices[j]])))
        min_price.sort()
        price_result = min_price[0]
        if price_result <= money:
            left_over = money - price_result
            return left_over
        else:
            return money


s = Solution()
inp1 = list(map(int, input("Enter Input : ").split(",")))
inp2 = int(input("Enter money : "))
print(s.buyChoco(inp1, inp2))
