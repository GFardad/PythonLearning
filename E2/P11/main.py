visited = set()
def C2I (inp_string: str):
    char = inp_string[0]
    num = inp_string[1]
    char = ((ord(char.lower())) - (ord("a")))
    return(int(char),int(num)-1)
def calc_offset(x,y):
    offset = [[x+2,y+1],[x+2,y-1],[x-2,y+1],[x-2,y-1],[x+1,y+2],[x+1,y-2],[x-1,y+2],[x-1,y-2]]
    offset_t = [tuple(tuple(item)) for item in offset]
    return tuple(offset_t)
def validator(new_points):
    global visited
    for point in new_points:
        
    visited.add(new_points)
    print(visited)


print(validator(calc_offset(*C2I("A3"))))