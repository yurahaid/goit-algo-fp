import random


def get_dice_sum():
    return random.randint(1, 6) + random.randint(1, 6)


total_count = 10000
results = {key: 0 for key in range(2, 13)}

for i in range(total_count):
    sum = get_dice_sum()
    results[sum] = results[sum] + 1

probability_table = {}

for sum, count in results.items():
    probability_table[sum] = (count / total_count) * 100



# Друк заголовків таблиці
print(f"{'Sum':<10} {'Probability':<10}")
print("-" * 20)

# Друк кожної пари ключ-значення
for sim, probability in probability_table.items():
    print(f"{sim:<10} {probability:<10}")