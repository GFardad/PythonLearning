scores = [12, 19, 8, 15, 20, 10, 5, 17]
map_of_scores=map(lambda x:"exelent" if x >= 15 else "need amprovmnt",scores)
list(map(lambda x: print(f"{x}"),map_of_scores))
