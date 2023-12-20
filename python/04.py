def resolve(num, room):
    start = 1
    index = 0
    result = [None]*len(room)
    while (start <= num):
        for i in range(len(room)):
            if start == room[i]:
                index = i
                break
        result = check(result, index)
        start += 1
    return result


def check(lst_of_result, index):
    # <-------------------------------Left-Right Check----------------------------------->
    if index-1 < 0:
        left = None
    else:
        left = lst_of_result[index-1]

    if index+1 > (len(lst_of_result)-1):
        right = None
    else:
        right = lst_of_result[index+1]

    # <-------------------------------Level Check----------------------------------->
    if left == None and right == None:
        lst_of_result[index] = 0

    elif suspect_check(lst_of_result):
        lst_of_result[index] = 2

    else:
        lst_of_result[index] = 1

    return lst_of_result

 # <-------------------------------Suspect Check----------------------------------->
 # this fuction return boolean


def suspect_check(lst):
    # <-------------------------------Left-Rigth Check----------------------------------->
    for i in range(len(lst)-1):
        if i-1 < 0:
            left = None
        else:
            left = lst[i-1]

        if i+1 > (len(lst)-1):
            right = None
        else:
            right = lst[i+1]

        # if It's suspect return False
        # This row indicates that there is room available.
        if left == None and right == None:
            return True
    # It's not a suspect
    return False


inp1 = int(input("Input 1 : "))
inp2 = list(map(int, input("Input 2 : ").split(",")))
print(f"Output : {resolve(inp1, inp2)}")
