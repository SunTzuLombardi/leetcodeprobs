#sortdict by values then keys
counts = {}
for i in words:
    if i in counts.keys():
        counts[i] += 1
    else:
        counts[i] = 1
sorted_values = {k: v for k, v in sorted(counts.items(), key=lambda x: (-x[1], x[0]))}

for i in sorted_values.items():
    print(i[0], i[1])

