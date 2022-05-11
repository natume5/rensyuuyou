from collections import defaultdict


def count_characters(string):
    count_dict = defaultdict(int)
    for c in string:
        count_dict[c] += 1

    print(count_dict)


count_characters("Dynasty")
