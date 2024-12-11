#!/usr/bin/python3
"""
Interview 0x0A. Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of each game round and returns the name of the
    player with the most wins.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n values for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"),
             or None if the winner cannot be determined.
    """
    def sieve_of_eratosthenes(n):
        """Generates a list of primes up to n."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    # Validate inputs
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(primes[:n + 1])  # Count primes up to n
        # Determine winner of the round
        if primes_count % 2 == 1:  # Maria wins if count of primes is odd
            maria_wins += 1
        else:  # Ben wins if count of primes is even
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
