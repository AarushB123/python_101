
def is_even(x):
    """
    This function checks if a number is even.
    """
    if x % 2 == 0:
        return True
    else:
        return False

def print_even_numbers(x):
    """
    This function prints even numbers from 0 to x.
    """
    for i in range(0, x+1, 1):
        if is_even(i):
            print(i)

def sum(x, y):
    """
    This function returns the sum of two numbers.
    """
    return x + y


print(sum(2, 3))
print(sum(5, 10))
sum(10, 20)



print("Even numbers from 0 to 10:")
print_even_numbers(10)

print("Even numbers from 0 to 20:")
print_even_numbers(20)

print("Even numbers from 0 to 30:")
print_even_numbers(30)

print("Even numbers from 0 to 40:")
print_even_numbers(40)

print("Even numbers from 0 to 50:")
print_even_numbers(50)
