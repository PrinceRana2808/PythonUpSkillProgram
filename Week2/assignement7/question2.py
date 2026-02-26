def infinite_multiples(n):
    multiple = 1
    while True:
        yield n * multiple
        multiple += 1

gen = infinite_multiples(3)

for _ in range(5):
    print(next(gen))