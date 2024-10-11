N = int(input("Введіть кількість рядків: "))
strings = [input(f"Введіть рядок {i+1}: ") for i in range(N)]

max_length = max(len(s) for s in strings)

padded_strings = [s.ljust(max_length, '*') for s in strings]

print("\nДоповнені рядки:")
for s in padded_strings:
    print(s)