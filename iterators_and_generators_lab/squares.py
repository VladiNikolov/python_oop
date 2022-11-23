def squares(n):
    num = 1

    while num <= n:
        yield num ** 2

        num += 1

s = squares(5)
my_list = []
for el in s:
    my_list.append(el)

print(my_list)


# print(list(squares(5)))