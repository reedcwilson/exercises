import math
import heapq as h


# Arthur and Alena are playing a game with an array containing some integers.
# Arthur can take any integer and remove it from the array and he has to add
# half of that number (rounded up) back to the array.

# Alena allots Arthur a fixed number of moves and challenges him to minimize
# the sum of the final array.

# As an example of how moves work, start with the array nums = [10, 20, 7] and
# perform k = 4 moves. Pick any element to perform a move on, for example the
# 7. Perform the division: 7/2 = 3.5, and round up to 4. Replace the 7 with the
# new value 4. At this point, the array is nums = [10, 20, 4].  All 4 moves are
# performed as follows:

# Initial array                            [10, 20, 7]

# Pick    Pick/2    Rounded        Result
# 7       3.5       4              [10, 20, 4]
# 10      5         5              [5,  20, 4]
# 20      10        10             [5,  10, 4]
# 10      5         5              [5,  5,  4]

# The sum of the final array is 5 + 5 + 4 = 14, and that sum is minimal.

def minSum(nums, k):
    result = [-n for n in nums]
    h.heapify(result)
    for i in range(k):
        el = h.heappop(result)
        h.heappush(result, math.floor(el / 2))
    return sum([-n for n in sorted(result)])
