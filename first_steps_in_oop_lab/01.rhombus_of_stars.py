def print_row(figure_size, row_size):
    print(" " * (figure_size - row_size), end="")
    for col in range(1, row_size + 1):
        print("*", end=" ")
    print()

number = int(input())

for row in range(1, number + 1):
    print_row(number, row)

for row in range(number - 1, - 1, - 1):
    print_row(number, row)
