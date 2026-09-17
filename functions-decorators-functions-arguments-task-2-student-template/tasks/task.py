def union(*args) -> set:
    elem = set(args[0])
    for i in args:
        elem = elem.union(i)
    return elem


def intersect(*args) -> set:
    elem = set(args[0])
    for i in args:
        elem = elem.intersection(i)
    return elem


