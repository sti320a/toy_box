nums = [1, 2, 3]

nums += [4]  # [1, 2, 3] + [4] = [1, 2, 3, 4]
print(nums)

nums.append([5]) # [1, 2, 3, 4] append [5] = [1, 2, 3, 4, [5]]
print(nums)

nums.append(6) # [1, 2, 3, 4, [5]] append 6 = [1, 2, 3, 4, [5], 6]
print(nums)

nums.append('7') # [1, 2, 3, 4, [5], 6, '7']
print(nums)

nums.append(object) # [1, 2, 3, 4, [5], 6, '7', <type 'object'>
print(nums)