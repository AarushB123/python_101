

def is_divisible_by_8(x):
    """
    This function checks if a number is divisible by 8.
    """
    remainder = x % 2 + x % 4
    #print(remainder)
    if remainder == 0:
        print(str(x) + " is divisible by 8")
    else:
        print(str(x) + " is not divisible by 8")

is_divisible_by_8(16)
is_divisible_by_8(15)
is_divisible_by_8(24)
is_divisible_by_8(1)
is_divisible_by_8(0)
is_divisible_by_8(-1)
