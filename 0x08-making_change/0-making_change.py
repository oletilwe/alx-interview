#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make a given total.

    Parameters:
    coins (list): A list of the values of the available coins.
    total (int): The total value for which we need to make change.

    Returns:
    int: The minimum number of coins needed to make the total, or -1 if it is not possible.
    """
    # If the total is less than or equal to 0, no coins are needed.
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each value from 0 to total.
    # We use float('inf') to indicate that the value is initially considered unreachable.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0.

    # Iterate over each value from 1 to total.
    for i in range(1, total + 1):
        # For each coin in the list of coins,
        for coin in coins:
            # Check if the coin can be used to make the current total i.
            if coin <= i:
                # Update the dp array with the minimum number of coins needed to make the total i.
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the value at dp[total] is still float('inf'), it means the total cannot be made with the given coins.
    return dp[total] if dp[total] != float('inf') else -1
