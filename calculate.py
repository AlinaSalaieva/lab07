import random
import string
N = int(input("Введіть кількість рядків: "))
def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
strings = [random_string(N) for _ in range(N)]
print("\nЗгенеровані рядки:")
for s in strings:
    print(s)
max_o_count = 0
string_with_max_o = ""
for s in strings:
    o_count = s.count('o')
    if o_count > max_o_count:
        max_o_count = o_count
        string_with_max_o = s
print("\nРядок з найбільшою кількістю 'o'це:")
print(string_with_max_o)
