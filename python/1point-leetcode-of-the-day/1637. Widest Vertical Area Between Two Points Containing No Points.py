def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    x = []

    for i in range(len(points)):
        x.append(points[i][0])
    x.sort()
    max = 0
    for i in range(len(x)-1):
        if x[i+1] - x[i] > max:
            max = x[i+1] - x[i]

            print(x[i+1], x[i], "=", max)
    return max


input_points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
max = maxWidthOfVerticalArea(input_points)
print(max)
