from typing import Dict

with open('data/1.txt') as file:
    lines = file.readlines()

pairs = [map(int, line.split()) for line in lines]
left_list, right_list = zip(*pairs)
right_list_counts: Dict[int, int] = {}
for n in right_list:
    right_list_counts[n] = right_list_counts.get(n, 0) + 1
result = sum(map(lambda n: n * right_list_counts.get(n, 0), left_list))

print(result)
 