with open('data/1.txt') as file:
    lines = file.readlines()

pairs = [map(int, line.split()) for line in lines]
sorted_lists = map(sorted, zip(*pairs))
sorted_pairs = zip(*sorted_lists)
result = sum(map(lambda p: abs(p[0] - p[1]), sorted_pairs))
print(result)
