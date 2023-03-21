def closure_avg2():
    cnt = 0
    total = 0

    def averager2(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager2
