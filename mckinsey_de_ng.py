#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countStableSegments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY capacity as parameter.
#
from collections import Counter


def countStableSegments(capacity):
    # print(len(capacity))
    # print(Counter(capacity))
    # return 1
    if len(Counter(capacity)) == 1 and len(capacity) != 1:

        return len(capacity) - 2
    n = len(capacity)
    count = 0
    prefix_sum = [0 for _ in range(n)]
    prefix_sum[0] = capacity[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + capacity[i]
    left = 0
    for left in range(n - 2):
        right = left + 2
        while right < n:
            if capacity[left] == capacity[right]:
                while prefix_sum[right - 1] - prefix_sum[left] < capacity[left]:
                    right += 1
                if capacity[left] == prefix_sum[right - 1] - prefix_sum[left]:
                    count += 1
            right += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    capacity_count = int(input().strip())

    capacity = []

    for _ in range(capacity_count):
        capacity_item = int(input().strip())
        capacity.append(capacity_item)

    result = countStableSegments(capacity)

    fptr.write(str(result) + '\n')

    fptr.close()
