def intersect(set1, set2):
    new_set = set()
    for i in set1:
        for j in set2:
            if i == j:
                new_set.add(j)
    return new_set 