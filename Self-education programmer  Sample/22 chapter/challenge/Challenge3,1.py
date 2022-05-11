# 3問目と同じバブルソート

# !/usr/bin/env python
# -*- coding: utf-8 -*-


dt = [42, 21, 10, 2, 30, 51, 80, 90, 18, 56, 50, 25, 15,
      95, 44, 69]

for i in dt:
    for j in dt:
        k = dt.index(j) + 1
        if len(dt) > k and j > dt[k]:
            tmp = dt[k]
            dt[k] = j
            dt[dt.index(j)] = tmp

print(tmp)
