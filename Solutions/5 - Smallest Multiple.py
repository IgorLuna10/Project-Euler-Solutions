import math

def solve_euler_5(limit):
    result = 1
    for i in range(1, limit + 1):
        # The LCM of two numbers a and b is (a * b) // GCD(a, b)
        result = abs(result * i) // math.gcd(result, i)
    return result

# Project Euler asks for the range 1 to 20
n = 20
print(f"The smallest multiple of 1 to {n} is: {solve_euler_5(n)}")