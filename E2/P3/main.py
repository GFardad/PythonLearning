like = ["Peter", "Alex", "John", "Sarah", "Emily"]


def match_liek(names):
    match names:
        case []:
            return "no one likes this"
        case [name1]:  
            return f"{name1} likes this"
        case [name1, name2]:  
            return f"{name1} and {name2} like this"
        case [name1, name2, name3]:  
            return f"{name1}, {name2} and {name3} like this"
        case [name1, name2, *others]:  
            return f"{name1}, {name2} and {len(others)} others like this"


print(match_liek(like))
