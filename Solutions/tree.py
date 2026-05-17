
def tree(height):
    length = height * 2 - 1
    stars = 1

    for i in range(1, height + 1):
        print(("*" * stars).center(length))
        stars += 2

    trunk = height // 5
    if trunk == 0:
        trunk = 1

    for x in range(trunk):
        print("*".center(length))

    base = height + 1
    print(("*" * base).center(length))

tree(40)

