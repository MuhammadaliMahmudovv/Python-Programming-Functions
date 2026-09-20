from typing import Dict

execution_time: Dict[str, float] = {}

import time
from functools import wraps

execution_time = {}


def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        execution_time[func.__name__] = end_time - start_time

        return result

    return wrapper
