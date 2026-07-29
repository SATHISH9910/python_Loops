def maxProfit(prices):

    minimum = prices[0]
    profit = 0

    for price in prices:

        if price < minimum:
            minimum = price

        else:
            if price - minimum > profit:
                profit = price - minimum

    return profit


prices = [7, 1, 5, 3, 6, 4]

print(maxProfit(prices))