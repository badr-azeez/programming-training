from timeit import default_timer

def timeis(n):
    time_st = default_timer()
    for n in range(0,n):
        continue

    print(default_timer() - time_st)

timeis(1000000)    