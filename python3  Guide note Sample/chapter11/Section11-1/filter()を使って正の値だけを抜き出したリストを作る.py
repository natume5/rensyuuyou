# filter()を使って正の値だけを抜き出したリストを作る
nums = [4, -3, 9, 1, -2, -4, 5]
nums2 = list(filter(lambda x: x > 0, nums))
# filter   numsをフィルタリングする
print(nums2)
