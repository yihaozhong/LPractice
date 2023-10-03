def xor(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

print(1^1)
print(1^2)
print(0^2^1^0^2)

def hm(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for key, value in count.items():
        if value == 1:
            return key
        
def max_profit(prices):
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price <min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit




from collections import defaultdict

def hm1(arr):
    count = defaultdict(int)
    for num in arr:
        count[num] +=1