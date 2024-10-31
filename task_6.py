def greedy_algorithm(items: dict, budget: int):
    result = []
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    for name, item in sorted_items:
        if item['cost'] > budget:
            continue

        result.append(name)
        budget -= item['cost']

    return result

def dynamic_programming(items: dict, budget: int):
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]

    for item, details in items.items():
        cost = details['cost']
        calories = details['calories']
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                item_selection[b] = item_selection[b - cost] + [item]

    return item_selection[budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print(greedy_algorithm(items, 100))
print(dynamic_programming(items, 100))
