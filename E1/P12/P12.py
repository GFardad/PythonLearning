import random
import time

y, d, h, m = 0, 0, 0, 0

moz = random.randint(0, 10 * 365 * 24 * 3600)

time_s = moz

y = time_s // 365 * 24 * 3600
time_s = time_s % 365 * 24 * 3600


d = time_s // 86400
time_s = time_s % 24 * 3600


h = time_s // 3600
time_s = time_s % 3600


m = time_s // 60
time_s = time_s % 60


print(
    f"{moz} seconde is => year : -{y}- | day : -{d}- | hour : -{h}- | minente : -{m}- seconde : -{time_s}-"
)
