array = [3, 4, 2, 8, 10]
sorted = [0] * len(array)

for i in array:
    for j in sorted:
        while array[i] < sorted[j]:
            continue
        else:
            sorted[j] = array[i]

print(sorted)
