game_status = "X 7/ 90 X X 8/ 23 6/ X 8/1"


def spliter():
    status_list = game_status.split(" ")

    return status_list


def solve(status_list):
    result = 0
    for curr, i in zip(status_list, range(len(status_list))):
        # next_frame_sper = sts(status_list[i + 1][0])
        next_frame_full = status_list[i + 1]
        if "X" in curr:
            if "/" in (status_list[i + 1]):
                result = result + sts(curr, next_frame_full)
            else:
                result = result + sts(curr, next_frame_full)
        # elif "/" in curr:
        # if "X" in status_list[i + 1]:

        # else:
        #     result = result + 10 + int(status_list[i + 1][0])


def sts(inp, next_frame):

    if len(inp) == 2:
        sepprated_number = [str(inp)[i] for i in range(len(str(inp)))]
    if "X" in inp:
        return 10
    elif "/" in inp:
    
    return int()
