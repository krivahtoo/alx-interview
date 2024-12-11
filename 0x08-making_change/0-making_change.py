#!/usr/bin/python3
"""
Interview 0x08. Making Change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target total amount.

    Returns:
        The fewest number of coins needed to meet the total,
        or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Initialize an array for the minimum number of coins needed
    # for each amount up to `total`
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make 0

    # Populate the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the total is still float('inf'), it means it's
    # not possible to form the total
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
