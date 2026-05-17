def tree(height):
    # 1. Total width of the tree's bottom-most row of stars
    width = height * 2 - 1
    stars = 1
    
    # 2. Draw the Leafy Canopy
    for i in range(1, height + 1):
        # We center the stars based on the widest star row
        print( ("*" * stars).center(width) )
        stars += 2
        
    # 3. Draw the Dynamic Trunk (1 star per 5 heights)
    trunk_height = height // 5
    if trunk_height == 0:
        trunk_height = 1
        
    for _ in range(trunk_height):
        print("*".center(width))
        
    # 4. Draw the Base (width of height + 1)
    # We use '=' or '-' to create a solid "ground" line
    base_width = height + 1
    print( ("=" * base_width).center(width) )

# Let's test it with height 15
tree(15)