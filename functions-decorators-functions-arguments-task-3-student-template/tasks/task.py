from typing import Dict


def combine_dicts(*args: Dict[str, int]) -> Dict[str, int]:
    result = {}
    for i in args:
        for key, vaue in i.items():
            result[key] = result.get(key, 0) + vaue
    return result



