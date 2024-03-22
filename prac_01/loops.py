
# Part a
print("Part a:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Part b
print("\nPart b:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Part c
print("\nPart c:")
num_stars = int(input("Enter the number of stars: "))
for _ in range(num_stars):
    print('*', end='')
print()
