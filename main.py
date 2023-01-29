import math

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = math.ceil((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if item < guess:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [
  -1024, -512, -256, -128, -64, -32, -16, -8, -4, -2, -1, 0, 1, 3, 5, 7, 9, 12,
  16, 32, 64, 128, 256, 512, 1024, 1025
]

for item in my_list:
    print(binary_search(my_list, item))