from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    result = 0
    for i in sequence:
        try:
            result += i
        except TypeError:
            result += seq_sum(i)
    return result


print(seq_sum([1, 2, 3, [4, 5, (6, 7)]]))
