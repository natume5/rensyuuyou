# リスト内包表記を使った場合(filter)
nums = [4, -3, 9, 1, -2, -4, 5]
nums2 = [num for num in nums if num > 0]
# [num for num in nums if num > 0]   リスト内包表記
print(nums2)
