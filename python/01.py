def count_ways_to_walk(n):
    if n <= 0:
        return
    one, two = 1, 1

    for _ in range(n-1):
        temp = one+two
        # update value
        one = two
        two = temp
    return two


def display_ways(n, ls=[]):
    if n == 0:
        print(" → ".join(map(str, ls)))
        return
    elif n < 0:
        return
    display_ways(n-1, ls+[1])
    display_ways(n-2, ls+[2])


inp = int(input("Input : n = "))
print(f"Output : {count_ways_to_walk(inp)}")
display_ways(inp)
