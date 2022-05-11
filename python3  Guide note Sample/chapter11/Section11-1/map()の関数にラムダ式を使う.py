# map()の関数にラムダ式を使う
nums = [4, 3, 7, 6, 2, 1]
nums2 = list(map(lambda x: x * 2, nums))
# lambda x: x * 2, nums   ラムダ式
print(nums2)
