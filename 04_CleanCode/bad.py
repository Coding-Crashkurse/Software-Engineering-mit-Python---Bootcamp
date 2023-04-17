def clc(a, b, o):
    if o == "a":
        return a + b
    elif o == "m":
        return a * b
    elif o == "d":
        if b != 0:
            return a / b
        else:
            return None
    else:
        return None

result = clc(4, 2, "a")
print(result)
