def bsearch_solver(fn, x_min, x_max, target, accuracy=0.1):
    # start, end = x_min, x_max
    # if target < start or target > end:
    #     raise ValueError(f"start is : {start}, end is {end}, target is {target}. Not satisfy start < target < end")
    mid = (x_min + x_max) / 2
    mid_value = fn(mid)
    if target - accuracy < mid_value < target + accuracy:
        return mid
    elif target < mid_value:
        return bsearch_solver(fn, x_min, mid,  target, accuracy)
    else:
        return bsearch_solver(fn, mid, x_max, target, accuracy)