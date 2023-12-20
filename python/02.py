def cal_level_of_water(input1, input2):
    i = min(input2)

    while (input1 >= 1):
        l = 0
        for j in input2:
            sum = j-i
            if sum <= 0:
                l += 1
        if l <= input1:
            input1 = input1-l
            i += 1
        else:
            input1 = input1/l
            i = input1+i
    return i-min(input2)

input1 = int(input("Input 1 : "))
input2 = list(map(int, input("Input 2 : ").split(",")))
output = cal_level_of_water(input1, input2)
print(f"Output :{output: .2f}")
