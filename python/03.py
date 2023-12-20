def height_of_water(inp):

    index = [i for i in range(len(inp))]
    sort = sorted(index, key=lambda i: inp[i])
    result = [0] * (len(inp)-1)

    for i in range(len(inp)-1):
        min_val = min(sort[i], sort[i+1])
        max_val = max(sort[i], sort[i+1])
        for j in range(min_val, max_val):
            result[j] = inp[sort[i]]
    return result


inp = list(map(int, input("Input : ").split(",")))

print(height_of_water(inp))
