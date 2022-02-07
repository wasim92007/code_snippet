import itertools

nums = [1, 2, 3, 4]

nums_C_2 = itertools.combinations(nums, 2)
for x, y in nums_C_2:
    print(f'x:{x}, y:{y}')
