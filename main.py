import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum_):
    coins_count = {}
    for coin in coins:
        count = sum_//coin
        if count > 0:
            coins_count[coin] = count
            sum_ -= coin * count
    return coins_count

def find_min_coins(sum_):
    min_coins_required = [0] + [float('inf')] * sum_
    last_coin_used = [0] * (sum_ + 1)
    for s in range(1, sum_ + 1):
        for coin in coins:
            if s >= coin and min_coins_required[s-coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s-coin] + 1
                last_coin_used[s] = coin
    coins_count = {}
    current_sum = sum_
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_sum -= coin
    return coins_count

def print_result(fun1, fun2, num):
    print(f"|{num:^15}|{timeit.timeit(lambda: fun1(num), number = 10):^25}|{timeit.timeit(lambda: fun2(num), number = 10):^25}|")



if __name__ == "__main__":
    print(f"greedy for 113: {find_coins_greedy(113)}")
    print(f"dynamic for 113: {find_min_coins(113)}")
    print(f"greedy for 1013: {find_coins_greedy(1013)}")
    print(f"dynamic for 1013: {find_min_coins(1013)}")
    print(f"|{'num':^15}|{'greedy':^25}|{'dynamic':^25}|")
    print(f"|{'-'*15}|{'-'*25}|{'-'*25}|")
    print_result(find_coins_greedy, find_min_coins, 13)
    print_result(find_coins_greedy, find_min_coins, 113)
    print_result(find_coins_greedy, find_min_coins, 1_013)
    print_result(find_coins_greedy, find_min_coins, 10_013)
    print_result(find_coins_greedy, find_min_coins, 1_000_013)

          
    
