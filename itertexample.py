import itertools as it

for n in it.count(15, 2):
    if n < 40:
        print(n, end='')
    else:
        break
