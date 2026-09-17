from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    result = {}
    for i in range(1, num+1):
        result[i] = i**2
    return result

print(generate_squares(6))