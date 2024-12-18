class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer = []
        price_len = len(prices)
        discount_to_apply = 0
        if price_len == 1:
            return prices
        for index, item in enumerate(prices):
            if index == price_len - 1:
                answer.append(item)
            else:
                for i in range(index + 1, price_len):
                    if item >= prices[i]:
                        discount_to_apply = prices[i]
                    if discount_to_apply > 0:
                        break
                answer.append(item - discount_to_apply)
            discount_to_apply = 0
        return answer


teste = Solution()
print(teste.finalPrices(prices=[10, 1, 1, 6]))
