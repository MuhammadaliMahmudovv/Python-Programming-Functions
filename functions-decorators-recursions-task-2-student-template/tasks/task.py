from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    result_lst = []
    for i in sequence:
        if isinstance(i, (list, tuple, set)):
            result_lst.extend(linear_seq(i))
        else:
            result_lst.append(i)
    return result_lst