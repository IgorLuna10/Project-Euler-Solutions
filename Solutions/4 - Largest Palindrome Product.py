def is_palindrome(n):
    # Convert to string and compare with its reverse
    return str(n) == str(n)[::-1]

def find_largest_palindrome():
    largest_pal = 0
    
    # Range starts at 999 and goes down to 100
    for i in range(999, 99, -1):
        # We start j at i to avoid redundant calculations (e.g., 900*800 vs 800*900)
        for j in range(i, 99, -1):
            product = i * j
            
            # If the product is smaller than our best find, 
            # no need to check smaller 'j' values in this loop
            if product <= largest_pal:
                break
                
            if is_palindrome(product):
                largest_pal = product
                
    return largest_pal

result = find_largest_palindrome()
print(f"The largest palindrome is: {result}")