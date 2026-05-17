def solve_sum_square_difference(n):
    # 1. Calculate the sum of squares using the formula: n(n+1)(2n+1) / 6
    # We use integer division // because the result is guaranteed to be an integer.
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
    
    # 2. Calculate the sum of the first n numbers: n(n+1) / 2
    sum_of_n = (n * (n + 1)) // 2
    
    # 3. Square that sum
    square_of_sum = sum_of_n ** 2
    
    # 4. Find the absolute difference
    difference = square_of_sum - sum_of_squares
    
    return difference

# Execute for the first 100 numbers
limit = 100
result = solve_sum_square_difference(limit)
print(f"The difference for the first {limit} numbers is: {result}")