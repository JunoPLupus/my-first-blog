def hi(name):
    print('Hello {}!'.format(name))

def area(side):
    return side * side

# hi("Ola")

small_square_area = area(2)
big_square_area = area(small_square_area)

print(small_square_area)
print(big_square_area)
