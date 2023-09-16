def float2str(num, digit=3):
    num = str(num)
    idx = num.find(".")
    if idx == -1:
        if digit == 0:
            return num
        else:
            return num + "." + "0" * digit
    else:
        if digit == 0:
            return num[:idx]
        else:
            return num[:idx + digit + 1] + "0" * max(0, digit - (len(num) - idx - 1))